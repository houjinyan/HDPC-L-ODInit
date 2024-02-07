import numpy as np
from pymongo import MongoClient
import time


layer1_clusters_num = 12
layer2_clusters_num = 72
layer3_clusters_num = 288
layer4_clusters_num = 1145
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

    client = MongoClient("mongodb://localhost:27017/")
    db = client['交通类大数据']
    collection = db['shenzhen_final']

    dayset=np.zeros(365,dtype=int)
    num = 0
    for x in collection.find():
        if (num % 1000000 == 0):
            end = time.perf_counter()
            print(num)
            print('Running time: %s Seconds' % (end - start))

        date_start = x['START_TIME'].replace('-', '')
        month_start = int(date_start[4:6])
        day_start = int(date_start[6:8])

        months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)  # 每月天数数组
        days = 0
        days = months[month_start - 1] + day_start
        dayset[days]+=1
        num+=1

    with open('../after-cluster-process/days.csv', 'w') as fin:
        for i in range(0,364):
            fin.write(str(dayset[i]))
            fin.write('\n')
        fin.write(str(dayset[364]))

    print(dayset)

