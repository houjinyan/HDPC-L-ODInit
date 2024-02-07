import pandas as pd
import numpy as np

if __name__== "__main__":
    clusters_layer4 = pd.read_csv('layer4_clusters_final.csv')
    clusters_layer4.drop_duplicates(subset=['layer4-final-order'],keep='first', inplace=True)
    clusters_layer4=clusters_layer4.reset_index(drop=True)
    clusters_layer1 = pd.read_csv('../cluster_layers/layer1_cluster_datas_final.csv')
    clusters_layer1_orders = sorted(clusters_layer1['cluster_order_final'].unique().tolist())
    clusters_layer2 = pd.read_csv('../cluster_layers/layer2_cluster_datas_final.csv')
    clusters_layer2_orders = sorted(clusters_layer2['cluster_order_final'].unique().tolist())
    clusters_layer3 = pd.read_csv('../cluster_layers/layer3_cluster_datas_final.csv')
    clusters_layer3_orders = sorted(clusters_layer3['cluster_order_final'].unique().tolist())

    df = pd.DataFrame(columns=['layer1-order', 'layer2-order', 'layer3-order'])
    for i in range(0,clusters_layer4.shape[0]):
        layer4_final_order = str(clusters_layer4['layer4-final-order'][i])
        layer1_cluster = str(clusters_layer4['layer1-cluster'][i])
        layer2_cluster = layer1_cluster+str(clusters_layer4['layer2-cluster'][i])
        layer3_cluster = layer2_cluster+str(clusters_layer4['layer3-cluster'][i])

        index_layer1 = clusters_layer1_orders.index(int(layer1_cluster))
        index_layer2 = clusters_layer2_orders.index(int(layer2_cluster))
        index_layer3 = clusters_layer3_orders.index(int(layer3_cluster))
        df.loc[len(df.index)] = [index_layer1, index_layer2, index_layer3]

    pd.DataFrame(df).to_csv('layer_match.csv')