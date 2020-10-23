# ### zipfile 压缩模块
import zipfile

# 1 压缩
# 创建压缩包
#zipfile.ZIP_DEFLATED 压缩减少空间  不写这个,就是只打包不压缩
zf = zipfile.ZipFile('ceshi113.zip','w',zipfile.ZIP_DEFLATED)

# 写入文件
# write(路径,别名)
zf.write('/bin/bash','bash')
zf.write('/bin/cat','tmp/cat')

# 关闭文件
zf.close()

# 2 解压
zf = zipfile.ZipFile('ceshi113.zip','r')
# 解压单个文件
# extract(文件,文件夹)
zf.extract('bash','ceshi113')

# 解压所有文件
# extract(文件夹)
zf.extractall('ceshi223')

zf.close()

# 3 追加
# 追加文件到压缩包
zf = zipfile.ZipFile('ceshi113.zip','a',zipfile.ZIP_DEFLATED)
zf.write('/bin/chmod','chmod')
zf.close()

with zipfile.ZipFile('ceshi113.zip','a',zipfile.ZIP_DEFLATED) as zf:
	zf.write('/bin/chmod','chmod123')


# 4 查看文件
with zipfile.ZipFile('ceshi113.zip','r') as zf:
	lst = zf.namelist()
	print(lst)  #['bash', 'tmp/cat', 'chmod', 'chmod123']
	
















































