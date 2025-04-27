import numpy as np
import pandas as pd
import time

layer1_clusters_num=12

with open('../cluster_layers/layer2_cluster_datas_final.csv','w') as fin:
    fin.write("lng,lat,dens,row,col,layer1-cluster,layer2-cluster,cluster_order_final,center_final_lng,center_final_lat,layer\n")

for layer1_clusters_order in range(0,layer1_clusters_num):
    file_name='../cluster_layers/layer2/layer2_clusters_(layer1-cluster'+str(layer1_clusters_order)+'-dens-200).csv'
    cluster_datas=pd.read_csv(file_name)
    for i in range(0,cluster_datas.shape[0]):
        with open('../cluster_layers/layer2_cluster_datas_final.csv','a') as fin:
            fin.write(str(cluster_datas["lng"][i]))
            fin.write(',')
            fin.write(str(cluster_datas["lat"][i]))
            fin.write(',')
            fin.write(str(cluster_datas["dens"][i]))
            fin.write(',')
            fin.write(str(cluster_datas["row"][i]))
            fin.write(',')
            fin.write(str(cluster_datas["col"][i]))
            fin.write(',')
            fin.write(str(layer1_clusters_order))
            fin.write(',')
            fin.write(str(cluster_datas['layer2-cluster'][i]))
            fin.write(',')
            fin.write(str(layer1_clusters_order)+str(cluster_datas['layer2-cluster'][i]))
            fin.write(',')
            fin.write(str(cluster_datas['layer2-center-lng'][i]))
            fin.write(',')
            fin.write(str(cluster_datas['layer2-center-lat'][i]))
            fin.write(',')
            fin.write(str(2))
            fin.write('\n')