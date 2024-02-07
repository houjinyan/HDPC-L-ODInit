import numpy as np
import pandas as pd
in_filename="..\\after-cluster-process\in\\adj_layer4.csv"
in_weighted_filename="..\\after-cluster-process\in_weighted\\adj_layer4.csv"
out_filename="..\\after-cluster-process\out\\adj_layer4.csv"
out_weighted_filename="..\\after-cluster-process\out_weighted\\adj_layer4.csv"

in_matrix = np.array(pd.read_csv(in_filename,header=0,index_col=0))
in_weighted_matrix = np.array(pd.read_csv(in_weighted_filename,header=0,index_col=0))
print(np.count_nonzero(in_matrix == 1))
print(np.count_nonzero(in_weighted_matrix == 1))

out_matrix = np.array(pd.read_csv(out_filename,header=0,index_col=0))
out_weighted_matrix = np.array(pd.read_csv(out_weighted_filename,header=0,index_col=0))
print(np.count_nonzero(out_matrix == 1))
print(np.count_nonzero(out_weighted_matrix == 1))