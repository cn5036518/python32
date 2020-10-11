# 1什么是递归?
# 2递归总结的4个特点
	# 1 必须有递归终止条件
	# 2  去-递的过程,不断在开辟新的栈帧空间
	#     回-归的过程,不断在释放空间
	# 3  触发归的2个条件
	#    1.代码执行完了
	#    2.return 向上返回调用处
	# 4 普通递归  return后面是表达式.一般是一个参数
	#   尾递归    return后面不是表达式,而是函数本身,一般是2,3个参数,最终返回的是参数
	#             归的时候,第一层和最后一层的结果是一致的.所以只需要考虑去的过程


# 3默认递归深度  1000  995 997 998

# 4求任意数n的阶乘,简述整个执行过程
# 方法1:普通实现
def func(n):
	total = 1  #累乘初始值是1
	# for i in range(n,0,-1):
	for i in range(1,n+1):
		total *= i
	return total
print(func(4))  #24

# 方法2:普通递归
# 规律: 5! = 5*4! 4! = 4*3!
def func(n):
	if n == 1:  #1 递归终止条件
		return n #2 返回参数1
	else:
		return func(n-1) * n  #3 return 函数调自己(参数递减的规律  第一个参数-1)  累乘的规律
print(func(4))  #24
print('--------------------4')

# 5用尾递归实现n的阶乘,简述整个执行过程
# 规律: 5! = 5*4! 4! = 4*3!
def func(n,endval=1):
	if n == 1:   #1 递归终止条件
		return endval  #2 返回参数1 尾递归 最后要的值
	else:
		return func(n-1,endval*n)  #3 return 函数调自己(参数递减的规律  第一个参数-1)  累乘的规律
print(func(4))
print('--------------------5')

# 6斐波那契数列递归实现,简述整个执行过程
# 规律 1 1 2 3 5 8 13...
#方法1 普通递归
def func(n):	 #n表示数列第几个数
	if n in (1,2): #1 递归的结束条件
		return 1   #2 #2 返回参数(唯一)或者固定值
	else:
		return func(n-1) + func(n-2)  #3 return 函数调自己(参数递减的规律  参数-1)  
print(func(4))  #3
print('--------------------6-1')

#方法2 普通实现
def func(n):
	a,b = 0,1
	for i in range(n):
		# print(b)
		yield b    #最后需要的结果存在这里
		a,b = b,a+b
# print(func(4))
gen = func(4)
print(list(gen))  #[1, 1, 2, 3]
print('--------------------6-2')

#方法3 尾递归 (3个参数,基于普通实现来改造)
def func(n,a=0,b=1):
	if n == 1:
		return b  #最后需要的结果存在这里 b
	else:
		return func(n-1,b,a+b)
print(func(4)) #3
print('--------------------6-3')

# 7谈一谈你对递归的理解
	# 1 必须有递归终止条件
	# 2  去-递的过程,不断在开辟新的栈帧空间
	#     回-归的过程,不断在释放空间
	# 3  触发归的2个条件
	#    1.代码执行完了
	#    2.return 向上返回调用处
	# 4 普通递归  return后面是表达式.一般是一个参数
	#   尾递归    return后面不是表达式,而是函数本身,一般是2,3个参数,最终返回的是参数
	#             归的时候,第一层和最后一层的结果是一致的.所以只需要考虑去的过程

# [linux]
# 相对于当前目录切换 cd.
# 相对于上一级切换目录 cd..
# 切换家目录  cd ~
# 回到上一个你操作的那一个目录 cd ..
# 查看的当前路径所在位置 pwd
# 以列表形式查看文件夹里的文件 ls -l
# 查看所有文件包括隐藏文件 ls -a
# 创建文件夹ceshi1     mkdir ceshi1
# 创建文件lianxi2		touch lianxi2
# 创建链接lianjie3     ln -s /home/wangtongpei/mywork/001.txt /home/wangtongpei/mywork/c
					# ln -s 软链接的实际指向  软链接的存放路径 必须是绝对路径
					# 软链接的名字是001.txt -> /home/wangtongpei/mywork/001.txt*
					# lrwxrwxrwx 1 wangtongpei wangtongpei   32 10月 11 19:15 001.txt -> /home/wangtongpei/mywork/001.txt*
					# wangtongpei@wangtongpei-virtual-machine:~/mywork/c$ pwd
					# /home/wangtongpei/mywork/c

# 剪切文件/文件夹   move 001.txt 001/  剪切文件
			    # wangtongpei@wangtongpei-virtual-machine:~/mywork$ mv 3.txt a3/03.txt   剪切并改名
				#   move 001/  002/    剪切文件夹
# mv   从哪个路径  到哪个路径
# mv 123.py ../ceshi300  相对 (剪切)
# mv /home/wangwen/ceshi100/abc.php /home/wangwen/ceshi300/abcccccccc.php 绝对 (剪切并改名)				
				
# 复制文件/文件夹   cp 001.txt 001/   复制文件  可以复制并改名
				#   cp -r 001 002/   复制文件夹 内容
				#   cp -a 001 002/   复制文件夹 内容 权限 修改时间

# 删除文件/文件夹   rm -rf 
# 查看文件的方式有几种?  more cat head tail nano

# 描述下列目录的作用:
# /bin   
# /boot  
# /cdrom 
# /dev   
# /etc   
# /home  
# /lib  
# /lib64
# /lost+found 
# /media
# /mnt   
# /opt   
# /proc  
# /root  
# /run   
# /sbin  
# /srv   
# /sys   
# /tmp   
# /usr   
# /var   
































