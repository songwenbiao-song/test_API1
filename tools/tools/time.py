from tools.data import time_tool
import time
import datetime
def open():        #当前日期和时间减5分钟后转成时间戳
    p = time_tool.get_jian5fenzhong()
    timeArray = time.strptime(p, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp
def open1():
    p = time_tool.get_now()       #当前日期和时间转成时间戳
    timeArray = time.strptime(p, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp
def time_jiaqi():       #当前时间加一天
    time1=(datetime.datetime.now()+datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
    return time1


