import os
import pandas as pd
import numpy as np
import torch
from ..signal import StaticGraphTemporalSignal

LAYER=4
WEIGHTED=True

class ShenzhenDatasetLoader_layer4_weighted(object):
    def __init__(self,raw_data_dir=os.path.join(os.getcwd(), "data")):
        super(ShenzhenDatasetLoader_layer4_weighted, self).__init__()
        self.raw_data_dir = raw_data_dir
        self._read_web_data()

    def _read_web_data(self):
        A = np.array(pd.read_csv(os.path.join(self.raw_data_dir, "out_weighted\\adj_layer"+str(LAYER)+".csv"),header=0,index_col=0))
        X = np.expand_dims(np.array(pd.read_csv(os.path.join(self.raw_data_dir, "out_weighted\\layer"+str(LAYER)+"_dataset_s.csv"),header=0,index_col=0)),axis=2).transpose((1, 2, 0))
        W = np.array(pd.read_csv(os.path.join(self.raw_data_dir, "out_weighted\\adj_layer"+str(LAYER)+"_weighted.csv"),header=0,index_col=0))
        # X = np.expand_dims(np.load(os.path.join(self.raw_data_dir, "node_values.npy")),axis=2).transpose(
        #     (1, 2, 0)
        # )
        X = X.astype(np.float32)
        W = W.astype(np.float32)

        self.A = torch.from_numpy(A)
        self.X = torch.from_numpy(X)
        self.W = torch.from_numpy(W)


    def _get_edges_and_weights(self):
        list_start=[]
        list_end=[]
        weights=[]
        for i in range(self.A.shape[0]):
            for j in range(self.A.shape[1]):
                if(self.A[i][j]==1):
                    list_start.append(i)
                    list_end.append(j)
                    if(WEIGHTED==True):
                        weights.append(self.W[i][j])
                        #print(i,"-",j,"-",self.W[i][j])
                    else:
                        weights.append(1)

        list_start=np.array(list_start)
        list_end=np.array(list_end)
        weights=np.array(weights)
        self.edges = np.vstack((list_start,list_end))
        self.edge_weights = weights


    def _generate_task(self, num_timesteps_in: int = 12, num_timesteps_out: int = 4):
        """Uses the node features of the graph and generates a feature/target
        relationship of the shape
        (num_nodes, num_node_features, num_timesteps_in) -> (num_nodes, num_timesteps_out)
        predicting the average traffic speed using num_timesteps_in to predict the
        traffic conditions in the next num_timesteps_out

        Args:
            num_timesteps_in (int): number of timesteps the sequence model sees
            num_timesteps_out (int): number of timesteps the sequence model has to predict
        """
        indices = [
            (i, i + (num_timesteps_in + num_timesteps_out))
            for i in range(self.X.shape[2] - (num_timesteps_in + num_timesteps_out) + 1)
        ]

        # Generate observations
        features, target = [], []
        for i, j in indices:
            features.append((self.X[:, :, i : i + num_timesteps_in]).numpy())
            target.append((self.X[:, 0, i + num_timesteps_in : j]).numpy())

        self.features = features
        self.targets = target

    def get_dataset(
        self, num_timesteps_in: int = 12, num_timesteps_out: int = 4
    ) -> StaticGraphTemporalSignal:
        """Returns data iterator for METR-LA dataset as an instance of the
        static graph temporal signal class.

        Return types:
            * **dataset** *(StaticGraphTemporalSignal)* - The METR-LA traffic
                forecasting dataset.
        """
        self._get_edges_and_weights()
        self._generate_task(num_timesteps_in, num_timesteps_out)
        dataset = StaticGraphTemporalSignal(
            self.edges, self.edge_weights, self.features, self.targets
        )

        return dataset