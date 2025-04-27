import matplotlib.pyplot as plt
import colorsys
import random
import pandas as pd

def get_n_hls_colors(num):
    hls_colors = []
    i = 0
    step = 360.0 / num
    while i < 360:
        h = i
        s = 90 + random.random() * 10
        l = 50 + random.random() * 10
        _hlsc = [h / 360.0, l / 100.0, s / 100.0]
        hls_colors.append(_hlsc)
        i += step

    return hls_colors


def ncolors(num):
    rgb_colors = []
    if num < 1:
        return rgb_colors
    hls_colors = get_n_hls_colors(num)
    for hlsc in hls_colors:
        _r, _g, _b = colorsys.hls_to_rgb(hlsc[0], hlsc[1], hlsc[2])
        r, g, b = [int(x * 255.0) for x in (_r, _g, _b)]
        rgb_colors.append([r, g, b])

    return rgb_colors


def color(value):
    digit = list(map(str, range(10))) + list("ABCDEF")
    if isinstance(value, tuple):
        string = '#'
        for i in value:
            a1 = i // 16
            a2 = i % 16
            string += digit[a1] + digit[a2]
        return string
    elif isinstance(value, str):
        a1 = digit.index(value[1]) * 16 + digit.index(value[2])
        a2 = digit.index(value[3]) * 16 + digit.index(value[4])
        a3 = digit.index(value[5]) * 16 + digit.index(value[6])
        return (a1, a2, a3)

if __name__ == "__main__":
    clusters_datas_final=pd.read_csv("../cluster_layers/layer3_cluster_datas_final.csv")
    clusters_datas_final = clusters_datas_final[
        ~((clusters_datas_final['center_final_lng'] <= 113.8) & (clusters_datas_final['center_final_lat'] <= 22.6))]
    clusters_orders=clusters_datas_final['cluster_order_final'].unique()
    clusters_orders_num=len(clusters_orders)
    colors=list(map(lambda x: color(tuple(x)), ncolors(clusters_orders_num)))
    print(clusters_orders_num)
    plt.figure(dpi=4000)
    for k in range(0,clusters_orders_num):
        clusters_datas_k=clusters_datas_final[clusters_datas_final['cluster_order_final']==clusters_orders[k]].reset_index()
        plt.scatter(clusters_datas_k['lng'],clusters_datas_k['lat'],color=colors[k])
        plt.scatter(clusters_datas_k['center_final_lng'], clusters_datas_k['center_final_lat'], color="k", marker=".", s=20.)
    plt.savefig('../cluster_layers/layer3_clusters_final.jpg')
