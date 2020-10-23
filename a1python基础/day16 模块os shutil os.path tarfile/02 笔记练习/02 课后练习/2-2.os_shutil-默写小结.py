# ### os 模块 (文件操作) 新建/删除/ 
import os
os.chdir('/home/wangtongpei/mywork')

# -- os模块具有 新建/删除/

#01 os.mknod   创建文件
# os.mknod('1.txt')  #
# os.mknod('1.txt')  #不能重复创建
# FileExistsError: [Errno 17] File exists

#02 os.remove  删除文件
# os.remove('1.txt')
# os.remove('1.txt')  #不能重复删除
#FileNotFoundError: [Errno 2] No such file or directory: '1.txt'

#03 os.mkdir   创建目录(文件夹)
# os.mkdir('ceshi111')
# os.mkdir('ceshi111') #不能重复创建
#FileExistsError: [Errno 17] File exists: 'ceshi111'

#04 os.rmdir   删除目录(文件夹)
# os.rmdir('ceshi111')
# os.rmdir('ceshi111')  #不能重复删除
#FileNotFoundError: [Errno 2] No such file or directory: 'ceshi111'

#05 os.rename  对文件,目录重命名
# 001 文件重命名
# os.rename('2.txt','3.txt')
# os.rename('2.txt','3.txt')   #不能重复重命名
# FileNotFoundError: [Errno 2] No such file or directory: '2.txt' -> '3.txt'

# 002 目录重命名
# os.rename('001','002')
# os.rename('001','002')  #不能重复重命名
#FileNotFoundError: [Errno 2] No such file or directory: '001' -> '002'

#06 os.makedirs   递归创建文件夹
# os.makedirs('a/b')
# os.makedirs('a/b')  # #不能重复创建
#FileExistsError: [Errno 17] File exists: 'a/b'

#07 os.removedirs 递归删除文件夹（空文件夹）
# os.removedirs('a/b')
# os.removedirs('a/b')   #不能重复删除
#FileNotFoundError: [Errno 2] No such file or directory: 'a/b'
# 如果非空 OSError: [Errno 39] Directory not empty: 'a/b'


# 小结
# 1 创建文件
# os.mknod('jack.txt')
# os.mknod('jack2.txt')  #留着1

# 2 删除文件
# os.remove('jack.txt')

# 3 创建目录
# os.mkdir('a1')
# os.mkdir('a2')  #留着2

# 4 删除目录
# os.rmdir('a1')

# 5 重命名文件
# os.rename('jack2.txt','jack3.txt')

# 6 重命名目录
# os.rename('a2','a3')

# 7 递归创建目录
# os.makedirs('a/b')
# os.makedirs('c/d')  #留着3

# 8 递归删除目录(空目录)
# os.removedirs('a/b')


# ### shutil模块 复制/移动/
import shutil

#01 copyfileobj(fsrc, fdst[, length=16*1024])  
#复制文件 (length的单位是字符(表达一次读多少字符/字节))
# fp_src = open("3.txt",mode="r",encoding="utf-8")
# fp_dst = open("4.txt",mode="w",encoding="utf-8")
# shutil.copyfileobj(fp_src,fp_dst)

#02 #copyfile(src,dst)   #单纯的仅复制文件内容 , 底层调用了 copyfileobj
# shutil.copyfile('4.txt','5.txt')

#03 copymode(src,dst)   #单纯的仅复制文件权限 , 不包括内容  
#(虚拟机共享目录都是默认777)
# """注意: 要先有两个文件才可以,不会默认创建"""
# shutil.copymode('4.txt','5.txt')

#04 copystat(src,dst)   #复制所有状态信息,包括权限，组，用户，修改时间等,
# 不包括内容
# shutil.copystat('4.txt','5.txt')

#05 copy(src,dst)       #复制文件权限和内容
# shutil.copy('5.txt','6.py')

#06 copy2(src,dst)      #复制文件权限和内容,还包括权限，组，用户，时间等
# shutil.copy2('5.txt','6.py')

#07 copytree(src,dst)   #拷贝文件夹里所有内容(递归拷贝)
# shutil.copytree('c','ff')
# shutil.copytree('c','ff')   #不能重复拷贝
#FileExistsError: [Errno 17] File exists: 'ff'

#08 rmtree(path)        #删除当前文件夹及其中所有内容(递归删除)  谨慎使用
# shutil.rmtree('ff')
# shutil.rmtree('ff')   #不能重复删除
# FileNotFoundError: [Errno 2] No such file or directory: 'ff'

#09 move(path1,paht2)   #移动文件或者文件夹
# shutil.move('6.py','c/88.php')  #这里目录c必须是存在的,如果不存在,会报错.不会自动创建
# shutil.move('6.py','c/88.php')  #不能重复移动
# FileNotFoundError: [Errno 2] No such file or directory: '6.py'

# 小结
# 复制8个  shutil模块
import shutil
	# 1 普通复制 6个
		# 1 底层
obj1 = open('001.txt',mode='r',encoding='utf-8')
obj2 = open('002.txt',mode='w',encoding='utf-8')
		
# shutil.copyfileobj(obj1,obj2)
		
		# 2 仅仅复制内容
# shutil.copyfile('001.txt','003.txt')
			
		# 3 复制权限(不复制修改时间),不复制内容
# shutil.copymode('001.txt','004.txt')  #004.txt必须是事先存在的,不存在的话,不会自动创建
#FileNotFoundError: [Errno 2] No such file or directory: '004.txt'
		
		# 4 复制其他(权限,修改时间等),不复制内容
# shutil.copystat('001.txt','005.txt')   #005.txt必须是事先存在的,不存在的话,不会自动创建
		
		# 5 复制权限+内容(不包括修改时间)
# shutil.copy('001.txt','006.txt')
		
		# 6 复制权限+内容+修改时间
# shutil.copy2('001.txt','007.txt')
	
	
	# 2 递归复制+递归删除 2个
	# 递归复制目录及其子目录
# shutil.copytree('c','ffda')
	
	# 递归删除目录及其子目录   谨慎使用
# shutil.rmtree('ffda')

# 移动1个
# move()
# shutil.move('005.txt','c')






































