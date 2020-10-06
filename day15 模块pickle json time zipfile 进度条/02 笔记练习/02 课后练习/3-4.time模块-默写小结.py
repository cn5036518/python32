#小结默写
import time
 # 7个方法

# time()  #当前时间戳

# 时间元组<==========>时间戳==============>时间字符串1  格式:Tue Oct  6 10:30:19 2020
# localtime		    mktime				 ctime

# 时间元组============asctime=======>时间字符串1   格式:Tue Oct  6 10:30:19 2020


# 时间元组============strftime=======>时间字符串2  格式:2020-10-06 20:30:22

# 时间元组<============strptime=======时间字符串1  格式:Tue Oct  6 10:30:19 2020

#1 time()  #返回当前时间戳  无参数
time_stamp = time.time()
print(time_stamp)  #1601950404.2018447 单位秒 10位
print('------------------1 time()')

#2 localtime()   #返回时间元组 参数时间戳
# 01 参数是当前时间戳
time_tuple = time.localtime(time_stamp)  #
print(time_tuple,type(time_tuple))
#time.struct_time(tm_year=2020, tm_mon=10, tm_mday=6, tm_hour=10, tm_min=17, tm_sec=9, tm_wday=1, tm_yday=280, tm_isdst=0)
print(tuple(time_tuple),type(tuple(time_tuple)))
#(2020, 10, 6, 10, 18, 20, 1, 280, 0) <class 'tuple'>
print('------------------2-1  localtime()')

# 02 参数是指定时间戳
time_tup = time.localtime(1501950404)
print(time_tup)
# time.struct_time(tm_year=2017, tm_mon=8, tm_mday=6, tm_hour=0, tm_min=26, tm_sec=44, tm_wday=6, tm_yday=218, tm_isdst=0)
print(tuple(time_tup))  # (2017, 8, 6, 0, 26, 44, 6, 218, 0)
print(list(time_tup))  #[2017, 8, 6, 0, 26, 44, 6, 218, 0]
print('------------------2-2  localtime()')

#3 mktime()  返回时间戳 参数是时间元组
# 01 参数是当前时间元组
time_tup = time.localtime(time.time())   #把当前时间戳-->时间元组
time_stamp = time.mktime(time_tup)
print(time_stamp)  #1601951247.0
print('------------------3-1  mktime()')

# 02 参数是指定时间元组
time_tup = (2017, 8, 6, 0, 26, 44, 6, 218, 0)
time_stamp = time.mktime(time_tup)
print(time_stamp)  #1501950404.0
print('------------------3-2  mktime()')

#4 ctime()  返回时间字符串  参数是时间戳
# 01 参数是当前时间戳
time_stamp = time.time()
time_str = time.ctime(time_stamp)
print(time_str)  #Tue Oct  6 10:30:19 2020
print('------------------4-1  ctime()')

# 02 参数是指定时间戳
time_str = time.ctime(1501950404)
print(time_str) #Sun Aug  6 00:26:44 2017
print('------------------4-2  ctime()')

#5 asctime()  返回时间字符串 参数是时间元组
# 01 参数是当前时间元组
time_tup = time.localtime(time.time())  #先把当前时间戳转换成当前时间元组
time_str = time.asctime(time_tup)
print(time_str) #Tue Oct  6 10:38:01 2020
print('------------------5-1  asctime()')

# 02 参数是指定时间元组
time_tup = (2017, 8, 6, 0, 26, 44, 6, 218, 0)
# time_tup = [2017, 8, 6, 0, 26, 44, 6, 218, 0]  #TypeError: Tuple or struct_time argument required
time_str = time.asctime(time_tup)
print(time_str) #Sun Aug  6 00:26:44 2017
print('------------------5-2  asctime()')

time_tup = (2017, 8, 6, 0, 26, 44, 6, 218, 0)
time_stamp = time.mktime(time_tup)  #时间元组==>时间戳
time_str = time.ctime(time_stamp)   #时间戳==>时间字符串
print(time_str) #Sun Aug  6 00:26:44 2017
print('------------------5-2-2  asctime()')

#6 strftime()  返回时间字符串(2020-10-06格式) 参数1是时间格式化'%Y-%m-%d %H:%M:%S'  参数2是时间元组
# 01 参数是当前时间元组
time_tup = time.localtime(time.time())  #先把当前的时间戳转成当前的时间元组
print(tuple(time_tup))  #(2020, 10, 6, 10, 50, 54, 1, 280, 0)
time_str_format = time.strftime('%Y-%m-%d %H:%M:%S',time_tup)
print(time_str_format)  #2020-10-06 10:50:02
print('------------------6-1  strftime()')

# 02 参数是指定时间元组
time_tup = (2017, 8, 6, 0, 26, 44, 6, 218, 0)
time_str_format = time.strftime('%Y-%m-%d %H:%M:%S',time_tup)
#TypeError: strftime() argument 1 must be str, not tuple
print(time_str_format)  #2017-08-06 00:26:44
print('------------------6-2  strftime()')

#7 strptime() 返回时间元组,参数是时间字符串 格式'Tue Oct  6 10:30:19 2020'
# time_str = '2017-08-06 00:26:44'
#ValueError: time data '2017-08-06 00:26:44' does not match format '%a %b %d %H:%M:%S %Y'
time_str = 'Tue Oct  6 10:30:19 2020'
time_tup = time.strptime(time_str)
print(time_tup)
#time.struct_time(tm_year=2020, tm_mon=10, tm_mday=6, tm_hour=10, tm_min=30, tm_sec=19, tm_wday=1, tm_yday=280, tm_isdst=-1)
print(tuple(time_tup))#(2020, 10, 6, 10, 30, 19, 1, 280, -1)











