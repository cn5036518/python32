# time 时间模块
import time

# 1 time()   获取本地时间戳
res = time.time()
print(res)  #1601464907.9929702

# localtime <=======> mktime =============> ctime
# 时间元组			时间戳				 时间字符串1  Wed Sep 30 19:34:16 2020

# 时间元组=======>asctime=======>时间字符串1   Wed Sep 30 19:34:16 2020

# 时间元组=======>strftime=======>时间字符串2   2020-10-31 10:10:10

# 时间元组<=======strptime<=======时间字符串2


# 2 localtime   获取本地时间元组
# 参数不写.默认当前时间元组
time_tuple = time.localtime()
print(time_tuple)
#time.struct_time(tm_year=2020, tm_mon=9, tm_mday=30,
# tm_hour=19, tm_min=26, tm_sec=34, tm_wday=2, tm_yday=274, tm_isdst=0)

# 指定具体的时间戳
time_tuple = time.localtime(1601360000)
print(time_tuple)
# time.struct_time(tm_year=2020, tm_mon=9, tm_mday=29,
# tm_hour=14, tm_min=13, tm_sec=20, tm_wday=1, tm_yday=273, tm_isdst=0)

# 3 mktime()  通过时间元组获取时间戳  参数是时间元组
time_tuple = (2020,9,29,16,48,30,0,0,0)
time_stamp = time.mktime(time_tuple)
print(time_stamp)  #1601369310.0

# 4 ctime()    获取本地时间字符串(参数是时间戳,默认当前)
# 默认当前时间戳
res = time.ctime()
print(res)  #Wed Sep 30 19:34:16 2020

# 指定具体的时间戳
time_str = time.ctime(1601360000)
print(time_str)  #Tue Sep 29 14:13:20 2020

# 5 asctime()  通过时间元组获取时间字符串
time_tuple = (2020,9,29,16,48,30,0,0,0)
time_str = time.asctime(time_tuple)
print(time_str)  #Mon Sep 29 16:48:30 2020

#  通过时间元组获取时间字符串 方法2
time_tuple = (2020,9,29,16,48,30,0,0,0)
time_stamp = time.mktime(time_tuple)  #1先获取时间戳
print(time_stamp)  #1601369310.0

time_str = time.ctime(time_stamp)  #1获取时间字符串
print(time_str)  #Tue Sep 29 16:48:30 2020

# 6 strftime() 指定格式输出  时间字符串   时间元组==>时间字符串
# 默认当前时间元组
time_str = time.strftime('%Y-%m-%d %H:%M:%S')
print(time_str,type(time_str))
# 2020-09-30 19:43:50 <class 'str'>

# 指定时间元组
strvar = time.strftime("%Y-%m-%d %H:%M:%S",(2020,10,31,10,10,10,0,0,0))
print(strvar)  #2020-10-31 10:10:10

# 7 strptime()  将时间字符串通过指定格式提取到时间元组中(时间字符串,格式化字符串) 
#替换时间格式化标签时,必须严丝合缝.不能随便加空格或特殊字符
ttp = time.strptime("2020年的9月29号是杜兰特的生日,晚上20点30分40秒准备轰趴派队","%Y年的%m月%d号是杜兰特的生日,晚上%H点%M分%S秒准备轰趴派队")
print(ttp)
#time.struct_time(tm_year=2020, tm_mon=9, tm_mday=29, tm_hour=20, tm_min=30, tm_sec=40, tm_wday=1, tm_yday=273, tm_isdst=-1)

print('-------------------------------------------')

# 小结:  7个方法
# 时间戳  time.time()

# localtime <=======> mktime =============> ctime
# 时间元组			时间戳				 时间字符串1  Wed Sep 30 19:34:16 2020

# 时间元组=======>asctime=======>时间字符串1   Wed Sep 30 19:34:16 2020

# 时间元组=======>strftime=======>时间字符串2   2020-10-31 10:10:10

# 时间元组<=======strptime<=======时间字符串2

# time_tuple = (2020,9,29,16,48,30,0,0,0)  #时间元组作为参数
# time.struct_time(tm_year=2020, tm_mon=9, tm_mday=29)   #时间元组输出



















