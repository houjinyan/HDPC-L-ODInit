import pandas as pd

if __name__== "__main__":
    data_time=pd.read_csv('../trainset/shenzhen_trainset_final.csv',usecols=['USER_ID','START_TIME','END_TIME'])
    datas_trainset=pd.read_csv('../after-cluster-process/trainset/final_cluster_order_trainset.csv')
    loop_end=datas_trainset.shape[0]

    with open('../after-cluster-process/trainset/final_data_sml_clusterorder_time_trainset.csv','w') as fin:
        fin.write('NUM,USER_ID,COM_ID,'
                  'START_S_SLOT_ORDER,START_M_SLOT_ORDER,START_L_SLOT_ORDER,'
                  'START_LNG,START_LAT,'
                  'START_ROW,START_COL,'
                  'END_S_SLOT_ORDER,END_M_SLOT_ORDER,END_L_SLOT_ORDER,'
                  'END_LNG,END_LAT,'
                  'END_ROW,END_COL,'
                  'START_LAYER1_ORDER,END_LAYER1_ORDER,'
                  'START_LAYER2_ORDER,END_LAYER2_ORDER,'
                  'START_LAYER3_ORDER,END_LAYER3_ORDER,'
                  'START_LAYER4_ORDER,END_LAYER4_ORDER,'
                  'START_TIME,END_TIME\n')
    for i in range(0,loop_end):
        if(i%100000==0):
            print(i)
        with open('../after-cluster-process/trainset/final_data_sml_clusterorder_time_trainset.csv', 'a') as fin:
            fin.write(str(i))
            fin.write(',')
            fin.write(str(datas_trainset['USER_ID'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['COM_ID'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['START_S_SLOT_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['START_M_SLOT_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['START_L_SLOT_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['START_LNG'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['START_LAT'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['START_ROW'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['START_COL'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['END_S_SLOT_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['END_M_SLOT_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['END_L_SLOT_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['END_LNG'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['END_LAT'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['END_ROW'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['END_COL'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['START_LAYER1_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['END_LAYER1_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['START_LAYER2_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['END_LAYER2_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['START_LAYER3_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['END_LAYER3_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['START_LAYER4_ORDER'][i]))
            fin.write(',')
            fin.write(str(datas_trainset['END_LAYER4_ORDER'][i]))
            fin.write(',')
            start_time=data_time['START_TIME'][i].replace('-','')
            fin.write(str(start_time[0:4]+start_time[4:6]+start_time[6:8]+start_time[9:11]+start_time[12:14]))
            fin.write(',')
            end_time = data_time['END_TIME'][i].replace('-','')
            fin.write(str(end_time[0:4]+end_time[4:6]+end_time[6:8]+end_time[9:11]+end_time[12:14]))
            fin.write('\n')