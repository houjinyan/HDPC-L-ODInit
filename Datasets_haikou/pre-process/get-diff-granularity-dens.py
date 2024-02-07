import pandas as pd
import numpy as np
import datetime
from math import floor
from pymongo import MongoClient

LNG_MIN=110.11
LNG_MAX=110.59
LAT_MIN=19.74
LAT_MAX=20.09
#step=1200
# LNG_range_meter=41223.05320706877#单位米
# LAT_range_meter=38362.30250835731#单位米
# LNG_range=np.append(np.arange(LNG_MIN,LNG_MAX,(LNG_MAX-LNG_MIN)/step),LNG_MAX)
# LAT_range=np.append(np.arange(LAT_MIN,LAT_MAX,(LAT_MAX-LAT_MIN)/step),LAT_MAX)

def isin(lat_s,lng_s,lat_e,lng_e):
    if(lng_s>=LNG_MIN and lng_s<=LNG_MAX):
        if(lng_e>=LNG_MIN and lng_e<=LNG_MAX):
            if(lat_s>=LAT_MIN and lat_s<=LAT_MAX):
                if(lat_e>=LAT_MIN and lat_e<=LAT_MAX):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return False

if __name__== "__main__":
    steps=[50,200,600,1200]
    for step in steps:
        dens = np.zeros((int(step+1), int(step+1)),dtype=int)
        LNG_positions=np.zeros((int(step+1),int(step+1)),dtype = float)
        LAT_positions=np.zeros((int(step+1),int(step+1)),dtype = float)
        for i in range(8):
            print("haikou_", i)
            haikou = pd.DataFrame(pd.read_csv('../海口网约车/dwv_order_make_haikou_' + str(i + 1) + '.txt', sep='\t'))
            for j in range(haikou.shape[0]):
                lat_s = float(haikou['dwv_order_make_haikou_'+str(i+1)+'.starting_lat'][j])
                lng_s = float(haikou['dwv_order_make_haikou_'+str(i+1)+'.starting_lng'][j])
                lat_e = float(haikou['dwv_order_make_haikou_'+str(i+1)+'.dest_lat'][j])
                lng_e = float(haikou['dwv_order_make_haikou_'+str(i+1)+'.dest_lng'][j])

                if (isin(lat_s, lng_s, lat_e, lng_e)):
                    cur_x_s = floor(step * ((lng_s - LNG_MIN) / (LNG_MAX - LNG_MIN)))
                    cur_y_s = floor(step * ((lat_s - LAT_MIN) / (LAT_MAX - LAT_MIN)))
                    cur_x_e = floor(step * ((lng_e - LNG_MIN) / (LNG_MAX - LNG_MIN)))
                    cur_y_e = floor(step * ((lat_e - LAT_MIN) / (LAT_MAX - LAT_MIN)))
                    dens[cur_x_s, cur_y_s] = dens[cur_x_s, cur_y_s] + 1
                    LNG_positions[cur_x_s, cur_y_s] = (LNG_positions[cur_x_s, cur_y_s] * (dens[cur_x_s, cur_y_s] - 1) + lng_s) / dens[cur_x_s, cur_y_s]
                    LAT_positions[cur_x_s, cur_y_s] = (LAT_positions[cur_x_s, cur_y_s] * (dens[cur_x_s, cur_y_s] - 1) + lat_s) / dens[cur_x_s, cur_y_s]

                    dens[cur_x_e, cur_y_e] = dens[cur_x_e, cur_y_e] + 1
                    LNG_positions[cur_x_e, cur_y_e] = (LNG_positions[cur_x_e, cur_y_e] * (dens[cur_x_e, cur_y_e] - 1) + lng_e) / dens[cur_x_e, cur_y_e]
                    LAT_positions[cur_x_e, cur_y_e] = (LAT_positions[cur_x_e, cur_y_e] * (dens[cur_x_e, cur_y_e] - 1) + lat_e) / dens[cur_x_e, cur_y_e]

        # 输出密度到csv文件
        with open("../dens_haikou/dens_haikou_test_"+str(step)+".csv","w") as fin:
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