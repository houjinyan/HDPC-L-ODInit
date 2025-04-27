import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

file_name_list=['out_weighted/adj_layer4_weighted','out/adj_layer4']

for file_name in file_name_list:
    # 读取CSV文件为DataFrame
    df = pd.read_csv(file_name+'.csv', index_col=0)

    # 确保DataFrame是数值型的
    df = df.apply(pd.to_numeric, errors='coerce')

    # 将对角线元素置为0
    np.fill_diagonal(df.values, 0)

    # 归一化处理：按行将数据缩放到[0, 1]区间
    def normalize_row(row):
        row_values = row.values.reshape(-1, 1)
        scaler = MinMaxScaler()
        scaled_values = scaler.fit_transform(row_values)
        return pd.Series(scaled_values.flatten(), index=row.index)

    df_normalized = df.apply(normalize_row, axis=1)

    # 定义颜色渐变，从白色(1, 1, 1)到深蓝色(0, 0, 128)
    colors = [(1, 1, 1), (0, 0, 128)]  # 可以根据需要调整目标颜色
    custom_cmap = LinearSegmentedColormap.from_list('custom blue', colors, N=256)

    # 绘制热力图并移除坐标轴刻度和边框线
    plt.figure(figsize=(8, 8))
    sns.heatmap(df_normalized, cmap=custom_cmap, vmin=0, vmax=1, cbar=True)
    print(df_normalized)
    # 获取当前图形的Axes对象
    ax = plt.gca()

    # 移除x轴和y轴的刻度标记
    plt.xticks([])  # 移除x轴刻度
    plt.yticks([])  # 如果也想移除y轴刻度，请取消此行注释

    # 隐藏边框线
    ax.spines['top'].set_visible(False)  # 隐藏顶部边框线
    ax.spines['right'].set_visible(False)  # 隐藏右侧边框线
    ax.spines['bottom'].set_visible(False)  # 隐藏底部边框线
    ax.spines['left'].set_visible(False)  # 隐藏左侧边框线

    # 设置颜色条标签
    cbar = plt.gcf().axes[-1]  # 获取当前图形最后一个轴，即颜色条
    cbar.set_ylabel('Weight Intensity')  # 设置颜色条的标签

    # 显示图形（如果需要显示）
    # plt.show()

    # 保存图形到文件（可选）
    plt.savefig(file_name+'.jpg', dpi=1000, bbox_inches='tight')