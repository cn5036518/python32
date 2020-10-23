# ### os.path 路径模块
import os

# pathvar = '/home/wangtongpei/mywork/001.txt'
pathvar = __file__

# 第一组   basename  dirname split join  splitext getsize
# 1 basename() 返回文件名部分
res = os.path.basename(pathvar)
print(res)  #3-2.os_path.py

# 2 dirname()  返回路径部分
res = os.path.dirname(pathvar)
print(res)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习

# 3 split() 将路径拆分成单独的文件部分和路径部分 组合成一个元组
res = os.path.split(pathvar)
print(res)
#('/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习', '3-2.os_path.py')
print('-----------------------------3 split')

# 4 join()  将多个路径和文件组成新的路径 可以自动通过不同的系统加不同的斜杠  *** 
# linux / windows\ ***
path1 = "home"
path2 = "wangtongpei"
path3 = "mywork"
pathvar = path1 + os.sep + path2 + os.sep + path3
print(pathvar) 
#home/wangtongpei/mywork

# 用join改造
path_new = os.path.join(path1,path2,path3)
print(path_new)
#home/wangtongpei/mywork

# 5 splitext() 将路径分割为后缀和其他部分 (了解)
pathvar = "/home/wangwen/mywork/ceshi.py"
res = os.path.splitext(pathvar)
print(res)  
#('/home/wangwen/mywork/ceshi', '.py')

pathvar = "/home/wangwen/mywork/ceshi.py"
res = pathvar.split('.')
print(res)
#['/home/wangwen/mywork/ceshi', 'py']
print('-----------------------------5 splitext')

# 6 getsize()  获取文件的大小  ***   
# 如何拼接文件的绝对路径?

# 方法1  拼接
# 第一步:获取当前文件所在目录的绝对路径
# 方法1  简洁
res = os.getcwd()  #如果没有用chdir() 就可以用os.getcwd()
print(res)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习

# 方法2  适用范围大
res = os.path.dirname(__file__) #即使用了chdir() 也可以用这个
print(res)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习

# 第二步:
path_new = os.path.join(res,'4.tarfile.py')
print(path_new)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习/4.tarfile.py

# 方法2  将相对路径转化为绝对路径
print(os.getcwd())
path_new = os.path.abspath('4.tarfile.py')
print(path_new)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习/4.tarfile.py
print('-----------------------------6-0 getsize')

os.chdir('/home/wangtongpei/mywork')
print(os.getcwd())
path_new = os.path.abspath('001.txt')
print(path_new)  #/home/wangtongpei/mywork/001.txt
print('-----------------------------6-1 getsize')

# 计算文件的大小
res = os.path.getsize(path_new)
print(res)  #2881 单位字节

# 计算目录的本身大小(非实际大小)
# path1 = os.path.dirname(__file__)
# print(path1)
# res = os.path.getsize(path1)
# print(res)
res = os.path.getsize('/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile')
print(res)  #4096  #目录的本身大小都是4096 字节
print('-----------------------------6-2 getsize')


# 第二组  检查是否  isdir  isfile  islink
# 1 isdir()    检测路径是否是一个文件夹  ***
res = os.path.isdir('/mnt/hgfs/ubuntu_gx/python32')
print(res) #True

# 2 isfile()   检测路径是否是一个文件    ***
res = os.path.isfile('/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习/4.tarfile.py')
print(res) #True   
# 应用:递归计算目录及其子目录子文件大小的时候

# 3 islink()   检测路径数否是一个链接
res = os.path.islink('/bin/lsmod')
print(res) #True
print('-----------------------------9 islink')


# 第三组  时间相关  getctime  getmtime  getatime
# 1 getctime() [windows]文件的创建时间,[linux]权限的改动时间(返回时间戳)  c-change
import time
filepath = r'/home/wangtongpei/mywork/001.txt'
res = os.path.getctime('/home/wangtongpei/mywork/001.txt')
print(res)#1601892297.0097635
print(time.ctime(res))  #时间戳==>时间字符串
#Mon Oct  5 18:04:57 2020

# wangtongpei@wangtongpei-virtual-machine:~/mywork$ stat 001.txt 
  # 文件：'001.txt'
  # 大小：7         	块：8          IO 块：4096   普通文件
# 设备：801h/2049d	Inode：833789      硬链接：1
# 权限：(0777/-rwxrwxrwx)  Uid：( 1000/wangtongpei)   Gid：( 1000/wangtongpei)
# 最近访问：2020-10-05 18:05:29.181777400 +0800
# 最近更改：2020-10-05 18:00:10.705742170 +0800
# 最近改动：2020-10-05 18:04:57.009763466 +0800
# 创建时间：-

# 2 getmtime() 获取文件最后一次内容修改时间(返回时间戳) m-modify
filepath = r'/home/wangtongpei/mywork/001.txt'
res = os.path.getmtime(filepath)
print(res) # 1601892010.7057421
print(time.ctime(res))    
# Mon Oct  5 18:00:10 2020

# 注意:文件内容修改后, mtime ctime atime 都会随之修改

# 3 getatime() 获取文件最后一次访问时间(返回时间戳) a-access
filepath = r'/home/wangtongpei/mywork/002.txt'
res = os.path.getatime(filepath)
print(res)  # 1601892092.1897264
print(time.ctime(res))
# Mon Oct  5 18:01:32 2020

# wangtongpei@wangtongpei-virtual-machine:~/mywork$ stat 002.txt
  # 文件：'002.txt'
  # 大小：0         	块：0          IO 块：4096   普通空文件
# 设备：801h/2049d	Inode：833793      硬链接：1
# 权限：(0664/-rw-rw-r--)  Uid：( 1000/wangtongpei)   Gid：( 1000/wangtongpei)
# 最近访问：2020-10-05 18:01:32.189726357 +0800
# 最近更改：2020-10-05 18:13:35.930159311 +0800
# 最近改动：2020-10-05 18:13:35.930159311 +0800
# 创建时间：-
print('-----------------------------3 getatime')


# 第四组  是否存在 绝对路径   exists  isabs  abspath
# 1 exists()   检测指定的路径是否存在(文件或者目录) ***
filepath = r'/home/wangtongpei/mywork/002.txt'
# filepath = r'/home/wangtongpei/mywork/'
res = os.path.exists(filepath)
print(res) #True

# 2 isabs()    检测一个路径是否是绝对路径
res = os.path.isabs('001.txt')
print(res)  #False

# 3 abspath()  将相对路径转化为绝对路径
res = os.path.abspath('001.txt')
print(res)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习/001.txt

if not os.path.isabs('002.txt'):
	abs_path = os.path.abspath('002.txt')
print(abs_path)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习/002.txt


# ### 作业题 : 计算一个文件夹中的所有文件大小  # 判断文件还是目录,递归子目录














