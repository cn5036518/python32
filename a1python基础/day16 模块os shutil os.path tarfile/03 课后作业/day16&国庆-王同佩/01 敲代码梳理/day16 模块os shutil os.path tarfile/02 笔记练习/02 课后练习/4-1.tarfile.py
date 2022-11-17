# ### tarfile 压缩模块
import tarfile
# (1) 压缩文件

# 1.只是单纯的打包.
# 创建压缩包
tf = tarfile.open('ceshi0930_0.tar','w',encoding= 'utf-8')

# 写入文件
# add(路径,别名)
tf.add('/bin/chown','chown')
tf.add('/bin/cp','cp')
tf.add('/bin/dash','tmp/dash')

# 关闭文件
tf.close()  # 378880

# 2.使用gz算法压缩
tf = tarfile.open('ceshi0930_1.tar.gz','w:gz',encoding='utf-8')

# 写入文件
# add(路径,别名)
tf.add('/bin/chown','chown')
tf.add('/bin/cp','cp')
tf.add('/bin/dash','tmp/dash')

# 关闭文件
tf.close()  # 180413

# 3.使用bz2算压缩
tf = tarfile.open('ceshi0930_2.tar.bz2','w:bz2',encoding='utf-8')
# 写入文件
# add(路径,别名)
tf.add('/bin/chown','chown')
tf.add('/bin/cp','cp')
tf.add('/bin/dash','tmp/dash')

# 关闭文件
tf.close()   ## 163261

# (2) 解压文件
tf = tarfile.open('ceshi0930_1.tar.gz','r',encoding='utf-8')
# extract(文件,路径) 解压单个文件
tf.extract('chown','ceshi0930_1')

# extractall(路径) 解压所有文件
tf.extractall('ceshi0930_1_2')

tf.close()

# (3) 追加文件
# 对已经压缩过的包无法进行追加文件,只能是没有压缩过的包进行追加文件
tf = tarfile.open('ceshi0930_0.tar','a',encoding= 'utf-8')
tf.add('/bin/mkdir','mkdir')
tf.close()

# (4) 查看文件
with tarfile.open('ceshi0930_0.tar','r',encoding='utf-8') as tf:
	lst = tf.getnames()
	print(lst)  #['chown', 'cp', 'tmp/dash', 'mkdir']

# tarfile和zipfile的区别
# tarfile的bz2压缩,会更小
# zipfile可以直接给压缩包追加文件.tarfile不行

# ### 追加文件到压缩包中再压缩
import os,shutil
# 思路:
# 1.把已经压缩的包进行解压
# 2.把要追加的内容放进去
# 3.过滤文件
# 4.重新打包

# 记录压缩包所在的绝对路径
pathvar1 = os.path.abspath('ceshi0930_2.tar.bz2')
print(pathvar1)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/ceshi0930_2.tar.bz2

# 要解压到哪个文件夹(绝对路径)
# print(os.getcwd())  #当前文件所在目录的绝对路径  #方法1
# /mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile
#
# # print(__file__)    #方法2
#  /mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/4-1.tarfile.py
# # print(os.path.dirname(__file__))
# /mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile

pathvar2 = os.path.join(os.getcwd(),'ceshi0930_2')
print(pathvar2)
# /mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/ceshi0930_2

# 1.把已经压缩的包进行解压  解压到指定路径
with tarfile.open(pathvar1,'r',encoding= 'utf-8') as tf:
def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(tf, pathvar2)

# 2.把要追加的内容放进去  (复制文件或add都可)
shutil.copy('/bin/echo',pathvar2)
shutil.copy('/bin/ip',pathvar2)
# tf.add('/bin/ip',pathvar)  #注意:如果用add,tf不能用with,因为会关闭tf对象
# OSError: TarFile is closed

# 3.过滤文件
# 先查看文件夹当中有什么文件
lst = os.listdir(pathvar2)
print(lst)  #['chown', 'cp', 'echo', 'ip', 'tmp']

with tarfile.open(pathvar1,'w:bz2',encoding= 'utf-8') as tf:
	for i in lst:
		if i != 'chown':
			#拼凑成完整的绝对路径
			abs_path = os.path.join(pathvar2,i)
			#除了chown外,其余的都要压缩
			# add(文件的完整路径和文件名,别名)
			tf.add(abs_path,i)

# /mnt/hgfs/python32_gx/day16/ceshi0930_2/chown
	# /mnt/hgfs/python32_gx/day16/ceshi0930_2/cp
	# /mnt/hgfs/python32_gx/day16/ceshi0930_2/echo	
	# tf.add("/bin/chown","chown")	


# 4.重新打包













































