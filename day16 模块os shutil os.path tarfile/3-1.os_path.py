# ### os.path 路径模块
import os

pathvar = '/home/wangtongpei/mywork/6.py'
pathvar = __file__   #当前py文件所在的绝对路径
print(pathvar)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/3-1.os_path.py

#1 basename() 返回文件名部分
res = os.path.basename(pathvar)
print(res)  #3-1.os_path.py

#2 dirname()  返回路径部分
res = os.path.dirname(pathvar)
print(res)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile

#3 split() 将路径拆分成单独的文件部分和路径部分 组合成一个元组
res = os.path.split(__file__)
print(res)
# ('/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile', 
#'3-1.os_path.py')

#4 join() 将多个路径和文件组成新的路径  可以自动通过不同的系统加不同的斜杠
   # linux /  windows \    ***
path1 = 'home'
path2 = 'wangtongpei'
path3 = 'mywork'
pathvar = path1 + os.sep + path2 + os.sep + path3
print(pathvar)  #home/wangtongpei/mywork

# 用join改造  拼接路径
path_new = os.path.join(path1,path2,path3)
print(path_new) #home/wangtongpei/mywork

# 用join改造  拼接路径+文件
path1 = 'home'
path2 = 'wangtongpei'
path3 = 'mywork'
path4 = '6.py'
path_new = os.path.join(path1,path2,path3,path4)
print(path_new) #home/wangtongpei/mywork/6.py

#5 splitext() 将路径分割为后缀和其他部分(了解)
pathvar = "/home/wangwen/mywork/ceshi.py"
res = os.path.splitext(pathvar)
print(res)  #('/home/wangwen/mywork/ceshi', '.py')
print(res[-1])  #.py

#6 getsize() 获取文件的大小  ***  
# 这里只能获取文件的大小,而无法获取文件夹的大小
pathvar = os.getcwd()  #获取当前py文件所在的目录  #方法1
# pathvar = os.path.dirname(__file__)  #这里的__file__不能加引号  #方法2

print(pathvar)
print('-----------------------6-1')
# /mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile
path_new = os.path.join(pathvar,'__init__.py')
print(path_new)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/__init__.py

# 计算文件大小
res = os.path.getsize(path_new)
print(res)   #96  字节


# 7 isdir()  检测路径是否是一个文件夹   ***
res = os.path.isdir('/mnt/hgfs/ubuntu_gx/python32')
print(res)  #True

# 8 isfile()  检测路径是否是一个文件  ***
res = os.path.isfile('/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/__init__.py')
print(res)  #True

# 9 islink()  检测路径是否是一个链接 
res = os.path.islink('/etc/resolv.conf')
print(res)  #True


#10 getctime() windows文件的创建时间  linux权限的改动时间(返回时间戳) c-change
import time
res = os.path.getctime('/home/wangtongpei/mywork/4.txt')
print(res)  #1601437813.3984275
time_str = time.ctime(res)
print(time_str)  #Wed Sep 30 11:50:13 2020

# os.system('stat /home/wangtongpei/mywork/4.txt')
os.chdir("/home/wangtongpei/mywork")
os.system('stat 4.txt')

# 最近访问：2020-09-30 11:50:13.394427455 +0800  a-access  atime
# 最近更改：2020-09-30 11:50:13.394427455 +0800   m-modify  mtime
# 最近改动：2020-09-30 11:50:13.398427422 +0800   c-change   ctime

# 最近访问：2020-09-30 16:24:00.750029695 +0800   cat查看  atime
# 最近更改：2020-09-30 16:24:25.714131923 +0800   内容修改  mtime
# 最近改动：2020-09-30 16:25:11.862314016 +0800   权限修改  ctime


#11 getmtime()  获取文件最后一次修改时间(返回时间戳)  m-modify
time_stamp = os.path.getmtime('/home/wangtongpei/mywork/4.txt')
time_str = time.ctime(time_stamp)
print(time_str)
# Wed Sep 30 16:24:25 2020

#12 getatime()  获取文件最后一次访问时间(返回时间戳)   a-access
time_stamp = os.path.getatime('/home/wangtongpei/mywork/4.txt')
time_str = time.ctime(time_stamp)  #把时间戳转成时间字符串   1-3
print(time_str)  #Wed Sep 30 16:24:00 2020


#13 exists()  检测指定的路径是否存在   ***
res = os.path.exists('/home/wangtongpei/mywork/4.txt')
print(res)  #True

#14 isabs() 检测一个路径是否是绝对路径
res = os.path.isabs('4.txt')
print(res)  #False

#15 abspath()   #将相对路径转化成绝对路径
res = os.path.abspath('4.txt')
print(res)  #/home/wangtongpei/mywork/4.txt

pathvar = '6.py'
if not os.path.isabs(pathvar):
	abs_path = os.path.abspath('6.py')
print(abs_path)
#/home/wangtongpei/mywork/6.py

# ### 作业题:计算一个文件夹中的所有文件大小  listdir



































