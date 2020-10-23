#  ### 进度条
import time

# [##########################]  100%
# [##########				   ]   40%
# [####################      ]   80%

# 1 定义进度条的样式

# print('[%-50s]' % ('#'))  #50个#的位置,#靠左
# print('[%-50s]' % ('##########'))  #
# print('[%-50s]' % ('####################'))  #

# 2 进度条动起来
# strvar = ''
# for i in range(50):	
	# strvar += '#'
	# print('[%-50s]' % (strvar))

# strvar = ''
# for i in range(50):	
	# time.sleep(0.1)
	# strvar += '#'
	# print('\r[%-50s]' % (strvar),end='')
	# # 这里的\r是将后面的内容截断,覆盖行首的内容

# 3  加上百分比
# 显示进度条
def myprocess(percent):  #参数是进度百分比数字
	if percent > 1:
		percent = 1
	
	# 打印对应的#号数量 * '#' ==> 字符串#号的效果
	strvar = int(percent * 50) * '#'  
	# 根据百分比数字,打印#图形
	
	# 进行打印 %% ==> %
	print('\r[%-50s] %d%%' % (strvar,percent * 100),end='')	


# 接受数据
recv_size = 0
total_size = 100
while recv_size  < total_size:
	time.sleep(0.02)
	recv_size += 1
	percent = recv_size/total_size
	myprocess(percent)

#随着数据的增多,百分比在增多,进度条#的图形在增多








































