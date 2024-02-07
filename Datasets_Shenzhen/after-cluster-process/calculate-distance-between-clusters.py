'''
This file is used to calculate the distance between the first 1152 clusters.
'''
import pandas as pd
import numpy as np
import math

LNG_range_meter=41223.05320706877#单位米
LAT_range_meter=38362.30250835731#单位米
LNG_MIN=113.78
LNG_MAX=114.1812
LAT_MIN=22.475
LAT_MAX=22.82
LAT_Resolution=(LAT_range_meter)/(LAT_MAX-LAT_MIN)
LNG_Resolution=(LNG_range_meter)/(LNG_MAX-LNG_MIN)
layer=2



def Calculate_Distances_Meter(lng0,lat0,lng1,lat1):
    return math.sqrt(np.power((lng0-lng1)*LNG_Resolution,2)+np.power((lat0-lat1)*LAT_Resolution,2))

if __name__== "__main__":
    clusters0=pd.read_csv('../cluster_layers/layer'+str(layer)+'_cluster_datas_final.csv')
    clusters_orders = clusters0['cluster_order_final'].unique()
    clusters_orders_num = len(clusters_orders)
    distances = np.zeros((clusters_orders_num, clusters_orders_num), dtype=float)
    clusters=clusters0[['cluster_order_final','center_final_lng','center_final_lat']]
    clusters=clusters.drop_duplicates().reset_index(drop=True)
    rows_num=clusters.shape[0]
    cols_num=clusters.shape[0]
    with open("../cluster_layers/distances/layer"+str(layer)+"_distances.csv",'w') as fin:
        fin.write('cluster_order_1,cluster_order_2,distance\n')
    for i in range(0,rows_num):
        for j in range(i+1,cols_num):
            distances[i][j] = Calculate_Distances_Meter(clusters['center_final_lng'][i],clusters['center_final_lat'][i],clusters['center_final_lng'][j],clusters['center_final_lat'][j])
            distances[j][i] = Calculate_Distances_Meter(clusters['center_final_lng'][i], clusters['center_final_lat'][i],clusters['center_final_lng'][j], clusters['center_final_lat'][j])
            with open("../cluster_layers/distances/layer"+str(layer)+"_distances.csv",'a') as fin:
                fin.write(str(clusters['cluster_order_final'][i]))
                fin.write(',')
                fin.write(str(clusters['cluster_order_final'][j]))
                fin.write(',')
                fin.write(str(distances[i][j]))
                fin.write('\n')
