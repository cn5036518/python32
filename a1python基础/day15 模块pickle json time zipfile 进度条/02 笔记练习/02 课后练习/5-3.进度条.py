# ### 进度条
import time
# """
# [###################################] 100%
# [##############                     ] 40%
# [#############################      ] 80%
# """
# (1) 定义进度条样式
# print('[{:50s}]'.format('#'))
# [#                                                 ]

# print('[{:50s}]'.format('##############'))
# [##############                                    ]

# print('[{:50s}]'.format('############################'))
# [############################                      ]


# (2) 让进度条动起来
# strvar = ''
# for i in range(50):  #一共50个 # 号
# 	time.sleep(0.1) #延时效果
# 	strvar += '#'   #依次拼接50个 # 号  分50行打印 #如何实现下面行每次覆盖上面行的效果 \r
# 	# print(strvar)
# 	# print('[{:50s}]'.format(strvar))  #加上[]和50个占位符
# 	# print('[{:50s}]'.format(strvar),end='')  #去掉换行
# 	print('\r[{:50s}]'.format(strvar),end='')  #1加上 \r   2去掉换行  关键点  ssy
# 	# \r的作用: 实现\r后面的内容覆盖当前行的行首


# (3) 加上百分比
# 显示进度条
strvar = ''
def process(percent):
	if percent > 1:
		percent = 1
	strvar = int(percent * 50) * '#'  #进度条一共是50个#号
	print('\r[{:50s}] {:.2f}%'.format(strvar,percent*100),end='')

# process(0.25)  #如何让0.25动起来?

# 接受数据
recv_size = 0
total_size = 100
while recv_size <= total_size:
	time.sleep(0.1)
	recv_size += 1
	percent = recv_size/total_size
	process(percent)













































