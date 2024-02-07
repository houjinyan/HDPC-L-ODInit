import pandas as pd
import numpy as np

file_name_layer1_s_in='in\layer1_dataset_s.csv'
file_name_layer1_l_in='in\layer1_dataset_l.csv'
file_name_layer2_s_in='in\layer2_dataset_s.csv'
file_name_layer2_l_in='in\layer2_dataset_l.csv'

file_name_layer3_s_in='in\layer3_dataset_s.csv'
file_name_layer3_l_in='in\layer3_dataset_l.csv'
file_name_layer4_s_in='in\layer4_dataset_s.csv'
file_name_layer4_l_in='in\layer4_dataset_l.csv'

layer1_s_in=np.array(pd.read_csv(file_name_layer1_s_in,header=0,index_col=0))
layer1_l_in=np.array(pd.read_csv(file_name_layer1_l_in,header=0,index_col=0))
layer2_s_in=np.array(pd.read_csv(file_name_layer2_s_in,header=0,index_col=0))
layer2_l_in=np.array(pd.read_csv(file_name_layer2_l_in,header=0,index_col=0))

layer3_s_in=np.array(pd.read_csv(file_name_layer3_s_in,header=0,index_col=0))
layer3_l_in=np.array(pd.read_csv(file_name_layer3_l_in,header=0,index_col=0))
layer4_s_in=np.array(pd.read_csv(file_name_layer4_s_in,header=0,index_col=0))
layer4_l_in=np.array(pd.read_csv(file_name_layer4_l_in,header=0,index_col=0))


layer1_s_in[np.isnan(layer1_s_in)] = 0
layer1_l_in[np.isnan(layer1_l_in)] = 0
layer2_s_in[np.isnan(layer2_s_in)] = 0
layer2_l_in[np.isnan(layer2_l_in)] = 0

layer3_s_in[np.isnan(layer3_s_in)] = 0
layer3_l_in[np.isnan(layer3_l_in)] = 0
layer4_s_in[np.isnan(layer4_s_in)] = 0
layer4_l_in[np.isnan(layer4_l_in)] = 0

pd.DataFrame(layer1_s_in).to_csv("in\layer1_dataset_s.csv")
pd.DataFrame(layer1_l_in).to_csv("in\layer1_dataset_l.csv")
pd.DataFrame(layer2_s_in).to_csv("in\layer2_dataset_s.csv")
pd.DataFrame(layer2_l_in).to_csv("in\layer2_dataset_l.csv")
pd.DataFrame(layer1_s_in).to_csv("in_weighted\layer1_dataset_s.csv")
pd.DataFrame(layer1_l_in).to_csv("in_weighted\layer1_dataset_l.csv")
pd.DataFrame(layer2_s_in).to_csv("in_weighted\layer2_dataset_s.csv")
pd.DataFrame(layer2_l_in).to_csv("in_weighted\layer2_dataset_l.csv")

pd.DataFrame(layer3_s_in).to_csv("in\layer3_dataset_s.csv")
pd.DataFrame(layer3_l_in).to_csv("in\layer3_dataset_l.csv")
pd.DataFrame(layer4_s_in).to_csv("in\layer4_dataset_s.csv")
pd.DataFrame(layer4_l_in).to_csv("in\layer4_dataset_l.csv")
pd.DataFrame(layer3_s_in).to_csv("in_weighted\layer3_dataset_s.csv")
pd.DataFrame(layer3_l_in).to_csv("in_weighted\layer3_dataset_l.csv")
pd.DataFrame(layer4_s_in).to_csv("in_weighted\layer4_dataset_s.csv")
pd.DataFrame(layer4_l_in).to_csv("in_weighted\layer4_dataset_l.csv")


file_name_layer1_s_out='out\layer1_dataset_s.csv'
file_name_layer1_l_out='out\layer1_dataset_l.csv'
file_name_layer2_s_out='out\layer2_dataset_s.csv'
file_name_layer2_l_out='out\layer2_dataset_l.csv'

file_name_layer3_s_out='out\layer3_dataset_s.csv'
file_name_layer3_l_out='out\layer3_dataset_l.csv'
file_name_layer4_s_out='out\layer4_dataset_s.csv'
file_name_layer4_l_out='out\layer4_dataset_l.csv'

layer1_s_out=np.array(pd.read_csv(file_name_layer1_s_out,header=0,index_col=0))
layer1_l_out=np.array(pd.read_csv(file_name_layer1_l_out,header=0,index_col=0))
layer2_s_out=np.array(pd.read_csv(file_name_layer2_s_out,header=0,index_col=0))
layer2_l_out=np.array(pd.read_csv(file_name_layer2_l_out,header=0,index_col=0))

layer3_s_out=np.array(pd.read_csv(file_name_layer3_s_out,header=0,index_col=0))
layer3_l_out=np.array(pd.read_csv(file_name_layer3_l_out,header=0,index_col=0))
layer4_s_out=np.array(pd.read_csv(file_name_layer4_s_out,header=0,index_col=0))
layer4_l_out=np.array(pd.read_csv(file_name_layer4_l_out,header=0,index_col=0))

layer1_s_out[np.isnan(layer1_s_out)] = 0
layer1_l_out[np.isnan(layer1_l_out)] = 0
layer2_s_out[np.isnan(layer2_s_out)] = 0
layer2_l_out[np.isnan(layer2_l_out)] = 0

layer3_s_out[np.isnan(layer3_s_out)] = 0
layer3_l_out[np.isnan(layer3_l_out)] = 0
layer4_s_out[np.isnan(layer4_s_out)] = 0
layer4_l_out[np.isnan(layer4_l_out)] = 0

pd.DataFrame(layer1_s_out).to_csv("out\layer1_dataset_s.csv")
pd.DataFrame(layer1_l_out).to_csv("out\layer1_dataset_l.csv")
pd.DataFrame(layer2_s_out).to_csv("out\layer2_dataset_s.csv")
pd.DataFrame(layer2_l_out).to_csv("out\layer2_dataset_l.csv")
pd.DataFrame(layer1_s_out).to_csv("out_weighted\layer1_dataset_s.csv")
pd.DataFrame(layer1_l_out).to_csv("out_weighted\layer1_dataset_l.csv")
pd.DataFrame(layer2_s_out).to_csv("out_weighted\layer2_dataset_s.csv")
pd.DataFrame(layer2_l_out).to_csv("out_weighted\layer2_dataset_l.csv")

pd.DataFrame(layer3_s_out).to_csv("out\layer3_dataset_s.csv")
pd.DataFrame(layer3_l_out).to_csv("out\layer3_dataset_l.csv")
pd.DataFrame(layer4_s_out).to_csv("out\layer4_dataset_s.csv")
pd.DataFrame(layer4_l_out).to_csv("out\layer4_dataset_l.csv")
pd.DataFrame(layer3_s_out).to_csv("out_weighted\layer3_dataset_s.csv")
pd.DataFrame(layer3_l_out).to_csv("out_weighted\layer3_dataset_l.csv")
pd.DataFrame(layer4_s_out).to_csv("out_weighted\layer4_dataset_s.csv")
pd.DataFrame(layer4_l_out).to_csv("out_weighted\layer4_dataset_l.csv")

