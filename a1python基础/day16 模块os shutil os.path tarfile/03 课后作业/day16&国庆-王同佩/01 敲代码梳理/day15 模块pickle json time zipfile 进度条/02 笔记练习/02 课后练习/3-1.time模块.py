# ### time 时间模块
import time

# time()   获取本地时间戳
res = time.time()
print(res)  #1601371552.7074633

# localtime <==> mktime ==> ctime

# localtime()  获取本地时间元组   (参数是时间戳,默认当前)
# 默认当前时间元组
ttp = time.localtime()
print(ttp)
# time.struct_time(tm_year=2020, tm_mon=9, tm_mday=29, 
# tm_hour=17, tm_min=28, tm_sec=43, tm_wday=1, tm_yday=273, tm_isdst=0)

# 指定具体的时间戳
ttp = time.localtime(1601360000)
print(ttp)
#time.struct_time(tm_year=2020, tm_mon=9, tm_mday=29, 
# tm_hour=14, tm_min=13, tm_sec=20, tm_wday=1, tm_yday=273, tm_isdst=0)


# mktime()   通过时间元组获取时间戳  (参数是时间元组)
res1 = time.mktime(ttp)
print(res1) #1601360000.0

# ctime()  获取本地时间字符串(参数是时间戳,默认当前)
# 默认当前时间戳
res = time.ctime()
print(res)  #Tue Sep 29 17:33:43 2020

# 指定具体的时间戳
res = time.ctime(1601360000)
print(res)  #Tue Sep 29 14:13:20 2020

# asctime() 通过时间元组获取时间字符串(参数是时间元组) (了解)
# 只能通过手动的形式来调星期
ttp = (2020,9,29,16,48,30,0,0,0)  #时间元组
res = time.asctime(ttp)
print(res) #Mon Sep 29 16:48:30 2020

# mktime配合ctime 来取代asctime(推荐)
# 自动识别当前是周几
ttp = (2020,9,29,16,48,30,0,0,0)  #时间元组
res = time.mktime(ttp)
print(res)  #1601369310.0
strvar = time.ctime(res)
print(strvar)  #Tue Sep 29 16:48:30 2020

# sleep() 程序睡眠等待
# time.sleep(3)
# print('我睡醒了')

# strftime()  格式化时间字符串(格式化字符串,时间元组)
# linux 支持中文,window不支持
strvar = time.strftime('%Y-%m-%d %H:%M:%S')
print(strvar) #2020-09-29 17:42:57

strvar = time.strftime('%Y-%m-%d %H:%M:%S 是杜兰特的生日')
print(strvar) #2020-09-29 17:44:18 是杜兰特的生日

strvar = time.strftime('%Y-%m-%d %H:%M:%S',(2020,10,31,10,10,10,0,0,0))
print(strvar)  #2020-10-31 10:10:10

# strptime()  
#将时间字符串通过指定格式提取到时间元组中
# (时间字符串,格式化字符串)
# 注意:替换时间格式化标签时,不能随便加空格或特殊字符

ttp = time.strptime("2020年的9月29号是杜兰特的生日,晚上20点30分40秒准备轰趴派队","%Y年的%m月%d号是杜兰特的生日,晚上%H点%M分%S秒准备轰趴派队")
print(ttp)
#time.struct_time(tm_year=2020, tm_mon=9, tm_mday=29,
 # tm_hour=20, tm_min=30, 
# tm_sec=40, tm_wday=1, tm_yday=273, tm_isdst=-1)

# strftime : 把时间元组==> 字符串
# srrptime:  把字符串  ==> 时间元组


# perf_counter()  用于计算程序运行的时间(了解)

startime = time.perf_counter()
for i in range(10000000):
	pass
endtime = time.perf_counter()
print('中间用时:',endtime-startime)
# 中间用时: 0.31045610300498083

startime = time.time()
for i in range(10000000):
	pass
endtime = time.time()
print('中间用时:',endtime-startime)
#中间用时: 0.3188009262084961






























