import numpy as np
import torch
import os
from math import sqrt
import pandas as pd
import torch.nn.functional as F
from torch_geometric_temporal.nn.recurrent import A3TGCN2
from torch_geometric_temporal.dataset import HaikouDatasetLoader_layer4_weighted,HaikouDatasetLoader_layer4_noweighted,HaikouDatasetLoader_layer3_weighted,HaikouDatasetLoader_layer3_noweighted
from torch_geometric_temporal.nn.recurrent.metrics import r2,explained_variance,accuracy
import time

# GPU support
DEVICE = torch.device('cuda') # cuda
batch_size = 16
TIME_LEN=16
PRE_LEN=4
HIDDEN_DIM=64
WEIGHTED=True
EPOCH=300

if(WEIGHTED==True):
    loader = HaikouDatasetLoader_layer4_weighted()
else:
    loader = HaikouDatasetLoader_layer4_noweighted()
dataset = loader.get_dataset(num_timesteps_in=TIME_LEN, num_timesteps_out=PRE_LEN)
print("Dataset type:  ", dataset)

# Train test split
from torch_geometric_temporal.signal import temporal_signal_split
train_dataset, test_dataset = temporal_signal_split(dataset, train_ratio=0.8)


# Creating Dataloaders
train_input = np.array(train_dataset.features) # (27399, 207, 2, 12)
train_target = np.array(train_dataset.targets) # (27399, 207, 12)
train_x_tensor = torch.from_numpy(train_input).type(torch.FloatTensor).to(DEVICE)  # (B, N, F, T)
train_target_tensor = torch.from_numpy(train_target).type(torch.FloatTensor).to(DEVICE)  # (B, N, T)
train_dataset_new = torch.utils.data.TensorDataset(train_x_tensor, train_target_tensor)
train_loader = torch.utils.data.DataLoader(train_dataset_new, batch_size=batch_size,drop_last=True)

test_input = np.array(test_dataset.features) # (, 207, 2, 12)
test_target = np.array(test_dataset.targets) # (, 207, 12)
test_x_tensor = torch.from_numpy(test_input).type(torch.FloatTensor).to(DEVICE)  # (B, N, F, T)
test_target_tensor = torch.from_numpy(test_target).type(torch.FloatTensor).to(DEVICE)  # (B, N, T)
test_dataset_new = torch.utils.data.TensorDataset(test_x_tensor, test_target_tensor)
test_loader = torch.utils.data.DataLoader(test_dataset_new, batch_size=batch_size,drop_last=True)


# Making the model 
class TemporalGNN(torch.nn.Module):
    def __init__(self, node_features, periods, batch_size):
        super(TemporalGNN, self).__init__()
        # Attention Temporal Graph Convolutional Cell
        self.tgnn1 = A3TGCN2(in_channels=node_features,  out_channels=HIDDEN_DIM, time_len=TIME_LEN,batch_size=batch_size)
        self.linear = torch.nn.Linear(HIDDEN_DIM, periods)
        self.sig = torch.nn.Sigmoid()

    def forward(self, x, edge_index, edge_attr):
        """
        x = Node features for T time steps
        edge_index = Graph edge indices
        """
        h = self.tgnn1(x, edge_index, edge_attr) # x [b, 207, 2, 12]  returns h [b, 207, 12]
        #h = self.sig(h)
        h = self.linear(h)
        return h

# Create model and optimizers
model = TemporalGNN(node_features=1, periods=PRE_LEN, batch_size=batch_size).to(DEVICE)
optimizer = torch.optim.Adam(model.parameters(), lr=0.0005,weight_decay=0)
loss_fn = torch.nn.MSELoss()


print('Net\'s state_dict:')
total_param = 0
for param_tensor in model.state_dict():
    print(param_tensor, '\t', model.state_dict()[param_tensor].size())
    total_param += np.prod(model.state_dict()[param_tensor].size())
print('Net\'s total params:', total_param)
#--------------------------------------------------
print('Optimizer\'s state_dict:')  # If you notice here the Attention is a trainable parameter
for var_name in optimizer.state_dict():
    print(var_name, '\t', optimizer.state_dict()[var_name])

# Loading the graph once because it's a static graph
for snapshot in train_dataset:
    static_edge_index = snapshot.edge_index.to(DEVICE)
    static_edge_weight = snapshot.edge_attr.to(DEVICE)
    break;


# Training the model 


df = pd.DataFrame(columns=['Epoch','Accuracy','RMSE','time'])
df_test = pd.DataFrame(columns=['Epoch','Accuracy','RMSE','R2','E_V','time'])

start=time.perf_counter()
for epoch in range(EPOCH):
    model.train()
    loss_list = []
    accuracy_list=[]
    for encoder_inputs, labels in train_loader:
        y_hat = model(encoder_inputs, static_edge_index,static_edge_weight)         # Get model predictions
        loss = loss_fn(y_hat, labels) # Mean squared error #loss = torch.mean((y_hat-labels)**2)  sqrt to change it to rmse
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_list.append(loss.item())
        accuracy_list.append(accuracy(y_hat.reshape(-1,y_hat.shape[1]),labels.reshape(-1,labels.shape[1])))
        accuracy_final = sum(accuracy_list) / len(accuracy_list)
        rmse_final = sqrt(sum(loss_list) / len(loss_list))
    print("epoch-",epoch,": ",sum(accuracy_list) / len(accuracy_list))
    print("Epoch {} train RMSE: {:.6f}".format(epoch, sqrt(sum(loss_list) / len(loss_list))))
    end1=time.perf_counter()
    df.loc[len(df)] = [str(epoch), str(accuracy_final.item()), str(rmse_final),str(end1-start)]

    ## Evaluation
    model.eval()
    with torch.no_grad():
        # Store for analysis
        total_loss = []
        accuracy_list = []
        r2_list = []
        explained_variance_list = []
        for encoder_inputs, labels in test_loader:
            # Get model predictions
            y_hat = model(encoder_inputs, static_edge_index, static_edge_weight)
            # Mean squared error
            loss = loss_fn(y_hat, labels)
            total_loss.append(loss.item())
            r2_list.append(r2(labels.reshape(-1, labels.shape[1]), y_hat.reshape(-1, y_hat.shape[1])))
            explained_variance_list.append(
                explained_variance(labels.reshape(-1, labels.shape[1]), y_hat.reshape(-1, y_hat.shape[1])))
            accuracy_list.append(accuracy(labels.reshape(-1, labels.shape[1]), y_hat.reshape(-1, y_hat.shape[1])))
    end2 = time.perf_counter()
    df_test.loc[len(df_test)] = [str(epoch), str((sum(accuracy_list) / len(accuracy_list)).item()),
                                 str((sqrt(sum(total_loss) / len(total_loss)))),
                                 str((sum(r2_list) / len(r2_list)).item()),
                                 str((sum(explained_variance_list) / len(explained_variance_list)).item()),str(end2-start)]

df.to_csv('A3TGCN_Train_Log_'+str(EPOCH)+'epoch_' + str(WEIGHTED) + '.csv')
df_test.to_csv('A3TGCN_Test_Log_'+str(EPOCH)+'epoch_' + str(WEIGHTED) + '.csv')

