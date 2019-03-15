import time
import datetime


def now_time():
    '''当前北京时间'''
    time_now = int(time.time())
    time_local = time.localtime(time_now)
    integral_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return integral_time

def semih_time():
    '''当前北京时间 + 30分钟'''
    whole_time = (datetime.datetime.now() + datetime.timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
    return whole_time

def whole_time():
    '''当前整点时间'''
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H")+":00:00"
    return now_time

def whole_semih_time():
    '''当前整点时间 + 60分钟'''
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H") + ":00:00"
    today_start_time = int(time.mktime(time.strptime(str(now_time), '%Y-%m-%d %H:%M:%S'))) + 3600
    time_local = time.localtime(today_start_time)
    now_semih_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return now_semih_time

def whole_semih_times():
    '''当前整点时间 + 90分钟'''
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H") + ":00:00"
    today_start_time = int(time.mktime(time.strptime(str(now_time), '%Y-%m-%d %H:%M:%S'))) + 5400
    time_local = time.localtime(today_start_time)
    now_semih_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return now_semih_time

if __name__ == '__main__':
    print(now_time())
    print(semih_time())
    print(whole_time())
    print(whole_semih_time())
    print(whole_semih_times())
