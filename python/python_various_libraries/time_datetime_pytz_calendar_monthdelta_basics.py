import datetime

print(datetime.date.today())  # 2020-05-25

dt = datetime.datetime.now()  # 2020-05-25 18:43:46.373069
print(datetime.datetime.utcnow())  # 2020-05-25 13:13:46.373069

s = dt.strftime("%Y-%m-%d %H:%M:%S")
print(type(s))  # <class 'str'>
print(s)  # 2020-05-25 18:44:52

dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(type(dt))  # <class 'datetime.datetime'>
print(dt)  # 2020-05-25 13:05:32

# refer epochconverter.com
timestamp = 1590411740
print(datetime.datetime.fromtimestamp(timestamp))  # 2020-05-25 18:32:20
print(datetime.datetime.utcfromtimestamp(timestamp))  # 2020-05-25 13:02:20

print(dt + datetime.timedelta(days=1))  # 2020-05-26 18:32:20

##########################################

import time

print(time.time())  # 1590412567.5555265

time.sleep(2)

# refer epochconverter.com
print(time.gmtime(timestamp))
# time.struct_time(tm_year=2020, tm_mon=5, tm_mday=25, tm_hour=13, tm_min=2, tm_sec=20, tm_wday=0, tm_yday=146, tm_isdst=0)

##########################################

import pytz
from pytz import timezone

utc_time_tuple = datetime.datetime(2020, 5, 25, 13, 2, 20, tzinfo=pytz.utc).utctimetuple()
print(utc_time_tuple)
# time.struct_time(tm_year=2020, tm_mon=5, tm_mday=25, tm_hour=13, tm_min=2, tm_sec=20, tm_wday=0, tm_yday=146, tm_isdst=0)

print(datetime.datetime.now(timezone('US/Eastern')))  # 2020-05-25 12:18:33.204196-04:00

###########################################

import calendar

print(calendar.timegm(utc_time_tuple))  # 1590411740

###########################################

from monthdelta import monthdelta

print(((dt + monthdelta(5))))  # 2020-10-25 22:01:52
