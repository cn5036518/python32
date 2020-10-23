# ### time 时间模块
import time

#1 time()  获取本地时间戳
res = time.time()
print(res)  #1601424750.230435

# localtime <=======> mktime =======> ctime
# 时间元组           时间戳           时间字符串

# 2 localtime()   获取本地时间元组    (参数是时间戳,不写默认当前)
#默认当前时间元组
ttp = time.localtime()
print(ttp)
#time.struct_time(tm_year=2020, tm_mon=9, tm_mday=30,
# tm_hour=8, tm_min=16, tm_sec=20, tm_wday=2, tm_yday=274, tm_isdst=0)

# 指定具体的时间戳
ttp = time.localtime(1601360000)
print(ttp) #time.struct_time(tm_year=2020, tm_mon=9, tm_mday=29, 
#tm_hour=14, tm_min=13, tm_sec=20, tm_wday=1, tm_yday=273, tm_isdst=0)

# 3 mktime()   通过时间元组获取时间戳   (参数是时间元组,必填)
timestamp1 = time.mktime(ttp)
print(timestamp1)  #1601360000.0

# 4 ctime()  获取本地时间字符串(参数是时间戳,不写默认当前)
# 默认当前时间戳
time_str = time.ctime()
print(time_str)  #Wed Sep 30 08:22:21 2020

# 指定具体的时间戳
time_str = time.ctime(1601360000)
print(time_str)  #Tue Sep 29 14:13:20 2020

# 5 asctime()  通过时间元组获取时间字符串(参数是时间元组,必填)  (了解)
# 只能通过手动的形式来调星期
time_tuple =  (2020,9,29,16,48,30,0,0,0)
time_str = time.asctime(time_tuple)
print(time_str)  #Mon Sep 29 16:48:30 2020

# 5-2 mktime 配合 ctime来取代asctime (推荐)
# 自动识别当前是周几
time_tuple =  (2020,9,29,16,48,30,0,0,0)





































