import numpy as np
import pandas as pd
import time


if __name__== "__main__":
    with open('../cluster_layers/layer1_cluster_datas_final.csv','w') as fin:
        fin.write("lng,lat,dens,row,col,layer1-cluster,cluster_order_final,center_final_lng,center_final_lat,layer\n")

    file_name='../cluster_layers/layer1/layer1_clusters.csv'
    cluster_datas=pd.read_csv(file_name)
    with open('../cluster_layers/layer1_cluster_datas_final.csv', 'a') as fin:
        for i in range(0,cluster_datas.shape[0]):
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
            fin.write(str(cluster_datas['layer1-cluster'][i]))
            fin.write(',')
            fin.write(str(cluster_datas['layer1-cluster'][i]))
            fin.write(',')
            fin.write(str(cluster_datas['layer1-center-lng'][i]))
            fin.write(',')
            fin.write(str(cluster_datas['layer1-center-lat'][i]))
            fin.write(',')
            fin.write(str(1))
            fin.write('\n')