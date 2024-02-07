import pandas as pd
import numpy as np

if __name__== "__main__":
    adj_layer1_in = np.array(pd.read_csv("in_weighted/adj_layer1.csv", header=0,index_col=0))
    adj_layer2_in = np.array(pd.read_csv("in_weighted/adj_layer2.csv", header=0, index_col=0))
    adj_layer3_in = np.array(pd.read_csv("in_weighted/adj_layer3.csv", header=0, index_col=0))
    adj_layer4_in = np.array(pd.read_csv("in_weighted/adj_layer4.csv", header=0, index_col=0))

    adj_layer1_out = np.array(pd.read_csv("out_weighted/adj_layer1.csv", header=0,index_col=0))
    adj_layer2_out = np.array(pd.read_csv("out_weighted/adj_layer2.csv", header=0, index_col=0))
    adj_layer3_out = np.array(pd.read_csv("out_weighted/adj_layer3.csv", header=0, index_col=0))
    adj_layer4_out = np.array(pd.read_csv("out_weighted/adj_layer4.csv", header=0, index_col=0))

    adj_layer1_in_final = np.eye(adj_layer1_in.shape[0]) + adj_layer1_in
    adj_layer2_in_final = np.eye(adj_layer2_in.shape[0]) + adj_layer2_in
    adj_layer3_in_final = np.eye(adj_layer3_in.shape[0]) + adj_layer3_in
    adj_layer4_in_final = np.eye(adj_layer4_in.shape[0]) + adj_layer4_in

    adj_layer1_out_final = np.eye(adj_layer1_out.shape[0]) + adj_layer1_out
    adj_layer2_out_final = np.eye(adj_layer2_out.shape[0]) + adj_layer2_out
    adj_layer3_out_final = np.eye(adj_layer3_out.shape[0]) + adj_layer3_out
    adj_layer4_out_final = np.eye(adj_layer4_out.shape[0]) + adj_layer4_out

    pd.DataFrame(adj_layer1_in_final).to_csv("in_weighted/adj_layer1.csv")
    pd.DataFrame(adj_layer2_in_final).to_csv("in_weighted/adj_layer2.csv")
    pd.DataFrame(adj_layer3_in_final).to_csv("in_weighted/adj_layer3.csv")
    pd.DataFrame(adj_layer4_in_final).to_csv("in_weighted/adj_layer4.csv")

    pd.DataFrame(adj_layer1_out_final).to_csv("out_weighted/adj_layer1.csv")
    pd.DataFrame(adj_layer2_out_final).to_csv("out_weighted/adj_layer2.csv")
    pd.DataFrame(adj_layer3_out_final).to_csv("out_weighted/adj_layer3.csv")
    pd.DataFrame(adj_layer4_out_final).to_csv("out_weighted/adj_layer4.csv")