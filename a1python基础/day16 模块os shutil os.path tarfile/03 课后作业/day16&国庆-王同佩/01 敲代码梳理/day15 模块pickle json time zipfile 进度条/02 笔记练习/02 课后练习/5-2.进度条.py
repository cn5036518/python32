# ### 进度条
import time

# [###################################] 100%
# [##############                     ] 40%
# [#############################      ] 80%

# 思路
# 1 定义进度条样式
# 2 让进度条动起来
# 3 加上百分比

# 1 定义进度条样式
# print('[{:50s}]'.format('#'))
# print('[{:50s}]'.format('######################'))
# print('[{:50s}]'.format('############################################'))

# 2 让进度条动起来
# strvar = ''
# for i in range(50):
	# time.sleep(0.05)
	# strvar += '#'
	# print('\r[{:50s}]'.format(strvar),end='')
	# \r   : 将\r后面的字符串拉到了当前行的行首


# strvar = "还有诗和\r远方的田野"
# print(strvar)  #远方的田野
# strvar = "还有诗和\n远方的\r田野"
# print(strvar)
# 还有诗和
# 田野

# 3 加上百分比
# 显示进度条
def myprocess(percent):
	if percent >1:
		percent = 1
		
	# 打印对应的#号数量
	strvar = int(percent * 50) * '#'
	
	# 进行打印 %%==>%
	print('\r[{:50s}] {:.2f}%'.format(strvar,percent*100),end='')
	# print("\r[%-50s] %d%%" % (strvar , percent * 100) , end="")

# myprocess(0.5)

# 接受数据
recv_size = 0
total_size = 1000
while recv_size < total_size:
	time.sleep(0.02)
	recv_size += 10
	
	percent = recv_size/total_size #0.5
	myprocess(percent)
































