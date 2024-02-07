import pandas as pd
import datetime
from math import floor

LNG_MIN=113.78
LNG_MAX=114.1812
LAT_MIN=22.475
LAT_MAX=22.82
step=1600

if __name__== "__main__":
    testset_datas=pd.read_csv('../testset/shenzhen_testset_final.csv')
    datas_num=testset_datas.shape[0]

    with open('../after-cluster-process/testset/sml_time_testset_datas.csv','w') as fin:
        fin.write('USER_ID,COM_ID,'
                  'START_S_SLOT_ORDER,START_M_SLOT_ORDER,START_L_SLOT_ORDER,'
                  'START_LNG,START_LAT,'
                  'START_ROW,START_COL,'
                  'END_S_SLOT_ORDER,END_M_SLOT_ORDER,END_L_SLOT_ORDER,'
                  'END_LNG,END_LAT,'
                  'END_ROW,END_COL\n')

    for i in range(datas_num):
        if(i%100001==0):
            print(i)
        date_start=testset_datas['START_TIME'][i].replace('-','')
        #print(date)
        year_start=int(date_start[0:4])
        month_start=int(date_start[4:6])
        day_start=int(date_start[6:8])
        hour_start=int(date_start[9:11])
        minute_start=int(date_start[12:14])
        s_slot_order_start=((hour_start*60+minute_start)%180//15)+1
        m_slot_order_start=(hour_start//3)+1
        l_slot_order_start=datetime.date(year_start,month_start,day_start).isoweekday()
        row_start=floor(step*(float(testset_datas['START_LNG'][i])-LNG_MIN)/(LNG_MAX-LNG_MIN))
        col_start=floor(step*(float(testset_datas['START_LAT'][i])-LAT_MIN)/(LAT_MAX-LAT_MIN))

        #END PART
        date_end=testset_datas['END_TIME'][i].replace('-','')
        #print(date)
        year_end=int(date_end[0:4])
        month_end=int(date_end[4:6])
        day_end=int(date_end[6:8])
        hour_end=int(date_end[9:11])
        minute_end=int(date_end[12:14])
        s_slot_order_end=((hour_end*60+minute_end)%180//15)+1
        m_slot_order_end=(hour_end//3)+1
        l_slot_order_end=datetime.date(year_end,month_end,day_end).isoweekday()
        row_end=floor(step*(float(testset_datas['END_LNG'][i])-LNG_MIN)/(LNG_MAX-LNG_MIN))
        col_end=floor(step*(float(testset_datas['END_LAT'][i])-LAT_MIN)/(LAT_MAX-LAT_MIN))

        with open('../after-cluster-process/testset/sml_time_testset_datas.csv','a') as fin:
            fin.write(str(testset_datas['USER_ID'][i]))
            fin.write(',')
            fin.write(str(testset_datas['COM_ID'][i]))
            fin.write(',')
            fin.write(str(s_slot_order_start))
            fin.write(',')
            fin.write(str(m_slot_order_start))
            fin.write(',')
            fin.write(str(l_slot_order_start))
            fin.write(',')
            fin.write(str(testset_datas['START_LNG'][i]))
            fin.write(',')
            fin.write(str(testset_datas['START_LAT'][i]))
            fin.write(',')
            fin.write(str(row_start))
            fin.write(',')
            fin.write(str(col_start))
            fin.write(',')
            fin.write(str(s_slot_order_end))
            fin.write(',')
            fin.write(str(m_slot_order_end))
            fin.write(',')
            fin.write(str(l_slot_order_end))
            fin.write(',')
            fin.write(str(testset_datas['END_LNG'][i]))
            fin.write(',')
            fin.write(str(testset_datas['END_LAT'][i]))
            fin.write(',')
            fin.write(str(row_end))
            fin.write(',')
            fin.write(str(col_end))
            fin.write('\n')