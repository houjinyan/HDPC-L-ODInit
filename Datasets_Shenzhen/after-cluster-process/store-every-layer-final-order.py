import pandas as pd
import numpy as np
from pymongo import MongoClient
from math import floor
import time
import datetime

loop_start=0
#loop_end=55000000

# layer1_clusters_num = 12
# layer2_clusters_num = 72
# layer3_clusters_num = 284
# layer4_clusters_num = 1120
LNG_MIN = 113.763
LNG_MAX = 114.19
LAT_MIN = 22.4725
LAT_MAX = 22.826
layer1_step = 50
layer2_step = 200
layer3_step = 600
layer4_step = 1200

if __name__ == "__main__":
    start = time.perf_counter()

    # adj_layer1 = np.zeros((layer1_clusters_num, layer1_clusters_num), dtype=int)
    # adj_layer2 = np.zeros((layer2_clusters_num, layer2_clusters_num), dtype=int)
    # adj_layer3 = np.zeros((layer3_clusters_num, layer3_clusters_num), dtype=int)
    # adj_layer4 = np.zeros((layer4_clusters_num, layer4_clusters_num), dtype=int)

    # layer1_cluster_datas_final = pd.read_csv('layer1_clusters_final.csv')
    # layer2_cluster_datas_final = pd.read_csv('layer2_clusters_final.csv')
    # layer3_cluster_datas_final = pd.read_csv('layer3_clusters_final.csv')
    layer4_cluster_datas_final = pd.read_csv('layer4_clusters_final.csv')

    client = MongoClient("mongodb://localhost:27017/")
    db = client['交通类大数据']
    collection = db['shenzhen42']
    collection_new=db['shenzhen42_complete_exSea']
    num = 0
    for x in collection.find():
        if (num % 100000 == 0):
            end = time.perf_counter()
            print(num)
            print('Running time: %s Seconds' % (end - start))
        if(num>=loop_start):
            try:
                del x['_id']

                # # Layer1 Row and Col
                # start_layer1_row = floor(layer1_step * ((float(x['START_LNG']) - LNG_MIN) / (LNG_MAX - LNG_MIN)))
                # start_layer1_col = floor(layer1_step * ((float(x['START_LAT']) - LAT_MIN) / (LAT_MAX - LAT_MIN)))
                # end_layer1_row = floor(layer1_step * ((float(x['END_LNG']) - LNG_MIN) / (LNG_MAX - LNG_MIN)))
                # end_layer1_col = floor(layer1_step * ((float(x['END_LAT']) - LAT_MIN) / (LAT_MAX - LAT_MIN)))
                #
                # # Layer2 Row and Col
                # start_layer2_row = floor(layer2_step * ((float(x['START_LNG']) - LNG_MIN) / (LNG_MAX - LNG_MIN)))
                # start_layer2_col = floor(layer2_step * ((float(x['START_LAT']) - LAT_MIN) / (LAT_MAX - LAT_MIN)))
                # end_layer2_row = floor(layer2_step * ((float(x['END_LNG']) - LNG_MIN) / (LNG_MAX - LNG_MIN)))
                # end_layer2_col = floor(layer2_step * ((float(x['END_LAT']) - LAT_MIN) / (LAT_MAX - LAT_MIN)))
                #
                # # Layer3 Row and Col
                # start_layer3_row = floor(layer3_step * ((float(x['START_LNG']) - LNG_MIN) / (LNG_MAX - LNG_MIN)))
                # start_layer3_col = floor(layer3_step * ((float(x['START_LAT']) - LAT_MIN) / (LAT_MAX - LAT_MIN)))
                # end_layer3_row = floor(layer3_step * ((float(x['END_LNG']) - LNG_MIN) / (LNG_MAX - LNG_MIN)))
                # end_layer3_col = floor(layer3_step * ((float(x['END_LAT']) - LAT_MIN) / (LAT_MAX - LAT_MIN)))

                # Layer4 Row and Col
                start_layer4_row = floor(layer4_step * ((float(x['START_LNG']) - LNG_MIN) / (LNG_MAX - LNG_MIN)))
                start_layer4_col = floor(layer4_step * ((float(x['START_LAT']) - LAT_MIN) / (LAT_MAX - LAT_MIN)))
                end_layer4_row = floor(layer4_step * ((float(x['END_LNG']) - LNG_MIN) / (LNG_MAX - LNG_MIN)))
                end_layer4_col = floor(layer4_step * ((float(x['END_LAT']) - LAT_MIN) / (LAT_MAX - LAT_MIN)))

                #START PART
                # layer1_start_temp=layer1_cluster_datas_final[(layer1_cluster_datas_final['row'] == start_layer1_row) & (layer1_cluster_datas_final['col'] == start_layer1_col)]
                # start_layer1_order = layer1_start_temp['layer1-cluster'].tolist()[0]
                # start_layer1_final_order=layer1_start_temp['layer1-final-order'].tolist()[0]
                #
                # layer2_start_temp=layer2_cluster_datas_final[(layer2_cluster_datas_final['row'] == start_layer2_row) & (layer2_cluster_datas_final['col'] == start_layer2_col)]
                # start_layer2_order = layer2_start_temp['layer2-cluster'].tolist()[0]
                # start_layer2_final_order=layer2_start_temp['layer2-final-order'].tolist()[0]
                #
                # layer3_start_temp=layer3_cluster_datas_final[(layer3_cluster_datas_final['row'] == start_layer3_row) & (layer3_cluster_datas_final['col'] == start_layer3_col)]
                # start_layer3_order = layer3_start_temp['layer3-cluster'].tolist()[0]
                # start_layer3_final_order=layer3_start_temp['layer3-final-order'].tolist()[0]

                layer4_start_temp=layer4_cluster_datas_final[(layer4_cluster_datas_final['row'] == start_layer4_row) & (layer4_cluster_datas_final['col'] == start_layer4_col)]
                start_layer4_order = layer4_start_temp['layer4-cluster'].tolist()[0]
                start_layer4_final_order=layer4_start_temp['layer4-final-order'].tolist()[0]

                #END PART
                # layer1_end_temp=layer1_cluster_datas_final[(layer1_cluster_datas_final['row'] == end_layer1_row) & (layer1_cluster_datas_final['col'] == end_layer1_col)]
                # end_layer1_order = layer1_end_temp['layer1-cluster'].tolist()[0]
                # end_layer1_final_order=layer1_end_temp['layer1-final-order'].tolist()[0]
                #
                # layer2_end_temp=layer2_cluster_datas_final[(layer2_cluster_datas_final['row'] == end_layer2_row) & (layer2_cluster_datas_final['col'] == end_layer2_col)]
                # end_layer2_order = layer2_end_temp['layer2-cluster'].tolist()[0]
                # end_layer2_final_order=layer2_end_temp['layer2-final-order'].tolist()[0]
                #
                # layer3_end_temp=layer3_cluster_datas_final[(layer3_cluster_datas_final['row'] == end_layer3_row) & (layer3_cluster_datas_final['col'] == end_layer3_col)]
                # end_layer3_order = layer3_end_temp['layer3-cluster'].tolist()[0]
                # end_layer3_final_order=layer3_end_temp['layer3-final-order'].tolist()[0]

                layer4_end_temp=layer4_cluster_datas_final[(layer4_cluster_datas_final['row'] == end_layer4_row) & (layer4_cluster_datas_final['col'] == end_layer4_col)]
                end_layer4_order = layer4_end_temp['layer4-cluster'].tolist()[0]
                end_layer4_final_order=layer4_end_temp['layer4-final-order'].tolist()[0]

                # x['START_LAYER1_ORDER']=str(start_layer1_order)
                # x['START_LAYER1_FINAL_ORDER'] = str(start_layer1_final_order)
                # x['START_LAYER2_ORDER'] = str(start_layer2_order)
                # x['START_LAYER2_FINAL_ORDER'] = str(start_layer2_final_order)
                # x['START_LAYER3_ORDER'] = str(start_layer3_order)
                # x['START_LAYER3_FINAL_ORDER'] = str(start_layer3_final_order)
                x['START_LAYER4_ORDER'] = str(start_layer4_order)
                x['START_LAYER4_FINAL_ORDER'] = str(start_layer4_final_order)
                # x['END_LAYER1_ORDER']=str(end_layer1_order)
                # x['END_LAYER1_FINAL_ORDER'] = str(end_layer1_final_order)
                # x['END_LAYER2_ORDER'] = str(end_layer2_order)
                # x['END_LAYER2_FINAL_ORDER'] = str(end_layer2_final_order)
                # x['END_LAYER3_ORDER'] = str(end_layer3_order)
                # x['END_LAYER3_FINAL_ORDER'] = str(end_layer3_final_order)
                x['END_LAYER4_ORDER'] = str(end_layer4_order)
                x['END_LAYER4_FINAL_ORDER'] = str(end_layer4_final_order)

                #START PART
                date_start = x['START_TIME'].replace('-', '')
                year_start = int(date_start[0:4])
                month_start = int(date_start[4:6])
                day_start = int(date_start[6:8])
                hour_start = int(date_start[9:11])
                minute_start = int(date_start[12:14])
                s_slot_order_start = ((hour_start * 60 + minute_start) % 180 // 15) + 1
                m_slot_order_start = (hour_start // 3) + 1
                l_slot_order_start = datetime.date(year_start, month_start, day_start).isoweekday()
                x['START_S_SLOT_ORDER']=str(s_slot_order_start)
                x['START_M_SLOT_ORDER']=str(m_slot_order_start)
                x['START_L_SLOT_ORDER']=str(l_slot_order_start)

                # END PART
                date_end = x['END_TIME'].replace('-', '')
                # print(date)
                year_end = int(date_end[0:4])
                month_end = int(date_end[4:6])
                day_end = int(date_end[6:8])
                hour_end = int(date_end[9:11])
                minute_end = int(date_end[12:14])
                s_slot_order_end = ((hour_end * 60 + minute_end) % 180 // 15) + 1
                m_slot_order_end = (hour_end // 3) + 1
                l_slot_order_end = datetime.date(year_end, month_end, day_end).isoweekday()
                x['END_S_SLOT_ORDER']=str(s_slot_order_end)
                x['END_M_SLOT_ORDER']=str(m_slot_order_end)
                x['END_L_SLOT_ORDER']=str(l_slot_order_end)

                months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)  # 每月天数数组
                days_start = 0
                days_start = months[month_start - 1] + day_start
                x['DAY_START']=str(days_start)

                days_end = 0
                days_end = months[month_end - 1] + day_end
                x['DAY_END']=str(days_end)
                collection_new.insert_one(x)
            except:
                continue
        num += 1