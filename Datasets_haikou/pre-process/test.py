import pandas as pd
import numpy as np

if __name__ == "__main__":
    haikou_1=pd.DataFrame(pd.read_csv('../海口网约车/dwv_order_make_haikou_1.txt', sep='\t'))
    print(haikou_1['dwv_order_make_haikou_1.arrive_time'])