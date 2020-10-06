# ### zipfile 压缩模块
# 小结默写
import zipfile

# (1) 压缩文件
# """ zipfile.ZIP_DEFLATED 压缩减少空间   不加就是只打包不压缩 """
# 1 创建压缩包
# with zipfile.open('zf43.zip','w','ZIP_DEDLATED') as zf: #AttributeError: module 'zipfile' has no attribute 'open'
with zipfile.ZipFile('zf43.zip','w',zipfile.ZIP_DEFLATED) as zf:  #95k  #打包压缩
	zf.write('/bin/cp','cp')
	zf.write('/bin/chmod','tmp/chmod')	
	
with zipfile.ZipFile('zf431.zip','w') as zf:  #只打包不压缩  203k
	zf.write('/bin/cp','cp')
	zf.write('/bin/chmod','tmp/chmod')

# 2 写入文件
# '''write(绝对路径,别名)'''
# 3 关闭文件


# (2) 解压文件
# 1 解压单个
# """extract(文件别名,路径)    路径是文件要解压到的目录"""
with zipfile.ZipFile('zf43.zip','r') as zf:
	zf.extract('cp','zf43')

# 2 解压所有
# """extractall(路径)   路径是文件要解压到的目录"""
with zipfile.ZipFile('zf43.zip','r') as zf:
	zf.extractall('zf431')

# (3) 追加文件
with zipfile.ZipFile('zf43.zip','a') as zf:
	zf.write('/bin/echo','echo')

# (4) 查看文件
# namelist()
with zipfile.ZipFile('zf43.zip','r') as zf:
	lst = zf.namelist()
	print(lst)  #['cp', 'tmp/chmod', 'echo']


# zipfile和tarfile的区别
# 1 zipfile可以直接给压缩包追加文件,tarfile不能直接追加
# 2 tarfile的bz2压缩算法,压缩后的大小比gz压缩算法更小,zipfile的压缩算法是gz

# 打开文件对象
# zipfile是zipfile.ZipFile
# tarfile是tarfile.open

# 添加文件
# zipfile是write(绝对路径,别名)
# tarfile是add(绝对路径,别名)

# 查看文件
# zipfile是namelist
# tarfile是getnames

































