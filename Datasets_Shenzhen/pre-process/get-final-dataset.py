from pymongo import MongoClient
import time


if __name__ == "__main__":
    date_min = 517
    date_max = 627
    start = time.perf_counter()
    client = MongoClient("mongodb://localhost:27017/")
    db = client['交通类大数据']
    collection = db['shenzhen_final']
    collection_new=db['shenzhen42']

    num = 0
    for x in collection.find():
        num+=1
        if (num % 1000000 == 0):
            end = time.perf_counter()
            print(num)
            print('Running time: %s Seconds' % (end - start))

        # START PART
        date_start = x['START_TIME'].replace('-', '')
        month_start = date_start[4:6]
        day_start = date_start[6:8]
        month_day_start=int(month_start+day_start)
        # END PART
        date_end = x['END_TIME'].replace('-', '')
        month_end = date_end[4:6]
        day_end = date_end[6:8]
        month_day_end=int(month_end+day_end)

        if((month_day_start>=date_min) & (month_day_start<=date_max) & (month_day_end>=date_min) & (month_day_end<=date_max)):
            del x['_id']
            collection_new.insert_one(x)
