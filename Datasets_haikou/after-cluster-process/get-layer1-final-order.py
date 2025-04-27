'''
This code is for getting the final cluster for trainset.(layer1:0~11; layer2:0~71; layer3:0~284; layer4:0~1144)
'''
import pandas as pd
import time

layer=1
layer1_step=50



if __name__== "__main__":
    start = time.perf_counter()
    clusters = pd.read_csv('../cluster_layers/layer' + str(layer) + '_cluster_datas_final.csv')
    clusters_orders = sorted(clusters['cluster_order_final'].unique().tolist())
    with open('layer'+str(layer)+'_clusters_final.csv','w') as fin:
        fin.write("lng,lat,dens,row,col,layer1-cluster,cluster_order_final,layer1-final-order,center_final_lng,center_final_lat,layer\n")
        for i in range(0,clusters.shape[0]):
            index = clusters_orders.index(clusters['cluster_order_final'][i])
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