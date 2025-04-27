from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize

adj_layer3_weighted=np.array(pd.read_csv('out_weighted/adj_layer2_weighted.csv', index_col=0,header=0))
# adj_layer3_weighted = adj_layer3_weighted-np.eye(adj_layer3_weighted.shape[0])
# adj_layer3_weighted = adj_layer3_weighted + adj_layer3_weighted.max()*np.eye(adj_layer3_weighted.shape[0])
adj_layer3_weighted = normalize(adj_layer3_weighted, axis=1, norm='l1')
pd.DataFrame(adj_layer3_weighted).to_csv('adj_layer2_weighted.csv')
# 练习的数据：
data = pd.read_csv('adj_layer2_weighted.csv', index_col=0)

# 绘制热度图：
plot = sns.heatmap(data,cmap="Purples")

plt.savefig('heatmap_weighted.jpg',dpi=800)