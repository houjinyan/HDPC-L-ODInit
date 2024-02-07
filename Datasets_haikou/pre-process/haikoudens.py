import pandas as pd
import numpy as np
from math import floor
import datetime

granularity=50
dens = np.zeros([granularity+1,granularity+1])

LAT_MIN=19.74
LNG_MIN=110.11
LAT_MAX=20.09
LNG_MAX=110.59

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

if __name__ == "__main__":
    error=0
    for i in range(8):
        print("haikou_",i)
        haikou = pd.DataFrame(pd.read_csv('../海口网约车/dwv_order_make_haikou_'+str(i+1)+'.txt', sep='\t'))
        for j in range(haikou.shape[0]):
            lat_s = float(haikou['dwv_order_make_haikou_'+str(i+1)+'.starting_lat'][j])
            lng_s = float(haikou['dwv_order_make_haikou_'+str(i+1)+'.starting_lng'][j])
            lat_e = float(haikou['dwv_order_make_haikou_'+str(i+1)+'.dest_lat'][j])
            lng_e = float(haikou['dwv_order_make_haikou_'+str(i+1)+'.dest_lng'][j])
            if (isin(lat_s, lng_s, lat_e, lng_e)):
                cur_x_s = floor(((lng_s - LNG_MIN)/(LNG_MAX-LNG_MIN)) * granularity)
                cur_y_s = floor(((lat_s - LAT_MIN)/(LAT_MAX-LAT_MIN)) * granularity)
                cur_x_e = floor(((lng_e - LNG_MIN)/(LNG_MAX-LNG_MIN)) * granularity)
                cur_y_e = floor(((lat_e - LAT_MIN)/(LAT_MAX-LAT_MIN)) * granularity)

                if cur_x_s < 0 or cur_y_s < 0 or cur_x_e < 0 or cur_y_e < 0:
                    error+=1
                else:
                    dens[cur_x_s, cur_y_s] = dens[cur_x_s, cur_y_s] + 1
                    dens[cur_x_e, cur_y_e] = dens[cur_x_e, cur_y_e] + 1
    print("error_nums: ",error)
    with open("dens_haikou_"+str(granularity)+".csv","w") as fin:
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
