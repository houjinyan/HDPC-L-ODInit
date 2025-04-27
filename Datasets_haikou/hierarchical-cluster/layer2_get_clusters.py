import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from DPC_base import getDistanceMatrix,select_dc,get_density,get_deltas,find_centers_auto,find_centers_K,cluster_PD,draw_decision,draw_cluster
import time


layer=2
layer2_step=200
layer2_clusters_num=4

def get_clusters_DPC(datas,cluster_layer1,k):
    datas_temp=np.array(datas[['lng','lat','dens']])
    # 计算距离矩阵
    dists = getDistanceMatrix(datas_temp)
    # 计算dc
    dc = select_dc(dists)
    # 计算局部密度
    rho = get_density(datas_temp, dists, dc, method="Gaussion")
    # 计算密度距离
    deltas, nearest_neiber = get_deltas(dists, rho)
    # 绘制密度/距离分布图
    draw_decision(datas_temp, rho, deltas,
                  name="../cluster_layers/layer" +str(layer) + "/layer" + str(layer) + "_(layer1-cluster"+str(cluster_layer1)+ "-dens-"+str(layer2_step)+")_decision.jpg")
    # 获取聚类中心点
    centers = find_centers_K(rho,deltas,k,layer)
    #centers = find_centers_auto(rho, deltas)
    #print("centers", centers)
    # 聚类 labs代表所属聚类编号
    labs = cluster_PD(rho, centers, nearest_neiber)
    # 可视化展示
    draw_cluster(datas_temp, labs, centers, dic_colors,
                 name="../cluster_layers/layer" + str(layer) + "/layer" + str(layer) + "_(layer1-cluster"+str(cluster_layer1) + "-dens-"+str(layer2_step)+")_cluster.jpg")
    with open("../cluster_layers/layer" + str(layer) + "/layer"+str(layer)+"_clusters_(layer1-cluster"+str(cluster_layer1)+"-dens-"+str(layer2_step)+").csv", "w") as fin:
        fin.write("lng,lat,dens,row,col,layer1-cluster,layer2-cluster,layer2-center-lng,layer2-center-lat,layer\n")
        for i in range(len(labs)):
            fin.write(str(datas["lng"][i]))
            fin.write(',')
            fin.write(str(datas["lat"][i]))
            fin.write(',')
            fin.write(str(datas["dens"][i]))
            fin.write(',')
            fin.write(str(datas["row"][i]))
            fin.write(',')
            fin.write(str(datas["col"][i]))
            fin.write(',')
            fin.write(str(cluster_layer1))
            fin.write(',')
            fin.write(str(labs[i]))
            fin.write(',')
            fin.write(str(datas['lng'][centers[labs[i]]]))
            fin.write(',')
            fin.write(str(datas['lat'][centers[labs[i]]]))
            fin.write(',')
            fin.write(str(layer))
            fin.write('\n')


if __name__== "__main__":
    start = time.perf_counter()
    # 画图保存的颜色卡
    dic_colors = {0: (.8, 0, 0), 1: (0, .8, 0),
                  2: (0, 0, .8), 3: (.8, .8, 0),
                  4: (.8, 0, .8), 5: (0, .8, .8),
                  6: (0, 0, 0), 7: (0.4, 0.2, 0), 8: (0.9, 0.9, 0.1), 9: (0.2, 0.3, 0.4), 10: (0.7, 0.2, 0.9),
                  11: (0.1, 0.9, 0.9), 12: (0.4, 0.2, 0.8), 13: (0.5, 0.6, 0.9)}
    # 读取文件
    layer1_datas=pd.read_csv("../cluster_layers/layer1/layer1_clusters.csv")
    for i in range(0,layer1_datas['layer1-cluster'].nunique()):
        file_name = "../cluster_layers/layer"+str(layer)+"/layer"+str(layer)+"_(layer1-cluster"+str(i)+"-dens-"+str(layer2_step)+").csv"
        clusteri = pd.read_csv(file_name)
        get_clusters_DPC(clusteri,i,layer2_clusters_num)

    end=time.perf_counter()
    print('Running time: %s Seconds' % (end - start))