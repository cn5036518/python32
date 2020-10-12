# ### 进度条
import time

# (1) 定义进度条样式
# [###################################] 100%
# print('[{:50s}]'.format('#'))
# [#                                                 ]

# print('[{:50s}]'.format('#############'))
# [#############                                     ]

# print('[{:50s}]'.format('##########################'))
# [##########################                        ]


# (2) 让进度条动起来
# strvar = ''
# for i in range(50):
	# time.sleep(0.1)
	# strvar += '#'
	# print(strvar)
	# print('[{:50s}]'.format(strvar))  # []
	# print('[{:50s}]'.format(strvar),end='')  #不换行
	# print('\r[{:50s}]'.format(strvar),end='')  #\r后面的内容覆盖当前行的行首


# (3) 加上百分比
# 显示进度条
# 先给个固定的百分比:50%
strvar = ''
def process(percent):
	if percent > 1:
		percent = 1
	strvar = int(percent*50) * '#'
	print('\r[{:50s}] {:.2f}%'.format(strvar,percent*100),end='')

# process(0.5)  #如何让percent动起来?即随着接受数据的增多而增大

# 接受数据
receive_size = 0
total_size =100
while receive_size <= total_size:
	time.sleep(1)
	receive_size += 1
	percent = receive_size/total_size
	process(percent)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
