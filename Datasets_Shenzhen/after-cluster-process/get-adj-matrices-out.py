import pandas as pd
import numpy as np
from pymongo import MongoClient
from sklearn.preprocessing import normalize

def normalize_digraph(A):
    Dl = np.sum(A, 0)  #计算邻接矩阵的度
    num_node = A.shape[0]
    Dn = np.zeros((num_node, num_node))
    for i in range(num_node):
        if Dl[i] > 0:
            Dn[i, i] = Dl[i]**(-1) #由每个点的度组成的对角矩阵
    AD = np.dot(A, Dn)
    return AD

threshold=0.01
layer1_clusters_num = 12
layer2_clusters_num = 72
layer3_clusters_num = 284
layer4_clusters_num = 1120
LNG_MIN=113.763
LNG_MAX=114.19
LAT_MIN=22.4725
LAT_MAX=22.826
layer1_step=50
layer2_step=200
layer3_step=600
layer4_step=1200


if __name__== "__main__":

    adj_layer1=np.zeros((layer1_clusters_num,layer1_clusters_num),dtype=int)
    adj_layer2=np.zeros((layer2_clusters_num,layer2_clusters_num),dtype=int)
    adj_layer3=np.zeros((layer3_clusters_num,layer3_clusters_num),dtype=int)
    adj_layer4=np.zeros((layer4_clusters_num,layer4_clusters_num),dtype=int)

    layer1_cluster_datas_final=pd.read_csv('layer1_clusters_final.csv')
    layer2_cluster_datas_final = pd.read_csv('layer2_clusters_final.csv')
    layer3_cluster_datas_final = pd.read_csv('layer3_clusters_final.csv')
    layer4_cluster_datas_final = pd.read_csv('layer4_clusters_final.csv')

    client = MongoClient("mongodb://localhost:27017/")
    db = client['交通类大数据']
    collection = db['shenzhen42_complete']
    num=0
    for x in collection.find():
        if(num%100000==0):
            print(num)
        START_LAYER1_FINAL_ORDER = int(x['START_LAYER1_FINAL_ORDER'])
        START_LAYER2_FINAL_ORDER = int(x['START_LAYER2_FINAL_ORDER'])
        START_LAYER3_FINAL_ORDER = int(x['START_LAYER3_FINAL_ORDER'])
        START_LAYER4_FINAL_ORDER = int(x['START_LAYER4_FINAL_ORDER'])
        END_LAYER1_FINAL_ORDER = int(x['END_LAYER1_FINAL_ORDER'])
        END_LAYER2_FINAL_ORDER = int(x['END_LAYER2_FINAL_ORDER'])
        END_LAYER3_FINAL_ORDER = int(x['END_LAYER3_FINAL_ORDER'])
        END_LAYER4_FINAL_ORDER = int(x['END_LAYER4_FINAL_ORDER'])
        if(START_LAYER1_FINAL_ORDER!=END_LAYER1_FINAL_ORDER):
            adj_layer1[START_LAYER1_FINAL_ORDER][END_LAYER1_FINAL_ORDER] += 1
            #adj_layer1[END_LAYER1_FINAL_ORDER][START_LAYER1_FINAL_ORDER] += 1
        if (START_LAYER2_FINAL_ORDER != END_LAYER2_FINAL_ORDER):
            adj_layer2[START_LAYER2_FINAL_ORDER][END_LAYER2_FINAL_ORDER] += 1
            #adj_layer2[END_LAYER2_FINAL_ORDER][START_LAYER2_FINAL_ORDER] += 1
        if (START_LAYER3_FINAL_ORDER != END_LAYER3_FINAL_ORDER):
            adj_layer3[START_LAYER3_FINAL_ORDER][END_LAYER3_FINAL_ORDER] += 1
            #adj_layer3[END_LAYER3_FINAL_ORDER][START_LAYER3_FINAL_ORDER] += 1
        if (START_LAYER4_FINAL_ORDER != END_LAYER4_FINAL_ORDER):
            adj_layer4[START_LAYER4_FINAL_ORDER][END_LAYER4_FINAL_ORDER] += 1
            #adj_layer4[END_LAYER4_FINAL_ORDER][START_LAYER4_FINAL_ORDER] += 1
        num+=1
    adj_layer1 = normalize(adj_layer1, axis=1, norm='l1')
    adj_layer2 = normalize(adj_layer2, axis=1, norm='l1')
    adj_layer3 = normalize(adj_layer3, axis=1, norm='l1')
    adj_layer4 = normalize(adj_layer4, axis=1, norm='l1')
    adj_layer1 = np.eye(adj_layer1.shape[0]) + adj_layer1
    adj_layer2 = np.eye(adj_layer2.shape[0]) + adj_layer2
    adj_layer3 = np.eye(adj_layer3.shape[0]) + adj_layer3
    adj_layer4 = np.eye(adj_layer4.shape[0]) + adj_layer4
    adj_layer1_non=np.where(adj_layer1, 1, 0)
    adj_layer2_non=np.where(adj_layer2, 1, 0)
    adj_layer3_non=np.where(adj_layer3, 1, 0)
    adj_layer4_non=np.where(adj_layer4, 1, 0)
    pd.DataFrame(adj_layer1_non).to_csv('out/adj_layer1.csv')
    pd.DataFrame(adj_layer2_non).to_csv('out/adj_layer2.csv')
    pd.DataFrame(adj_layer3_non).to_csv('out/adj_layer3.csv')
    pd.DataFrame(adj_layer4_non).to_csv('out/adj_layer4.csv')

    pd.DataFrame(adj_layer1_non).to_csv('out/adj_layer1_weighted.csv')
    pd.DataFrame(adj_layer2_non).to_csv('out/adj_layer2_weighted.csv')
    pd.DataFrame(adj_layer3_non).to_csv('out/adj_layer3_weighted.csv')
    pd.DataFrame(adj_layer4_non).to_csv('out/adj_layer4_weighted.csv')


    adj_layer1_0=np.where(adj_layer1 > threshold, adj_layer1, 0)
    adj_layer2_0=np.where(adj_layer2 > threshold, adj_layer2, 0)
    adj_layer3_0=np.where(adj_layer3 > threshold, adj_layer3, 0)
    adj_layer4_0=np.where(adj_layer4 > threshold, adj_layer4, 0)

    adj_layer1_1=np.where(adj_layer1_0, 1, 0)
    adj_layer2_1=np.where(adj_layer2_0, 1, 0)
    adj_layer3_1=np.where(adj_layer3_0, 1, 0)
    adj_layer4_1=np.where(adj_layer4_0, 1, 0)

    pd.DataFrame(adj_layer1_0).to_csv('out_weighted/adj_layer1_weighted.csv')
    pd.DataFrame(adj_layer2_0).to_csv('out_weighted/adj_layer2_weighted.csv')
    pd.DataFrame(adj_layer3_0).to_csv('out_weighted/adj_layer3_weighted.csv')
    pd.DataFrame(adj_layer4_0).to_csv('out_weighted/adj_layer4_weighted.csv')

    pd.DataFrame(adj_layer1_1).to_csv('out_weighted/adj_layer1.csv')
    pd.DataFrame(adj_layer2_1).to_csv('out_weighted/adj_layer2.csv')
    pd.DataFrame(adj_layer3_1).to_csv('out_weighted/adj_layer3.csv')
    pd.DataFrame(adj_layer4_1).to_csv('out_weighted/adj_layer4.csv')



