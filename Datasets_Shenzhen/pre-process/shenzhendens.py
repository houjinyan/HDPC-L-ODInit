import pandas as pd
import numpy as np
from math import floor
from pymongo import MongoClient

row=0
client = MongoClient("mongodb://localhost:27017/")
db = client['交通类大数据']
collection=db['shenzhen42']


granularity=100
dens = np.zeros([granularity+1,granularity+1])

LAT_MIN=22.4725
LNG_MIN=113.763
LAT_MAX=22.826
LNG_MAX=114.19

def isin(lat_s,lng_s,lat_e,lng_e):
    if((lng_s>=LNG_MIN) and (lng_s<=LNG_MAX)):
        if((lng_e>=LNG_MIN) and (lng_e<=LNG_MAX)):
            if((lat_s>=LAT_MIN) and (lat_s<=LAT_MAX)):
                if((lat_e>=LAT_MIN) and (lat_e<=LAT_MAX)):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return False

for x in collection.find():
    row+=1
    if(row%100000==0):
        print(row)

    lat_s = float(x['START_LAT'])
    lng_s = float(x['START_LNG'])
    lat_e = float(x['END_LAT'])
    lng_e = float(x['END_LNG'])
    if (isin(lat_s, lng_s, lat_e, lng_e)):
        cur_x_s = floor(((lng_s - LNG_MIN) / (LNG_MAX - LNG_MIN)) * granularity)
        cur_y_s = floor(((lat_s - LAT_MIN) / (LAT_MAX - LAT_MIN)) * granularity)
        cur_x_e = floor(((lng_e - LNG_MIN) / (LNG_MAX - LNG_MIN)) * granularity)
        cur_y_e = floor(((lat_e - LAT_MIN) / (LAT_MAX - LAT_MIN)) * granularity)
        if cur_x_s < 0 or cur_y_s < 0:
            print(cur_x_s, cur_y_s)
        if cur_x_e < 0 or cur_y_e < 0:
            print(cur_x_e, cur_y_e)
        dens[cur_x_s, cur_y_s] = dens[cur_x_s, cur_y_s] + 1
        dens[cur_x_e, cur_y_e] = dens[cur_x_e, cur_y_e] + 1

with open("dens_shenzhen_"+str(granularity)+".csv","w") as fin:
    fin.write("lng,lat,dens\n")
    for kk in range(granularity+1):
        for jj in range(granularity+1):
            if dens[kk,jj]>0:
                fin.write(str((kk/granularity)*(LNG_MAX-LNG_MIN)+LNG_MIN))
                fin.write(",")
                fin.write(str((jj/granularity)*(LAT_MAX-LAT_MIN)+LAT_MIN))
                fin.write(",")
                fin.write(str(dens[kk,jj]))
                fin.write("\n")
