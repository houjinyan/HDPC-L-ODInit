import pandas as pd
import numpy as np
import datetime
from math import floor
from pymongo import MongoClient

LNG_MIN=113.763
LNG_MAX=114.19
LAT_MIN=22.4725
LAT_MAX=22.826
#step=1200
# LNG_range_meter=41223.05320706877#单位米
# LAT_range_meter=38362.30250835731#单位米
# LNG_range=np.append(np.arange(LNG_MIN,LNG_MAX,(LNG_MAX-LNG_MIN)/step),LNG_MAX)
# LAT_range=np.append(np.arange(LAT_MIN,LAT_MAX,(LAT_MAX-LAT_MIN)/step),LAT_MAX)

if __name__== "__main__":
    steps=[50,200,600,1200]
    client = MongoClient("mongodb://localhost:27017/")
    db = client['交通类大数据']
    collection = db['shenzhen42']
    for step in steps:
        num=0
        dens = np.zeros((int(step+1), int(step+1)),dtype=int)
        LNG_positions=np.zeros((int(step+1),int(step+1)),dtype = float)
        LAT_positions=np.zeros((int(step+1),int(step+1)),dtype = float)
        for x in collection.find():
            num+=1
            if num % 1000000 == 0:
                print(num, datetime.datetime.now())
            lat_s = float(x['START_LAT'])
            lng_s = float(x['START_LNG'])
            cur_x_s = floor(step * ((lng_s - LNG_MIN) / (LNG_MAX - LNG_MIN)))
            cur_y_s = floor(step * ((lat_s - LAT_MIN) / (LAT_MAX - LAT_MIN)))
            lat_e = float(x['END_LAT'])
            lng_e = float(x['END_LNG'])
            cur_x_e = floor(step * ((lng_e - LNG_MIN) / (LNG_MAX - LNG_MIN)))
            cur_y_e = floor(step * ((lat_e - LAT_MIN) / (LAT_MAX - LAT_MIN)))
            if cur_x_s < 0 or cur_y_s < 0:
                print(cur_x_s, cur_y_s)
            if cur_x_e < 0 or cur_y_e < 0:
                print(cur_x_e, cur_y_e)
            dens[cur_x_s, cur_y_s] = dens[cur_x_s, cur_y_s] + 1
            LNG_positions[cur_x_s, cur_y_s] = (LNG_positions[cur_x_s, cur_y_s] * (dens[cur_x_s, cur_y_s] - 1) + lng_s) / dens[cur_x_s, cur_y_s]
            LAT_positions[cur_x_s, cur_y_s] = (LAT_positions[cur_x_s, cur_y_s] * (dens[cur_x_s, cur_y_s] - 1) + lat_s) / dens[cur_x_s, cur_y_s]

            dens[cur_x_e, cur_y_e] = dens[cur_x_e, cur_y_e] + 1
            LNG_positions[cur_x_e, cur_y_e] = (LNG_positions[cur_x_e, cur_y_e] * (dens[cur_x_e, cur_y_e] - 1) + lng_e) / dens[cur_x_e, cur_y_e]
            LAT_positions[cur_x_e, cur_y_e] = (LAT_positions[cur_x_e, cur_y_e] * (dens[cur_x_e, cur_y_e] - 1) + lat_e) / dens[cur_x_e, cur_y_e]

        # 输出密度到csv文件
        with open("../dens_shenzhen/dens_shenzhen_test_"+str(step)+".csv","w") as fin:
            fin.write("lng,lat,dens,row,col\n")
            for kk in range(int(step+1)):
                for jj in range(int(step+1)):
                    if dens[kk,jj]>0:
                        #lng_left,lng_right,lat_left,lat_right=get_latlng_range(LNG_positions[kk,jj],LAT_positions[kk,jj])
                        fin.write(str(LNG_positions[kk,jj]))
                        fin.write(",")
                        fin.write(str(LAT_positions[kk,jj]))
                        fin.write(",")
                        fin.write(str(dens[kk,jj]))
                        fin.write(",")
                        fin.write(str(kk))
                        fin.write(",")
                        fin.write(str(jj))
                        fin.write("\n")