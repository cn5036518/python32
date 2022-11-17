# ### tarfile 压缩模块
# 小结默写
import tarfile

# 1 创建压缩包
# 01 只打包不压缩
with tarfile.open('tar43.tar','w',encoding='utf-8') as tf:  #194k
	tf.add('/bin/cp','cp')
	tf.add('/bin/echo','tmp/echo')
	
# 02 打包压缩gz
with tarfile.open('tar44.tar.gz','w:gz',encoding='utf-8') as tf:  #82K
	tf.add('/bin/cp','cp')
	tf.add('/bin/echo','tmp/echo')

# 03 打包压缩bz2
with tarfile.open('tar45.tar.bz2','w:bz2',encoding='utf-8') as tf: #75K
	tf.add('/bin/cp','cp')
	tf.add('/bin/echo','tmp/echo')

# 2 解压
# 01 解压单个文件
with tarfile.open('tar45.tar.bz2','r',encoding='utf-8') as tf:
	tf.extract('cp','tar45')  #参数1:文件的别名  参数2:解压后的路径

# 02 解压所有文件
with tarfile.open('tar45.tar.bz2','r',encoding='utf-8') as tf:

import os

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
	

safe_extract(tf, "tar45-2")

# 3 追加文件
# 不能直接追加到压缩包,也不能追加到解压后的目录,只能追加到只打包不压缩的文件中
# with tarfile.open('tar45-2','a',encoding='utf-8') as tf:
	# tf.add('/bin/chmod','chmod')  #IsADirectoryError: [Errno 21] Is a directory: 'tar45-2'

with tarfile.open('tar43.tar','a',encoding='utf-8') as tf:	
	tf.add('/bin/chmod','chmod')

# 4 查看文件
with tarfile.open('tar45.tar.bz2','r',encoding='utf-8') as tf:
	lst = tf.getnames()
	print(lst)  #['cp', 'tmp/echo']





































