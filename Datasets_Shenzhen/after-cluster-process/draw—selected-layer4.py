# import numpy as np
# import pandas as pd
#
# data0=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster1-layer3-cluster0-dens-1200).csv')
# data1=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster1-layer3-cluster1-dens-1200).csv')
# data2=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster1-layer3-cluster2-dens-1200).csv')
# data3=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster1-layer3-cluster3-dens-1200).csv')
# data4=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster2-layer3-cluster0-dens-1200).csv')
# data5=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster2-layer3-cluster1-dens-1200).csv')
# data6=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster2-layer3-cluster2-dens-1200).csv')
# data7=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster2-layer3-cluster3-dens-1200).csv')
# data8=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster3-layer3-cluster0-dens-1200).csv')
# data9=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster3-layer3-cluster1-dens-1200).csv')
# data10=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster3-layer3-cluster2-dens-1200).csv')
# data11=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster3-layer3-cluster3-dens-1200).csv')
# data12=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster4-layer3-cluster0-dens-1200).csv')
# data13=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster4-layer3-cluster1-dens-1200).csv')
# data14=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster4-layer3-cluster2-dens-1200).csv')
# data15=pd.read_csv('../cluster_layers/layer4/layer4_clusters_(layer1-cluster3-layer2-cluster4-layer3-cluster3-dens-1200).csv')
# data_final=pd.concat([data0, data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15], sort=False)
# data_final.to_csv("E:\DataMining\layer4_draw_R.csv")
# data_centers=data_final.drop_duplicates(subset=['cluster_order_final'], keep='first', inplace=False)
# data_centers.columns=['lng', 'lat', 'dens', 'row', 'col', 'layer1-cluster', 'layer2-cluster',
#        'layer3-cluster', 'layer4-cluster', 'centerlng',
#        'centerlat', 'cluster_order_final', 'layer']
# print(data_centers.columns)
# data_centers.to_csv("E:\DataMining\layer4_draw_R_centers.csv")

import pandas as pd

# 文件路径
file_path = "E:\TraficPre\Datasets_Shenzhen\cluster_layers\layer2_cluster_datas_final.csv"
output_file_path = "E:\DataMining\layer2_draw_R_centers.csv"

# 读取CSV文件
df = pd.read_csv(file_path, encoding='utf-8')

# 查看原始数据框的行数
print(f"原始数据行数: {len(df)}")

# 根据cluster_order_final列去重
# keep参数指定保留第一次出现的重复项，False表示删除所有重复项
df_dedup = df.drop_duplicates(subset='cluster_order_final', keep='first')

# 查望去重后的数据框的行数
print(f"去重后数据行数: {len(df_dedup)}")

# 将去重后的数据保存到新的CSV文件中
df_dedup.to_csv(output_file_path, index=False, encoding='utf-8')

print(f"去重后的数据已保存到: {output_file_path}")