# 使用说明
1. 在这个命名体系中，如果无后缀代表对应的是根据每个结点的outflow的操作，如果后缀为in代表的是根据每个结点inflow的操作，这个代码是把outflow和inflow分开处理的。
2. 在这个命名体系中，如果后缀为noweighted，则代表使用的是未根据本论文提出的方法增强图的边权重；如果后缀为weighted，则代表使用该方法增强图的边权重。
3. 一共分为两个任务：第一个任务是HDPC-L的分层次聚类操作（对应Datasets_haikou和Datasets_Shenzhen两个文件夹）；第二个任务就是根据我们得到的邻接矩阵和数据集，去跑七个基线模型来得到实验结果（对应PyG_Haikou、PyG_Haikou_in、PyG_Shenzhen、PyG_Shenzhen_in、ST-SSL-main-300epoch和STPGCN-2pre六个文件夹）。

# Datasets_haikou和Datasets_Shenzhen
## Datasets_haikou
1. 运行Datasets_haikou/pre-process/get-diff-granularity-dens.py，得到海口数据集不同粒度下的分块处理结果。
2. 依次运行Datasets_haikou/hierarchical-cluster下的layer1_get_clusters.py、layer1_clusters_combine.py、layer2_get_layer1's_every_cluster.py、layer2_get_clusters.py、layer2_clusters_combine.py、layer3_get_layer2's_every_cluster.py、layer3_get_clusters.py、layer3_clusters_combine.py、layer4_get_layer3's_every_cluster.py、layer4_get_clusters、layer4_clusters_combine.py，得到海口数据集的四层分层次密度聚类的结果，具体保存的文件都位于Datasets_haikou/cluster_layers。
3. 运行Datasets_haikou/after-cluster-process下的store-every-layer-final-order.py将海口数据集下所有相关数据都存储到MongoDB中。
4. 运行Datasets_haikou/after-cluster-process下的get-adj-matrices-in.py和get-adj-matrices-out.py，得到海口数据集的inflow和outflow的邻接矩阵。
5. 运行Datasets_haikou/after-cluster-process下的get-final-dataset-in.py和get-final-dataset-out.py，得到海口数据集的inflow和outflow的每个结点流量数据集，并运行normalize-sml-dataset.py按照TGCN论文中的方法进行归一化处理。
6. Datasets_haikou/after-cluster-process下的get-layer{x}-final-order.py、adj-heatmap.py、before-after-compare.py和draw_adj.py是写论文画图用的，为的是将每层聚类统一处理绘制出来。

## Datasets_shenzhen
1. 运行Datasets_Shenzhen/pre-process/get-final-dataset-42days.py，筛选出我们使用的42天的深圳数据集（受疫情影响只有这个时间段数据量比较正常）。
2. 运行Datasets_Shenzhen/pre-process/get-diff-granularity-dens.py，得到深圳数据集不同粒度下的划分结果。
3. 依次运行Datasets_Shenzhen/hierarchical-cluster下的layer1_get_clusters.py、layer1_clusters_combine.py、layer2_get_layer1's_every_cluster.py、layer2_get_clusters.py、layer2_clusters_combine.py、layer3_get_layer2's_every_cluster.py、layer3_get_clusters.py、layer3_clusters_combine.py、layer4_get_layer3's_every_cluster.py、layer4_get_clusters、layer4_clusters_combine.py，得到深圳数据集的四层分层次密度聚类的结果，具体保存的文件都位于Datasets_Shenzhen/cluster_layers。
4. 运行Datasets_Shenzhen/after-cluster-process下的store-every-layer-final-order.py将深圳数据集下所有相关数据都存储到MongoDB中。
5. 运行Datasets_Shenzhen/after-cluster-process下的get-adj-matrices-in.py和get-adj-matrices-out.py，得到深圳数据集的inflow和outflow的邻接矩阵。
6. 运行Datasets_Shenzhen/after-cluster-process下的get-final-dataset-in.py和get-final-dataset-out.py，得到深圳数据集的inflow和outflow的每个结点流量数据集，并运行normalize-sml-dataset.py按照TGCN论文中的方法进行归一化处理。
7. Datasets_Shenzhen/after-cluster-process下的get-layer{x}-final-order.py、adj-heatmap.py、before-after-compare.py和draw_adj.py是写论文画图用的，为的是将每层聚类统一处理绘制出来。

# PyG_Haikou、PyG_Haikou_in、PyG_Shenzhen、PyG_Shenzhen_in、ST-SSL-main-300epoch和STPGCN-2pre
## PyG_Haikou
1. 把前面得到的Datasets_haikou得到的数据放到PyG_Haikou/self_models/recurrent/data下(in、in_weighted、out和out_weighted四个文件夹)。
2. 这个文件夹下的文件除了run.py都是会用到的模型文件，运行run.py就可以得到实验结果。

## PyG_Haikou_in
1. 把前面得到的Datasets_haikou得到的数据放到PyG_Haikou_in/self_models/recurrent/data下(in、in_weighted、out和out_weighted四个文件夹)。
2. 这个文件夹下的文件除了run.py都是会用到的模型文件，运行run.py就可以得到实验结果。

## PyG_Shenzhen
1. 把前面得到的Datasets_Shenzhen得到的数据放到PyG_Shenzhen/self_models/recurrent/data下(in、in_weighted、out和out_weighted四个文件夹)。
2. 这个文件夹下的文件除了run.py都是会用到的模型文件，运行run.py就可以得到实验结果。

## PyG_Shenzhen_in
1. 把前面得到的Datasets_Shenzhen得到的数据放到PyG_Shenzhen_in/self_models/recurrent/data下(in、in_weighted、out和out_weighted四个文件夹)。
2. 这个文件夹下的文件除了run.py都是会用到的模型文件，运行run.py就可以得到实验结果。

## ST-SSL-main-300epoch
1. 把前面Datasets_haikou和Datasets_Shenzhen得到的数据放到ST-SSL-main-300epoch/ST-SSL-main/data下。
2. 运行ST-SSL-main-300epoch/ST-SSL-main/settle_our_datasets.py将我们的数据处理成ST-SSL源码需要的格式。
3. 运行ST-SSL-main-300epoch/ST-SSL-main/run.py就可以得到实验结果。

## STPGCN-2pre
1. 把前面Datasets_haikou和Datasets_Shenzhen得到的数据放到STPGCN-2pre/STPGCN-main/Pytorch/data/dataset下。
2. 运行STPGCN-2pre/STPGCN-main/Pytorch/run.py得到实验结果。