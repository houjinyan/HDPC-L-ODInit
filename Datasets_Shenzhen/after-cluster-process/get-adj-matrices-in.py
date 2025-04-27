import pandas as pd
import numpy as np
from pymongo import MongoClient
from sklearn.preprocessing import normalize

def map_layer4_order(a_mapping: dict, b_mapping: dict, layer4_order: int) -> int:
    """
    根据给定的 layer4_order，在 a_mapping 中找到对应的 cluster_order_final，
    然后在 b_mapping 中找到相同 cluster_order_final 对应的 layer4_final_order。
    """
    # 先从 a_mapping 找到 cluster_order_final
    cluster_order = a_mapping.get(layer4_order)
    if cluster_order is None:
        return None  # 如果找不到，返回 None

    # 再从 b_mapping 找到对应的 layer4-final-order
    return b_mapping.get(cluster_order)

def filter_row(row,threshold=0.9):
    # 获取原始索引
    original_indices = np.argsort(-row)
    # 排序后的数组（降序）
    sorted_row = row[original_indices]
    cumulative_sum = 0
    for i, value in enumerate(sorted_row):
        cumulative_sum += value
        if cumulative_sum >= threshold:
            break

    # 将未达到阈值的元素置为0
    sorted_row[i + 1:] = 0
    # 应用额外的阈值：小于0.01的值置为0
    sorted_row[sorted_row < 0.01] = 0
    # 将处理后的值放回原位置
    filtered_row = np.zeros_like(row)
    filtered_row[original_indices] = sorted_row

    return filtered_row

def normalize_digraph(A):
    Dl = np.sum(A, 0)  #计算邻接矩阵的度
    num_node = A.shape[0]
    Dn = np.zeros((num_node, num_node))
    for i in range(num_node):
        if Dl[i] > 0:
            Dn[i, i] = Dl[i]**(-1) #由每个点的度组成的对角矩阵
    AD = np.dot(A, Dn)
    return AD

# threshold=0.01
# layer1_clusters_num = 12
# layer2_clusters_num = 72
# layer3_clusters_num = 284
layer4_clusters_num = 1115
# LNG_MIN=113.763
# LNG_MAX=114.19
# LAT_MIN=22.4725
# LAT_MAX=22.826
# layer1_step=50
# layer2_step=200
# layer3_step=600
# layer4_step=1200


if __name__== "__main__":

    dfA=pd.read_csv("layer4_clusters_final.csv")
    dfB=pd.read_csv("layer4_clusters_final_exSea.csv")

    # 创建映射关系
    a_mapping = dict(zip(dfA['layer4-final-order'], dfA['cluster_order_final']))
    b_mapping = dict(zip(dfB['cluster_order_final'], dfB['layer4-final-order']))
    print(a_mapping)
    print(b_mapping)

    # adj_layer1=np.zeros((layer1_clusters_num,layer1_clusters_num),dtype=int)
    # adj_layer2=np.zeros((layer2_clusters_num,layer2_clusters_num),dtype=int)
    # adj_layer3=np.zeros((layer3_clusters_num,layer3_clusters_num),dtype=int)
    adj_layer4=np.zeros((layer4_clusters_num,layer4_clusters_num),dtype=int)

    # layer1_cluster_datas_final=pd.read_csv('layer1_clusters_final.csv')
    # layer2_cluster_datas_final = pd.read_csv('layer2_clusters_final.csv')
    # layer3_cluster_datas_final = pd.read_csv('layer3_clusters_final.csv')
    #layer4_cluster_datas_final = pd.read_csv('layer4_clusters_final_exSea.csv')

    client = MongoClient("mongodb://localhost:27017/")
    db = client['交通类大数据']
    collection = db['shenzhen42_complete']
    num=0
    count=0
    edge=0
    for x in collection.find():
        if(num%100000==0):
            print(num)
        # START_LAYER1_FINAL_ORDER = int(x['START_LAYER1_FINAL_ORDER'])
        # START_LAYER2_FINAL_ORDER = int(x['START_LAYER2_FINAL_ORDER'])
        # START_LAYER3_FINAL_ORDER = int(x['START_LAYER3_FINAL_ORDER'])
        START_LAYER4_FINAL_ORDER = int(x['START_LAYER4_FINAL_ORDER'])
        START_LAYER4_FINAL_ORDER = map_layer4_order(a_mapping, b_mapping, START_LAYER4_FINAL_ORDER)
        # END_LAYER1_FINAL_ORDER = int(x['END_LAYER1_FINAL_ORDER'])
        # END_LAYER2_FINAL_ORDER = int(x['END_LAYER2_FINAL_ORDER'])
        # END_LAYER3_FINAL_ORDER = int(x['END_LAYER3_FINAL_ORDER'])
        END_LAYER4_FINAL_ORDER = int(x['END_LAYER4_FINAL_ORDER'])
        END_LAYER4_FINAL_ORDER = map_layer4_order(a_mapping, b_mapping, END_LAYER4_FINAL_ORDER)
        if((START_LAYER4_FINAL_ORDER is None) or (END_LAYER4_FINAL_ORDER is None)):
            print(START_LAYER4_FINAL_ORDER)
            print(END_LAYER4_FINAL_ORDER)
            count+=1
            continue
        # if(START_LAYER1_FINAL_ORDER!=END_LAYER1_FINAL_ORDER):
        #     #adj_layer1[START_LAYER1_FINAL_ORDER][END_LAYER1_FINAL_ORDER] += 1
        #     adj_layer1[END_LAYER1_FINAL_ORDER][START_LAYER1_FINAL_ORDER] += 1
        # if (START_LAYER2_FINAL_ORDER != END_LAYER2_FINAL_ORDER):
        #     #adj_layer2[START_LAYER2_FINAL_ORDER][END_LAYER2_FINAL_ORDER] += 1
        #     adj_layer2[END_LAYER2_FINAL_ORDER][START_LAYER2_FINAL_ORDER] += 1
        # if (START_LAYER3_FINAL_ORDER != END_LAYER3_FINAL_ORDER):
        #     #adj_layer3[START_LAYER3_FINAL_ORDER][END_LAYER3_FINAL_ORDER] += 1
        #     adj_layer3[END_LAYER3_FINAL_ORDER][START_LAYER3_FINAL_ORDER] += 1
        if (START_LAYER4_FINAL_ORDER != END_LAYER4_FINAL_ORDER):
            edge+=1
            #adj_layer4[START_LAYER4_FINAL_ORDER][END_LAYER4_FINAL_ORDER] += 1
            adj_layer4[END_LAYER4_FINAL_ORDER][START_LAYER4_FINAL_ORDER] += 1
        num+=1
    # adj_layer1 = normalize(adj_layer1, axis=1, norm='l1')
    # adj_layer2 = normalize(adj_layer2, axis=1, norm='l1')
    # adj_layer3 = normalize(adj_layer3, axis=1, norm='l1')
    adj_layer4 = normalize(adj_layer4, axis=1, norm='l1')
    adj_layer4_filter = np.array([filter_row(row) for row in adj_layer4])

    # adj_layer1 = np.eye(adj_layer1.shape[0]) + adj_layer1
    # adj_layer2 = np.eye(adj_layer2.shape[0]) + adj_layer2
    # adj_layer3 = np.eye(adj_layer3.shape[0]) + adj_layer3
    adj_layer4 = np.eye(adj_layer4.shape[0]) + adj_layer4
    # adj_layer1_non=np.where(adj_layer1, 1, 0)
    # adj_layer2_non=np.where(adj_layer2, 1, 0)
    # adj_layer3_non=np.where(adj_layer3, 1, 0)
    adj_layer4_non=np.where(adj_layer4, 1, 0)
    # pd.DataFrame(adj_layer1_non).to_csv('in/adj_layer1.csv')
    # pd.DataFrame(adj_layer2_non).to_csv('in/adj_layer2.csv')
    # pd.DataFrame(adj_layer3_non).to_csv('in/adj_layer3.csv')
    pd.DataFrame(adj_layer4_non).to_csv('in/adj_layer4.csv')
    # pd.DataFrame(adj_layer1_non).to_csv('in/adj_layer1_weighted.csv')
    # pd.DataFrame(adj_layer2_non).to_csv('in/adj_layer2_weighted.csv')
    # pd.DataFrame(adj_layer3_non).to_csv('in/adj_layer3_weighted.csv')
    pd.DataFrame(adj_layer4_non).to_csv('in/adj_layer4_weighted.csv')

    # adj_layer1_0=np.where(adj_layer1 > threshold, adj_layer1, 0)
    # adj_layer2_0=np.where(adj_layer2 > threshold, adj_layer2, 0)
    # adj_layer3_0=np.where(adj_layer3 > threshold, adj_layer3, 0)
    #adj_layer4_0=np.where(adj_layer4 > threshold, adj_layer4, 0)
    adj_layer4_0 = np.eye(adj_layer4_filter.shape[0]) +adj_layer4_filter

    # adj_layer1_1=np.where(adj_layer1_0, 1, 0)
    # adj_layer2_1=np.where(adj_layer2_0, 1, 0)
    # adj_layer3_1=np.where(adj_layer3_0, 1, 0)
    adj_layer4_1=np.where(adj_layer4_0, 1, 0)

    # pd.DataFrame(adj_layer1_0).to_csv('in_weighted/adj_layer1_weighted.csv')
    # pd.DataFrame(adj_layer2_0).to_csv('in_weighted/adj_layer2_weighted.csv')
    # pd.DataFrame(adj_layer3_0).to_csv('in_weighted/adj_layer3_weighted.csv')
    pd.DataFrame(adj_layer4_0).to_csv('in_weighted/adj_layer4_weighted.csv')

    # pd.DataFrame(adj_layer1_1).to_csv('in_weighted/adj_layer1.csv')
    # pd.DataFrame(adj_layer2_1).to_csv('in_weighted/adj_layer2.csv')
    # pd.DataFrame(adj_layer3_1).to_csv('in_weighted/adj_layer3.csv')
    pd.DataFrame(adj_layer4_1).to_csv('in_weighted/adj_layer4.csv')
    print("edges: ",edge)




