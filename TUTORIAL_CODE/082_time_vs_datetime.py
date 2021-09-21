from time import localtime, strftime
now = 1407694710
local_tuple = localtime(now)
print(local_tuple)
# time.struct_time(tm_year=2014, tm_mon=8, tm_mday=10, tm_hour=23, tm_min=48, tm_sec=30, tm_wday=6, tm_yday=222, tm_isdst=0)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print(time_str)
# 2014-08-10 11:18:30

from time import mktime, strptime

time_tuple = strptime(time_str, time_format)
print(time_tuple)
# time.struct_time(tm_year=2014, tm_mon=8, tm_mday=10, tm_hour=23, tm_min=48, tm_sec=30, tm_wday=6, tm_yday=222, tm_isdst=-1)
utc_now = mktime(time_tuple)
print(utc_now)

# 1407694710.0

parse_format = '%Y-%m-%d %H:%M:%S %Z'
depart_sfo = '2014-05-01 15:45:16 PDT'
time_tuple = strptime(depart_sfo, parse_format)
time_str = strftime(time_format, time_tuple)
print(time_str)

# 2014-05-01 15:45:16

arrival_nyc = '2014-05-01 23:33:24 EDT'
time_tuple = strptime(arrival_nyc, time_format)

# ValueError: unconverted data remains:  EDT

# platform-dependent nature of the time module

from datetime import datetime, timezone

now = datetime(2014, 8, 10, 18, 18, 30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_local)

# 2014-08-10 11:18:30-07:00

time_str = '2014-08-10 11:18:30'
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = mktime(time_tuple)
print(utc_now)

# 1407694710.0

'''
Unlike the time module, the datetime module has facilities for reliably converting from one local time to another local time. However, datetime only provides the machinery for time zone operations with its tzinfo class and related methods. What’s missing are the time zone definitions besides UTC.
'''

# hence pytz

'''
To use pytz effectively, you should always convert local times to UTC first. Perform any datetime operations you need on the UTC values (such as offsetting). Then, convert to local times as a final step.
'''

import pytz

arrival_nyc = '2014-05-01 23:33:24'
nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
eastern = pytz.timezone('US/Eastern')
nyc_dt = eastern.localize(nyc_dt_naive)
utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
print(utc_dt)

# 2014-05-02 03:33:24+00:00

pacific = pytz.timezone('US/Pacific')
sf_dt = pacific.normalize(utc_dt.astimezone(pacific))
print(sf_dt)

# 2014-05-01 20:33:24-07:00

nepal = pytz.timezone('Asia/Katmandu')
nepal_dt = nepal.normalize(utc_dt.astimezone(nepal))
print(nepal_dt)

# 2014-05-02 09:18:24+05:45

