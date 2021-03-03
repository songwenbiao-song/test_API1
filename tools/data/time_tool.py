# -*- coding: utf-8 -*- 
# Project: guoya-tools-test
# Creator: LudvikWoo
# Create time: 2019-09-20 16:52
import datetime

def get_now():                  #封装的当前日期和时间
    date_time=str(datetime.datetime.now())[0:19]
    #print(date_time)
    return date_time

def get_today():                # 封装的当天日期
    date=str(datetime.datetime.now())[0:10]
    #print(date)
    return date

def get_time():                  # 封装的当前时间
    time = str(datetime.datetime.now())[11:19]

    #print(time)
    return time
def get_jian5fenzhong():         # 封装的当前时间减5分钟
    date_time=str(datetime.datetime.now()+datetime.timedelta(minutes=-5))[0:19]
   #print(date_time)
    return date_time


if __name__ == '__main__':
    get_now()
    get_today()
    get_time()
    get_jian5fenzhong()