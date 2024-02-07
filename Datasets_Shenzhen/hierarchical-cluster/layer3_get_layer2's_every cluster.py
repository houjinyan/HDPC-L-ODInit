import time
import pandas as pd
from math import floor

layer=3
layer1_step=50
layer2_step=200
layer3_step=600
layer1_clusters_num=12
layer2_clusters_num=6
operator1=layer1_step/layer3_step
operator2=layer2_step/layer3_step

if __name__== "__main__":
    start=time.perf_counter()
    # 画图保存的颜色卡
    dic_colors = {0: (.8, 0, 0), 1: (0, .8, 0),
                  2: (0, 0, .8), 3: (.8, .8, 0),
                  4: (.8, 0, .8), 5: (0, .8, .8),
                  6: (0, 0, 0), 7: (0.4, 0.2, 0), 8: (0.9, 0.9, 0.1), 9: (0.2, 0.3, 0.4), 10: (0.7, 0.2, 0.9),
                  11: (0.1, 0.9, 0.9), 12: (0.4, 0.2, 0.8), 13: (0.5, 0.6, 0.9)}
    # 读取文件
    file_name_layer1 = "../cluster_layers/layer1/layer1_clusters.csv"
    file_name_origin="../dens_shenzhen/dens_shenzhen_test_"+str(layer3_step)+".csv"

    origin_datas = pd.read_csv(file_name_origin)
    layer1_datas=pd.read_csv(file_name_layer1)

    for i in range(0,layer1_clusters_num):
        for j in range(0,layer2_clusters_num):
            with open("../cluster_layers/" + "layer" + str(layer) + "/layer" + str(layer) + "_(layer1-cluster" + str(i) + "-layer2-cluster"+str(j)+"-dens-" + str(layer3_step) + ").csv", "w") as fin:
                fin.write("lng,lat,dens,row,col,layer1-cluster,layer2-cluster,layer\n")


    for i in range(0,origin_datas.shape[0]):
        layer1_cluster_order=layer1_datas[(layer1_datas['row']==floor(operator1*origin_datas['row'][i])) & (layer1_datas['col']==floor(operator1*origin_datas['col'][i]))]['layer1-cluster'].tolist()[0]
        layer2_datas=pd.read_csv('../cluster_layers/layer2/layer2_clusters_(layer1-cluster'+str(layer1_cluster_order)+'-dens-'+str(layer2_step)+').csv')
        layer2_cluster_order = layer2_datas[(layer2_datas['row'] == floor(operator2 * origin_datas['row'][i])) & (layer2_datas['col'] == floor(operator2 * origin_datas['col'][i]))]['layer2-cluster'].tolist()[0]
        with open("../cluster_layers/" + "layer" + str(layer) + "/layer" + str(layer) + "_(layer1-cluster" + str(layer1_cluster_order) + "-layer2-cluster"+str(layer2_cluster_order)+"-dens-" + str(layer3_step) + ").csv", "a") as fin:
            fin.write(str(origin_datas["lng"][i]))
            fin.write(',')
            fin.write(str(origin_datas["lat"][i]))
            fin.write(',')
            fin.write(str(origin_datas["dens"][i]))
            fin.write(',')
            fin.write(str(origin_datas["row"][i]))
            fin.write(',')
            fin.write(str(origin_datas["col"][i]))
            fin.write(',')
            fin.write(str(layer1_cluster_order))
            fin.write(',')
            fin.write(str(layer2_cluster_order))
            fin.write(',')
            fin.write(str(layer))
            fin.write('\n')

    end=time.perf_counter()
    print('Running time: %s Seconds' % (end - start))