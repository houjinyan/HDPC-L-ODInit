import pandas as pd
import numpy as np
from pymongo import MongoClient
import datetime

layer1_clusters_num = 12
layer2_clusters_num = 72
layer3_clusters_num = 284
layer4_clusters_num = 1120
days_num=42
s_num=96
m_num=8
l_num=1

def GetRowOrder(s,m,day):
    s_order=day*s_num+(m-1)*12+s-1
    m_order=day*m_num+m-1
    l_order=day*l_num
    return s_order,m_order,l_order

if __name__== "__main__":
    layer1_dataset_s = np.zeros((days_num * s_num,layer1_clusters_num),dtype=int)
    layer1_dataset_m = np.zeros((days_num * m_num,layer1_clusters_num), dtype=int)
    layer1_dataset_l = np.zeros((days_num * l_num,layer1_clusters_num), dtype=int)

    layer2_dataset_s = np.zeros((days_num * s_num,layer2_clusters_num),dtype=int)
    layer2_dataset_m = np.zeros((days_num * m_num,layer2_clusters_num), dtype=int)
    layer2_dataset_l = np.zeros((days_num * l_num,layer2_clusters_num), dtype=int)

    layer3_dataset_s = np.zeros((days_num * s_num,layer3_clusters_num),dtype=int)
    layer3_dataset_m = np.zeros((days_num * m_num,layer3_clusters_num), dtype=int)
    layer3_dataset_l = np.zeros((days_num * l_num,layer3_clusters_num), dtype=int)

    layer4_dataset_s = np.zeros((days_num * s_num,layer4_clusters_num),dtype=int)
    layer4_dataset_m = np.zeros((days_num * m_num,layer4_clusters_num), dtype=int)
    layer4_dataset_l = np.zeros((days_num * l_num,layer4_clusters_num), dtype=int)

    client = MongoClient("mongodb://localhost:27017/")
    db = client['交通类大数据']
    collection = db['shenzhen42_complete']
    num=0
    for x in collection.find():
        # day_start=int(x['DAY_START'])-137
        # START_S_SLOT_ORDER=int(x['START_S_SLOT_ORDER'])
        # START_M_SLOT_ORDER = int(x['START_M_SLOT_ORDER'])
        # START_L_SLOT_ORDER = int(x['START_L_SLOT_ORDER'])
        day_end=int(x['DAY_END'])-137
        END_S_SLOT_ORDER=int(x['END_S_SLOT_ORDER'])
        END_M_SLOT_ORDER = int(x['END_M_SLOT_ORDER'])
        END_L_SLOT_ORDER = int(x['END_L_SLOT_ORDER'])

        # START_LAYER1_FINAL_ORDER = int(x['START_LAYER1_FINAL_ORDER'])
        # START_LAYER2_FINAL_ORDER = int(x['START_LAYER2_FINAL_ORDER'])
        # START_LAYER3_FINAL_ORDER = int(x['START_LAYER3_FINAL_ORDER'])
        # START_LAYER4_FINAL_ORDER = int(x['START_LAYER4_FINAL_ORDER'])
        END_LAYER1_FINAL_ORDER = int(x['END_LAYER1_FINAL_ORDER'])
        END_LAYER2_FINAL_ORDER = int(x['END_LAYER2_FINAL_ORDER'])
        END_LAYER3_FINAL_ORDER = int(x['END_LAYER3_FINAL_ORDER'])
        END_LAYER4_FINAL_ORDER = int(x['END_LAYER4_FINAL_ORDER'])

        #s_start_order,m_start_order,l_start_order=GetRowOrder(START_S_SLOT_ORDER,START_M_SLOT_ORDER,day_start)
        s_end_order,m_end_order,l_end_order = GetRowOrder(END_S_SLOT_ORDER, END_M_SLOT_ORDER,day_end)

        # layer1_dataset_s[s_start_order][START_LAYER1_FINAL_ORDER] += 1
        # layer2_dataset_s[s_start_order][START_LAYER2_FINAL_ORDER] += 1
        # layer3_dataset_s[s_start_order][START_LAYER3_FINAL_ORDER] += 1
        # layer4_dataset_s[s_start_order][START_LAYER4_FINAL_ORDER] += 1
        #
        # layer1_dataset_m[m_start_order][START_LAYER1_FINAL_ORDER] += 1
        # layer2_dataset_m[m_start_order][START_LAYER2_FINAL_ORDER] += 1
        # layer3_dataset_m[m_start_order][START_LAYER3_FINAL_ORDER] += 1
        # layer4_dataset_m[m_start_order][START_LAYER4_FINAL_ORDER] += 1
        #
        # layer1_dataset_l[l_start_order][START_LAYER1_FINAL_ORDER] += 1
        # layer2_dataset_l[l_start_order][START_LAYER2_FINAL_ORDER] += 1
        # layer3_dataset_l[l_start_order][START_LAYER3_FINAL_ORDER] += 1
        # layer4_dataset_l[l_start_order][START_LAYER4_FINAL_ORDER] += 1

        layer1_dataset_s[s_end_order][END_LAYER1_FINAL_ORDER] += 1
        layer2_dataset_s[s_end_order][END_LAYER2_FINAL_ORDER] += 1
        layer3_dataset_s[s_end_order][END_LAYER3_FINAL_ORDER] += 1
        layer4_dataset_s[s_end_order][END_LAYER4_FINAL_ORDER] += 1

        layer1_dataset_m[m_end_order][END_LAYER1_FINAL_ORDER] += 1
        layer2_dataset_m[m_end_order][END_LAYER2_FINAL_ORDER] += 1
        layer3_dataset_m[m_end_order][END_LAYER3_FINAL_ORDER] += 1
        layer4_dataset_m[m_end_order][END_LAYER4_FINAL_ORDER] += 1

        layer1_dataset_l[l_end_order][END_LAYER1_FINAL_ORDER] += 1
        layer2_dataset_l[l_end_order][END_LAYER2_FINAL_ORDER] += 1
        layer3_dataset_l[l_end_order][END_LAYER3_FINAL_ORDER] += 1
        layer4_dataset_l[l_end_order][END_LAYER4_FINAL_ORDER] += 1

        num+=1
        if num % 1000000 == 0:
            print(num, datetime.datetime.now())

    pd.DataFrame(layer1_dataset_s).to_csv('in/layer1_dataset_s.csv')
    pd.DataFrame(layer2_dataset_s).to_csv('in/layer2_dataset_s.csv')
    pd.DataFrame(layer3_dataset_s).to_csv('in/layer3_dataset_s.csv')
    pd.DataFrame(layer4_dataset_s).to_csv('in/layer4_dataset_s.csv')
    pd.DataFrame(layer1_dataset_m).to_csv('in/layer1_dataset_m.csv')
    pd.DataFrame(layer2_dataset_m).to_csv('in/layer2_dataset_m.csv')
    pd.DataFrame(layer3_dataset_m).to_csv('in/layer3_dataset_m.csv')
    pd.DataFrame(layer4_dataset_m).to_csv('in/layer4_dataset_m.csv')
    pd.DataFrame(layer1_dataset_l).to_csv('in/layer1_dataset_l.csv')
    pd.DataFrame(layer2_dataset_l).to_csv('in/layer2_dataset_l.csv')
    pd.DataFrame(layer3_dataset_l).to_csv('in/layer3_dataset_l.csv')
    pd.DataFrame(layer4_dataset_l).to_csv('in/layer4_dataset_l.csv')

    pd.DataFrame(layer1_dataset_s).to_csv('in_weighted/layer1_dataset_s.csv')
    pd.DataFrame(layer2_dataset_s).to_csv('in_weighted/layer2_dataset_s.csv')
    pd.DataFrame(layer3_dataset_s).to_csv('in_weighted/layer3_dataset_s.csv')
    pd.DataFrame(layer4_dataset_s).to_csv('in_weighted/layer4_dataset_s.csv')
    pd.DataFrame(layer1_dataset_m).to_csv('in_weighted/layer1_dataset_m.csv')
    pd.DataFrame(layer2_dataset_m).to_csv('in_weighted/layer2_dataset_m.csv')
    pd.DataFrame(layer3_dataset_m).to_csv('in_weighted/layer3_dataset_m.csv')
    pd.DataFrame(layer4_dataset_m).to_csv('in_weighted/layer4_dataset_m.csv')
    pd.DataFrame(layer1_dataset_l).to_csv('in_weighted/layer1_dataset_l.csv')
    pd.DataFrame(layer2_dataset_l).to_csv('in_weighted/layer2_dataset_l.csv')
    pd.DataFrame(layer3_dataset_l).to_csv('in_weighted/layer3_dataset_l.csv')
    pd.DataFrame(layer4_dataset_l).to_csv('in_weighted/layer4_dataset_l.csv')