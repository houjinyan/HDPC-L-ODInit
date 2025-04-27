import pandas as pd
import numpy as np
from pymongo import MongoClient
import datetime

layer1_clusters_num = 5
layer2_clusters_num = 20
layer3_clusters_num = 60
layer4_clusters_num = 180
days_num=184
s_num=48
l_num=24

def GetRowOrder(s,l,day):
    s_order=day*s_num+l*2+s
    l_order=day*l_num+l
    return s_order,l_order

if __name__== "__main__":
    layer1_dataset_s = np.zeros((days_num * s_num,layer1_clusters_num),dtype=int)
    layer1_dataset_l = np.zeros((days_num * l_num,layer1_clusters_num), dtype=int)

    layer2_dataset_s = np.zeros((days_num * s_num,layer2_clusters_num),dtype=int)
    layer2_dataset_l = np.zeros((days_num * l_num,layer2_clusters_num), dtype=int)

    layer3_dataset_s = np.zeros((days_num * s_num,layer3_clusters_num),dtype=int)
    layer3_dataset_l = np.zeros((days_num * l_num,layer3_clusters_num), dtype=int)

    layer4_dataset_s = np.zeros((days_num * s_num,layer4_clusters_num),dtype=int)
    layer4_dataset_l = np.zeros((days_num * l_num,layer4_clusters_num), dtype=int)

    client = MongoClient("mongodb://localhost:27017/")
    db = client['交通类大数据']
    collection = db['haikou180_complete']
    num=0
    for x in collection.find():
        day_start=int(x['DAY_START'])-121
        START_S_SLOT_ORDER=int(x['START_S_SLOT_ORDER'])
        START_L_SLOT_ORDER = int(x['START_L_SLOT_ORDER'])
        # day_end=int(x['DAY_END'])-137
        # END_S_SLOT_ORDER=int(x['END_S_SLOT_ORDER'])
        # END_M_SLOT_ORDER = int(x['END_M_SLOT_ORDER'])
        # END_L_SLOT_ORDER = int(x['END_L_SLOT_ORDER'])

        START_LAYER1_FINAL_ORDER = int(x['START_LAYER1_FINAL_ORDER'])
        START_LAYER2_FINAL_ORDER = int(x['START_LAYER2_FINAL_ORDER'])
        START_LAYER3_FINAL_ORDER = int(x['START_LAYER3_FINAL_ORDER'])
        START_LAYER4_FINAL_ORDER = int(x['START_LAYER4_FINAL_ORDER'])
        # END_LAYER1_FINAL_ORDER = int(x['END_LAYER1_FINAL_ORDER'])
        # END_LAYER2_FINAL_ORDER = int(x['END_LAYER2_FINAL_ORDER'])
        # END_LAYER3_FINAL_ORDER = int(x['END_LAYER3_FINAL_ORDER'])
        # END_LAYER4_FINAL_ORDER = int(x['END_LAYER4_FINAL_ORDER'])

        s_start_order,l_start_order=GetRowOrder(START_S_SLOT_ORDER,START_L_SLOT_ORDER,day_start)
        #s_end_order,m_end_order,l_end_order = GetRowOrder(END_S_SLOT_ORDER, END_M_SLOT_ORDER,day_end)

        layer1_dataset_s[s_start_order][START_LAYER1_FINAL_ORDER] += 1
        layer2_dataset_s[s_start_order][START_LAYER2_FINAL_ORDER] += 1
        layer3_dataset_s[s_start_order][START_LAYER3_FINAL_ORDER] += 1
        layer4_dataset_s[s_start_order][START_LAYER4_FINAL_ORDER] += 1

        layer1_dataset_l[l_start_order][START_LAYER1_FINAL_ORDER] += 1
        layer2_dataset_l[l_start_order][START_LAYER2_FINAL_ORDER] += 1
        layer3_dataset_l[l_start_order][START_LAYER3_FINAL_ORDER] += 1
        layer4_dataset_l[l_start_order][START_LAYER4_FINAL_ORDER] += 1


        # layer1_dataset_s[s_end_order][END_LAYER1_FINAL_ORDER] += 1
        # layer2_dataset_s[s_end_order][END_LAYER2_FINAL_ORDER] += 1
        # layer3_dataset_s[s_end_order][END_LAYER3_FINAL_ORDER] += 1
        # layer4_dataset_s[s_end_order][END_LAYER4_FINAL_ORDER] += 1
        #
        # layer1_dataset_m[m_end_order][END_LAYER1_FINAL_ORDER] += 1
        # layer2_dataset_m[m_end_order][END_LAYER2_FINAL_ORDER] += 1
        # layer3_dataset_m[m_end_order][END_LAYER3_FINAL_ORDER] += 1
        # layer4_dataset_m[m_end_order][END_LAYER4_FINAL_ORDER] += 1
        #
        # layer1_dataset_l[l_end_order][END_LAYER1_FINAL_ORDER] += 1
        # layer2_dataset_l[l_end_order][END_LAYER2_FINAL_ORDER] += 1
        # layer3_dataset_l[l_end_order][END_LAYER3_FINAL_ORDER] += 1
        # layer4_dataset_l[l_end_order][END_LAYER4_FINAL_ORDER] += 1

        num+=1
        if num % 100000 == 0:
            print(num, datetime.datetime.now())

    pd.DataFrame(layer1_dataset_s).to_csv('out/layer1_dataset_s.csv')
    pd.DataFrame(layer2_dataset_s).to_csv('out/layer2_dataset_s.csv')
    pd.DataFrame(layer3_dataset_s).to_csv('out/layer3_dataset_s.csv')
    pd.DataFrame(layer4_dataset_s).to_csv('out/layer4_dataset_s.csv')
    pd.DataFrame(layer1_dataset_l).to_csv('out/layer1_dataset_l.csv')
    pd.DataFrame(layer2_dataset_l).to_csv('out/layer2_dataset_l.csv')
    pd.DataFrame(layer3_dataset_l).to_csv('out/layer3_dataset_l.csv')
    pd.DataFrame(layer4_dataset_l).to_csv('out/layer4_dataset_l.csv')

    pd.DataFrame(layer1_dataset_s).to_csv('out_weighted/layer1_dataset_s.csv')
    pd.DataFrame(layer2_dataset_s).to_csv('out_weighted/layer2_dataset_s.csv')
    pd.DataFrame(layer3_dataset_s).to_csv('out_weighted/layer3_dataset_s.csv')
    pd.DataFrame(layer4_dataset_s).to_csv('out_weighted/layer4_dataset_s.csv')
    pd.DataFrame(layer1_dataset_l).to_csv('out_weighted/layer1_dataset_l.csv')
    pd.DataFrame(layer2_dataset_l).to_csv('out_weighted/layer2_dataset_l.csv')
    pd.DataFrame(layer3_dataset_l).to_csv('out_weighted/layer3_dataset_l.csv')
    pd.DataFrame(layer4_dataset_l).to_csv('out_weighted/layer4_dataset_l.csv')