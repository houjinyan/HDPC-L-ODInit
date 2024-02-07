'''
This code is for getting the final cluster for trainset.(layer1:0~11; layer2:0~71; layer3:0~287; layer4:0~1146)
'''
import pandas as pd
import time

layer=4
layer1_step=50
layer2_step=200
layer3_step=600
layer4_step=1200
layer1_clusters_num=12
layer2_clusters_num=6
layer3_clusters_num=4
layer4_clusters_num=4

# def Get_Cluster_Order_Layer4(layer1_order,layer2_order,layer3_order,layer4_order):
#     return layer1_order*96+layer2_order*16+layer3_order*4+layer4_order
#
# def Get_Cluster_Order_Layer3(layer1_order,layer2_order,layer3_order):
#     return layer1_order*24+layer2_order*4+layer3_order
#
# def Get_Cluster_Order_Layer2(layer1_order,layer2_order):
#     return layer1_order*6+layer2_order


if __name__== "__main__":
    start = time.perf_counter()
    clusters = pd.read_csv('../cluster_layers/layer' + str(layer) + '_cluster_datas_final.csv')
    clusters_orders = sorted(clusters['cluster_order_final'].unique().tolist())
    with open('layer'+str(layer)+'_clusters_final.csv','w') as fin:
        fin.write("lng,lat,dens,row,col,layer1-cluster,layer2-cluster,layer3-cluster,layer4-cluster,cluster_order_final,layer4-final-order,center_final_lng,center_final_lat,layer\n")
        for i in range(0,clusters.shape[0]):
            index=clusters_orders.index(clusters['cluster_order_final'][i])
            fin.write(str(clusters["lng"][i]))
            fin.write(',')
            fin.write(str(clusters["lat"][i]))
            fin.write(',')
            fin.write(str(clusters["dens"][i]))
            fin.write(',')
            fin.write(str(clusters["row"][i]))
            fin.write(',')
            fin.write(str(clusters["col"][i]))
            fin.write(',')
            fin.write(str(clusters["layer1-cluster"][i]))
            fin.write(',')
            fin.write(str(clusters["layer2-cluster"][i]))
            fin.write(',')
            fin.write(str(clusters["layer3-cluster"][i]))
            fin.write(',')
            fin.write(str(clusters["layer4-cluster"][i]))
            fin.write(',')
            fin.write(str(clusters["cluster_order_final"][i]))
            fin.write(',')
            fin.write(str(index))
            fin.write(',')
            fin.write(str(clusters['center_final_lng'][i]))
            fin.write(',')
            fin.write(str(clusters['center_final_lat'][i]))
            fin.write(',')
            fin.write(str(layer))
            fin.write('\n')
    end=time.perf_counter()
    print('Running time: %s Seconds' % (end - start))