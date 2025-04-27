# I published a working notebook of this example at https://www.kaggle.com/elmahy/a3t-gcn-for-traffic-forecasting

# The contribution makes training possible because it support batches of data

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch
from torch_geometric_temporal.dataset import ShenzhenDatasetLoader


DEVICE = torch.device('cuda') # cuda
shuffle=True
batch_size = 4
TIME_LEN=8
PRE_LEN=2
HIDDEN_DIM=64

loader = ShenzhenDatasetLoader()
dataset = loader.get_dataset(num_timesteps_in=TIME_LEN, num_timesteps_out=PRE_LEN)
print("Dataset type:  ", dataset)