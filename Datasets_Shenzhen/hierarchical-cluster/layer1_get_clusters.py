#https://blog.csdn.net/qq_37055672/article/details/130000567
import numpy as np
import pandas as pd
from DPC_base import getDistanceMatrix,select_dc,get_density,get_deltas,find_centers_auto,find_centers_K,cluster_PD,draw_decision,draw_cluster

layer=1
dens=50
layer1_clusters_num=12

if __name__== "__main__":
    #画图保存的颜色卡
    dic_colors = {0:(.8,0,0),1:(0,.8,0),
                  2:(0,0,.8),3:(.8,.8,0),
                  4:(.8,0,.8),5:(0,.8,.8),
                  6:(0,0,0),7:(0.4,0.2,0),
                  8:(0.9,0.9,0.1),9:(0.2,0.3,0.4),
                  10:(0.7,0.2,0.9),11:(0.1,0.9,0.9),
                  12:(0.4,0.2,0.8),13:(0.5,0.6,0.9),
                  14:(0.32,0.89,0.18),15:(0.67,0.34,0.7),
                  16:(0.77,0.55,0.22),17:(0.19,0.32,0.76),
                  18:(0.59,0.12,0.78),19:(0.28,0.69,0.12)}
    #读取文件
    file_name = "../dens_shenzhen/dens_shenzhen_test_"+str(dens)+".csv"

    origin_datas = pd.read_csv(file_name)
    datas=origin_datas[origin_datas.columns[0:3]]
    datas = datas.values.tolist()
    datas=np.array(datas)
    # 计算距离矩阵
    dists = getDistanceMatrix(datas)

    # 计算dc
    dc = select_dc(dists)

    # 计算局部密度
    rho = get_density(datas,dists,dc,method="Gaussion")

    # 计算密度距离
    deltas, nearest_neiber= get_deltas(dists,rho)

    # 绘制密度/距离分布图
    draw_decision(datas,rho,deltas,name="../cluster_layers/"+"layer1/"+"layer"+str(layer)+"_dens-"+str(dens)+"_decision.jpg")

    # 获取聚类中心点
    centers = find_centers_K(rho,deltas,layer1_clusters_num,layer)

    #centers = find_centers_auto(rho,deltas)
    print("centers",centers)
    #聚类 labs代表所属聚类编号
    labs = cluster_PD(rho,centers,nearest_neiber)

    #可视化展示
    draw_cluster(datas,labs,centers, dic_colors, name="../cluster_layers/"+"layer1/"+"layer"+str(layer)+"_dens-"+str(dens)+"_cluster.jpg")
    with open("../cluster_layers/layer1/layer" + str(layer) + "_clusters.csv", "w") as fin:
        fin.write("lng,lat,dens,row,col,layer1-cluster,layer1-center-lng,layer1-center-lat,layer\n")
        for i in range(len(labs)):
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
            fin.write(str(labs[i]))
            #print(labs[i])
            fin.write(',')
            fin.write(str(origin_datas['lng'][centers[labs[i]]]))
            fin.write(',')
            fin.write(str(origin_datas['lat'][centers[labs[i]]]))
            fin.write(',')
            fin.write(str(layer))
            fin.write('\n')
