import numpy as np
import pandas as pd
from DPC_base import getDistanceMatrix,select_dc,get_density,get_deltas,find_centers_auto,find_centers_K,cluster_PD,draw_decision,draw_cluster
import time


layer=4
layer4_step=1200
layer1_clusters_num=12
layer2_clusters_num=6
layer3_clusters_num=4
layer4_clusters_num=4

def handleminicluster(clusterijk,layer1_clusters_order,layer2_clusters_order,layer3_clusters_order):
    with open("../cluster_layers/layer" + str(layer) + "/layer"+str(layer)+"_clusters_(layer1-cluster"+str(layer1_clusters_order)+"-layer2-cluster"+str(layer2_clusters_order)+"-layer3-cluster"+str(layer3_clusters_order)+"-dens-"+str(layer4_step)+").csv", "w") as fin:
        fin.write("lng,lat,dens,row,col,layer1-cluster,layer2-cluster,layer3-cluster,layer4-cluster,layer4-center-lng,layer4-center-lat,cluster_order_final,layer\n")
        for i in range(clusterijk.shape[0]):
            fin.write(str(clusterijk["lng"][i]))
            fin.write(',')
            fin.write(str(clusterijk["lat"][i]))
            fin.write(',')
            fin.write(str(clusterijk["dens"][i]))
            fin.write(',')
            fin.write(str(clusterijk["row"][i]))
            fin.write(',')
            fin.write(str(clusterijk["col"][i]))
            fin.write(',')
            fin.write(str(layer1_clusters_order))
            fin.write(',')
            fin.write(str(layer2_clusters_order))
            fin.write(',')
            fin.write(str(layer3_clusters_order))
            fin.write(',')
            fin.write(str(0))
            fin.write(',')
            fin.write(str(clusterijk['lng'][i]))
            fin.write(',')
            fin.write(str(clusterijk['lat'][i]))
            fin.write(',')
            fin.write(str(str(layer1_clusters_order)+str(layer2_clusters_order)+str(layer3_clusters_order)+str(0)))
            fin.write(',')
            fin.write(str(layer))
            fin.write('\n')

def get_clusters_DPC(datas,layer1_clusters_order,layer2_clusters_order,layer3_clusters_order,clusters_num):
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
                  name="../cluster_layers/layer" +str(layer) + "/layer" + str(layer) + "_(layer1-cluster"+str(layer1_clusters_order)+"-layer2-cluster"+str(layer2_clusters_order) +"-layer3-cluster"+str(layer3_clusters_order)+"-dens-"+str(layer4_step)+")_decision.jpg")
    # 获取聚类中心点
    centers = find_centers_K(rho,deltas,clusters_num,layer)
    print(centers)
    #centers = find_centers_auto(rho, deltas)
    #print("centers", centers)
    # 聚类 labs代表所属聚类编号
    labs = cluster_PD(rho, centers, nearest_neiber)
    # 可视化展示
    draw_cluster(datas_temp, labs, centers, dic_colors,
                 name="../cluster_layers/layer" + str(layer) + "/layer" + str(layer) + "_(layer1-cluster"+str(layer1_clusters_order) +"-layer2-cluster"+str(layer2_clusters_order) +"-layer3-cluster"+str(layer3_clusters_order)+"-dens-"+str(layer4_step)+")_cluster.jpg")
    with open("../cluster_layers/layer" + str(layer) + "/layer"+str(layer)+"_clusters_(layer1-cluster"+str(layer1_clusters_order)+"-layer2-cluster"+str(layer2_clusters_order)+"-layer3-cluster"+str(layer3_clusters_order)+"-dens-"+str(layer4_step)+").csv", "w") as fin:
        fin.write("lng,lat,dens,row,col,layer1-cluster,layer2-cluster,layer3-cluster,layer4-cluster,layer4-center-lng,layer4-center-lat,cluster_order_final,layer\n")
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
            fin.write(str(layer1_clusters_order))
            fin.write(',')
            fin.write(str(layer2_clusters_order))
            fin.write(',')
            fin.write(str(layer3_clusters_order))
            fin.write(',')
            fin.write(str(labs[i]))
            fin.write(',')
            fin.write(str(datas['lng'][centers[labs[i]]]))
            fin.write(',')
            fin.write(str(datas['lat'][centers[labs[i]]]))
            fin.write(',')
            fin.write(str(layer1_clusters_order)+str(layer2_clusters_order)+str(layer3_clusters_order)+str(labs[i]))
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
    for i in range(0,layer1_clusters_num):
        for j in range(0,layer2_clusters_num):
            for k in range(0,layer3_clusters_num):
                file_name = "../cluster_layers/layer"+str(layer)+"/layer"+str(layer)+"_(layer1-cluster"+str(i)+"-layer2-cluster"+str(j)+"-layer3-cluster"+str(k)+"-dens-"+str(layer4_step)+").csv"
                clusterij = pd.read_csv(file_name)
                try:
                    get_clusters_DPC(clusterij,i,j,k,layer4_clusters_num)
                except:
                    try:
                        handleminicluster(clusterij,i,j,k)
                    except:
                        pass
                        continue
    #i=6
    #j=5
    #k=0
    # for j in range(0,layer2_clusters_num):
    #     for k in range(0,layer3_clusters_num):
    #         file_name = "../cluster_layers/layer" + str(layer) + "/layer" + str(layer) + "_(layer1-cluster" + str(
    #             i) + "-layer2-cluster" + str(j) + "-layer3-cluster" + str(k) + "-dens-" + str(layer4_step) + ").csv"
    #         clusterijk = pd.read_csv(file_name)
    #         #handleminicluster(clusterijk, i, j, k)
    #         get_clusters_DPC(clusterijk,i,j,k,layer4_clusters_num)

    end=time.perf_counter()
    print('Running time: %s Seconds' % (end - start))

