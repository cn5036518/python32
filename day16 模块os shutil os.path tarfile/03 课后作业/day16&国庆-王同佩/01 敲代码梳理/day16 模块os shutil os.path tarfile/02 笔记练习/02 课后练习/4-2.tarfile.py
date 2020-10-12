# ### tarfile 压缩模块
import tarfile
# (1) 压缩文件
# 1.只是单纯的打包.
# 01 创建压缩包
tf = tarfile.open('ceshi0930_0.tar','w',encoding='utf-8')

# 02 写入文件
# """add(路径,别名)"""
tf.add('/bin/chown','chown')
tf.add("/bin/cp","cp")
tf.add('/bin/dash','tmp/dash')

# 03 关闭文件
tf.close()  # 378880


# 2.使用gz算法压缩
# 01 创建压缩包
tf = tarfile.open('ceshi0930_1.tar.gz','w:gz',encoding='utf-8')

# 02 写入文件
# """add(路径,别名)"""
tf.add('/bin/chown','chown')
tf.add("/bin/cp","cp")
tf.add('/bin/dash','tmp/dash')

# 03 关闭文件
tf.close()  # 180413


# 3.使用bz2算法压缩
# 01 创建压缩包
tf = tarfile.open('ceshi0930_2.tar.bz2','w:bz2',encoding='utf-8')

# 02 写入文件
# """add(路径,别名)"""
tf.add('/bin/chown','chown')
tf.add("/bin/cp","cp")
tf.add('/bin/dash','tmp/dash')

# 03 关闭文件
tf.close()  # 163261  单位 字节



# (2) 解压文件
# 01 打开压缩包
tf = tarfile.open('ceshi0930_1.tar.gz','r',encoding='utf-8')

# 02 解压文件
# """ 001 extract(文件,路径) 解压单个文件"""
tf.extract('chown','ceshi0930_1')

# """ 002 extract(路径) 解压所有文件"""
tf.extractall('ceshi0930_1_2')

# 03 关闭文件
tf.close() 

# (3) 追加文件
# """tarfile对已经压缩过的包无法进行追加文件,只能是没有压缩过的包进行追加文件"""
# 01 打开压缩包
tf = tarfile.open('ceshi0930_0.tar','a',encoding='utf-8')  #a 追加模式

# 02 追加文件
tf.add('/bin/mkdir','mkdir')

# 03关闭文件
tf.close() 

# 使用with进行改造
with tarfile.open('ceshi0930_0.tar','a',encoding='utf-8') as tf:
	tf.add('/bin/mkdir','mkdir12')


# (4) 查看文件
with tarfile.open('ceshi0930_0.tar','r',encoding='utf-8') as tf:
	lst = tf.getnames()
	print(lst)  #['chown', 'cp', 'tmp/dash', 'mkdir', 'mkdir12']


# ### 追加文件到压缩包中在压缩
import os,shutil

# 1.把已经压缩的包进行解压
# 2.把要追加的内容放进去
# 3.过滤文件重新压缩

# 记录压缩包所在的绝对路径
pathvar1 = os.path.abspath('ceshi0930_2.tar.bz2')
print(pathvar1)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习/ceshi0930_2.tar.bz2

# 要解压到哪个文件夹中(绝对路径)
pathvar2 = os.path.join(os.getcwd(),'ceshi0930_2')
print(pathvar2)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习/ceshi0930_2

# 1.把已经压缩的包进行解压
with tarfile.open(pathvar1,'r',encoding='utf-8') as tf:
	tf.extractall(pathvar2)

# 2.把要追加的内容放进去  copy
shutil.copy('/bin/echo',pathvar2)

# 3.过滤文件重新压缩
# 01 查看文件夹当中有什么文件
lst = os.listdir(pathvar2)
print(lst)  #['chown', 'cp', 'echo', 'tmp']

# 02 比如:除了文件chown外,其他的打包压缩
with tarfile.open(pathvar1,'w:gz',encoding='utf-8') as tf:  #压缩包在原来的位置不变
	for i in lst:
		if i != 'chown':
			#拼接文件的绝对路径
			abs_path = os.path.join(pathvar2,i)
			# """add(绝对路径,别名)"""
			tf.add(abs_path,i)
print('---------------------------')

# ### 追加文件到压缩包中在压缩   自己写一个

# 1 把压缩包1解压到文件夹a
# 2 把文件追加到文件夹a
# 3 把文件夹a压缩,替换原来的压缩包1

import os,shutil,tarfile
#压缩包1的绝对路径
pathvar1 = os.path.abspath('ceshi0930_1.tar.gz')
print(pathvar1)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习/ceshi0930_1.tar.gz

# 文件夹a的绝对路径
pathvar2 = os.path.join(os.getcwd(),'ceshi0930_3')
print(pathvar2)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习/ceshi0930_3

# 1 把压缩包1解压到文件夹a
with tarfile.open(pathvar1,'r',encoding='utf-8') as tf:
	tf.extractall(pathvar2)

# 2 把文件追加到文件夹a copy
shutil.copy('/bin/echo',pathvar2)

# 3 把文件夹a压缩,替换原来的压缩包1
# 01 查看文件夹a有哪些文件
lst = os.listdir(pathvar2)
print(lst) #['chown', 'cp', 'echo', 'tmp']

# 02 比如:除了文件'chown'外,其他都压缩
with tarfile.open(pathvar1,'w:gz',encoding='utf-8') as tf:
	for i in lst:
		if i != 'chown':
			#拼接绝对路径(绝对路径+文件名)
			# print(os.getcwd())  #打印当前工作路径
			#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习
			# abs_path = os.path.abspath(i)	  #因为i不在当前工作路径	如果i在当前工作路径就可以这么用	
			abs_path = os.path.join(pathvar2,i)			
			#tf.add(绝对路径,别名)
			tf.add(abs_path,i)














































