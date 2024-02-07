import pandas as pd
import numpy as np
if __name__== "__main__":
    #IN part
    layer1_s_in = np.array(pd.read_csv('in_weighted/layer1_dataset_s.csv',header=0,index_col=0))
    layer1_m_in = np.array(pd.read_csv('in_weighted/layer1_dataset_m.csv',header=0,index_col=0))
    layer1_l_in = np.array(pd.read_csv('in_weighted/layer1_dataset_l.csv',header=0,index_col=0))
    layer2_s_in = np.array(pd.read_csv('in_weighted/layer2_dataset_s.csv',header=0,index_col=0))
    layer2_m_in = np.array(pd.read_csv('in_weighted/layer2_dataset_m.csv',header=0,index_col=0))
    layer2_l_in = np.array(pd.read_csv('in_weighted/layer2_dataset_l.csv',header=0,index_col=0))
    layer3_s_in = np.array(pd.read_csv('in_weighted/layer3_dataset_s.csv',header=0,index_col=0))
    layer3_m_in = np.array(pd.read_csv('in_weighted/layer3_dataset_m.csv',header=0,index_col=0))
    layer3_l_in = np.array(pd.read_csv('in_weighted/layer3_dataset_l.csv',header=0,index_col=0))
    layer4_s_in = np.array(pd.read_csv('in_weighted/layer4_dataset_s.csv',header=0,index_col=0))
    layer4_m_in = np.array(pd.read_csv('in_weighted/layer4_dataset_m.csv',header=0,index_col=0))
    layer4_l_in = np.array(pd.read_csv('in_weighted/layer4_dataset_l.csv',header=0,index_col=0))

    layer1_s_norm_in = layer1_s_in / layer1_s_in.max()#(axis=0)
    pd.DataFrame(layer1_s_norm_in).to_csv("in_weighted/layer1_dataset_s.csv")
    pd.DataFrame(layer1_s_norm_in).to_csv("in/layer1_dataset_s.csv")

    layer1_m_norm_in = layer1_m_in / layer1_m_in.max()#(axis=0)
    pd.DataFrame(layer1_m_norm_in).to_csv("in_weighted/layer1_dataset_m.csv")
    pd.DataFrame(layer1_m_norm_in).to_csv("in/layer1_dataset_m.csv")

    layer1_l_norm_in = layer1_l_in / layer1_l_in.max()#(axis=0)
    pd.DataFrame(layer1_l_norm_in).to_csv("in_weighted/layer1_dataset_l.csv")
    pd.DataFrame(layer1_l_norm_in).to_csv("in/layer1_dataset_l.csv")

    layer2_s_norm_in = layer2_s_in / layer2_s_in.max()#(axis=0)
    pd.DataFrame(layer2_s_norm_in).to_csv("in_weighted/layer2_dataset_s.csv")
    pd.DataFrame(layer2_s_norm_in).to_csv("in/layer2_dataset_s.csv")

    layer2_m_norm_in = layer2_m_in / layer2_m_in.max()#(axis=0)
    pd.DataFrame(layer2_m_norm_in).to_csv("in_weighted/layer2_dataset_m.csv")
    pd.DataFrame(layer2_m_norm_in).to_csv("in/layer2_dataset_m.csv")

    layer2_l_norm_in = layer2_l_in / layer2_l_in.max()#(axis=0)
    pd.DataFrame(layer2_l_norm_in).to_csv("in_weighted/layer2_dataset_l.csv")
    pd.DataFrame(layer2_l_norm_in).to_csv("in/layer2_dataset_l.csv")

    layer3_s_norm_in = layer3_s_in / layer3_s_in.max()#(axis=0)
    pd.DataFrame(layer3_s_norm_in).to_csv("in_weighted/layer3_dataset_s.csv")
    pd.DataFrame(layer3_s_norm_in).to_csv("in/layer3_dataset_s.csv")

    layer3_m_norm_in = layer3_m_in / layer3_m_in.max()#(axis=0)
    pd.DataFrame(layer3_m_norm_in).to_csv("in_weighted/layer3_dataset_m.csv")
    pd.DataFrame(layer3_m_norm_in).to_csv("in/layer3_dataset_m.csv")

    layer3_l_norm_in = layer3_l_in / layer3_l_in.max()#(axis=0)
    pd.DataFrame(layer3_l_norm_in).to_csv("in_weighted/layer3_dataset_l.csv")
    pd.DataFrame(layer3_l_norm_in).to_csv("in/layer3_dataset_l.csv")

    layer4_s_norm_in = layer4_s_in / layer4_s_in.max()#(axis=0)
    pd.DataFrame(layer4_s_norm_in).to_csv("in_weighted/layer4_dataset_s.csv")
    pd.DataFrame(layer4_s_norm_in).to_csv("in/layer4_dataset_s.csv")

    layer4_m_norm_in = layer4_m_in / layer4_m_in.max()#(axis=0)
    pd.DataFrame(layer4_m_norm_in).to_csv("in_weighted/layer4_dataset_m.csv")
    pd.DataFrame(layer4_m_norm_in).to_csv("in/layer4_dataset_m.csv")

    layer4_l_norm_in = layer4_l_in / layer4_l_in.max()#(axis=0)
    pd.DataFrame(layer4_l_norm_in).to_csv("in_weighted/layer4_dataset_l.csv")
    pd.DataFrame(layer4_l_norm_in).to_csv("in/layer4_dataset_l.csv")

    #OUT part
    layer1_s_out = np.array(pd.read_csv('out_weighted/layer1_dataset_s.csv',header=0,index_col=0))
    layer1_m_out = np.array(pd.read_csv('out_weighted/layer1_dataset_m.csv',header=0,index_col=0))
    layer1_l_out = np.array(pd.read_csv('out_weighted/layer1_dataset_l.csv',header=0,index_col=0))
    layer2_s_out = np.array(pd.read_csv('out_weighted/layer2_dataset_s.csv',header=0,index_col=0))
    layer2_m_out = np.array(pd.read_csv('out_weighted/layer2_dataset_m.csv',header=0,index_col=0))
    layer2_l_out = np.array(pd.read_csv('out_weighted/layer2_dataset_l.csv',header=0,index_col=0))
    layer3_s_out = np.array(pd.read_csv('out_weighted/layer3_dataset_s.csv',header=0,index_col=0))
    layer3_m_out = np.array(pd.read_csv('out_weighted/layer3_dataset_m.csv',header=0,index_col=0))
    layer3_l_out = np.array(pd.read_csv('out_weighted/layer3_dataset_l.csv',header=0,index_col=0))
    layer4_s_out = np.array(pd.read_csv('out_weighted/layer4_dataset_s.csv',header=0,index_col=0))
    layer4_m_out = np.array(pd.read_csv('out_weighted/layer4_dataset_m.csv',header=0,index_col=0))
    layer4_l_out = np.array(pd.read_csv('out_weighted/layer4_dataset_l.csv',header=0,index_col=0))

    layer1_s_norm_out = layer1_s_out / layer1_s_out.max()#(axis=0)
    pd.DataFrame(layer1_s_norm_out).to_csv("out_weighted/layer1_dataset_s.csv")
    pd.DataFrame(layer1_s_norm_out).to_csv("out/layer1_dataset_s.csv")

    layer1_m_norm_out = layer1_m_out / layer1_m_out.max()#(axis=0)
    pd.DataFrame(layer1_m_norm_out).to_csv("out_weighted/layer1_dataset_m.csv")
    pd.DataFrame(layer1_m_norm_out).to_csv("out/layer1_dataset_m.csv")

    layer1_l_norm_out = layer1_l_out / layer1_l_out.max()#(axis=0)
    pd.DataFrame(layer1_l_norm_out).to_csv("out_weighted/layer1_dataset_l.csv")
    pd.DataFrame(layer1_l_norm_out).to_csv("out/layer1_dataset_l.csv")

    layer2_s_norm_out = layer2_s_out / layer2_s_out.max()#(axis=0)
    pd.DataFrame(layer2_s_norm_out).to_csv("out_weighted/layer2_dataset_s.csv")
    pd.DataFrame(layer2_s_norm_out).to_csv("out/layer2_dataset_s.csv")

    layer2_m_norm_out = layer2_m_out / layer2_m_out.max()#(axis=0)
    pd.DataFrame(layer2_m_norm_out).to_csv("out_weighted/layer2_dataset_m.csv")
    pd.DataFrame(layer2_m_norm_out).to_csv("out/layer2_dataset_m.csv")

    layer2_l_norm_out = layer2_l_out / layer2_l_out.max()#(axis=0)
    pd.DataFrame(layer2_l_norm_out).to_csv("out_weighted/layer2_dataset_l.csv")
    pd.DataFrame(layer2_l_norm_out).to_csv("out/layer2_dataset_l.csv")

    layer3_s_norm_out = layer3_s_out / layer3_s_out.max()#(axis=0)
    pd.DataFrame(layer3_s_norm_out).to_csv("out_weighted/layer3_dataset_s.csv")
    pd.DataFrame(layer3_s_norm_out).to_csv("out/layer3_dataset_s.csv")

    layer3_m_norm_out = layer3_m_out / layer3_m_out.max()#(axis=0)
    pd.DataFrame(layer3_m_norm_out).to_csv("out_weighted/layer3_dataset_m.csv")
    pd.DataFrame(layer3_m_norm_out).to_csv("out/layer3_dataset_m.csv")

    layer3_l_norm_out = layer3_l_out / layer3_l_out.max()#(axis=0)
    pd.DataFrame(layer3_l_norm_out).to_csv("out_weighted/layer3_dataset_l.csv")
    pd.DataFrame(layer3_l_norm_out).to_csv("out/layer3_dataset_l.csv")

    layer4_s_norm_out = layer4_s_out / layer4_s_out.max()#(axis=0)
    pd.DataFrame(layer4_s_norm_out).to_csv("out_weighted/layer4_dataset_s.csv")
    pd.DataFrame(layer4_s_norm_out).to_csv("out/layer4_dataset_s.csv")

    layer4_m_norm_out = layer4_m_out / layer4_m_out.max()#(axis=0)
    pd.DataFrame(layer4_m_norm_out).to_csv("out_weighted/layer4_dataset_m.csv")
    pd.DataFrame(layer4_m_norm_out).to_csv("out/layer4_dataset_m.csv")

    layer4_l_norm_out = layer4_l_out / layer4_l_out.max()#(axis=0)
    pd.DataFrame(layer4_l_norm_out).to_csv("out_weighted/layer4_dataset_l.csv")
    pd.DataFrame(layer4_l_norm_out).to_csv("out/layer4_dataset_l.csv")

