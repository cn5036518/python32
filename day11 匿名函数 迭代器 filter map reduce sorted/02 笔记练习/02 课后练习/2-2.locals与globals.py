# ### local 与 globals 使用  (了解)

# 一.locals 获取当前作用域所有的变量  返回是字典
# 1 全局空间

def func():
	a1 = 1
	b2 = 2

a = 1
b = 2
res = locals()
c = 3
print(res)  #locals 在函数外 , 获取的是打印之前所有的全局变量
# 'a': 1, 'b': 2, 'res': {...}, 'c': 3}
d = 4 


# 2 局部空间
a = 1
b = 2
def func():
	a1 = 1
	b2 = 2
	res = locals()
	c3 = 3
	print(res)  #{'b2': 2, 'a1': 1}
	# # locals 在函数内 , 获取的是调用之前所有的局部变量
	d4 = 4
c = 3
func()
d = 4

# 二.globals 只获取全局空间的全局变量 返回的是字典
# 1.全局空间
def func():
	a1 = 1
	b2 = 2
	
a = 1
b = 2 
res = globals()
c = 3 
print(res) #'a': 1, 'b': 2, 'res': {...}, 'c': 3, 'd': 4} py3.6.12
# globals 在函数外 , 获取的是所有的全局变量              py3.6.12 及其以上


# 2 .局部空间
a = 1
b = 2
def func():
	a1 = 1
	b2 = 2
	res = globals()
	c3 = 3
	print(res) #'a': 1, 'b': 2, 'res': {...}, 'c': 3, 'd': 4}
	d4 = 4
c = 3
func()
d = 4
# globals 在函数内 , 获取的是所有的全局变量              py3.6.12 及其以上
print('--------------2.2')

# ### globals #
# 如何用字符串创建单个全局变量
dic = globals()
print(dic)
#'a': 1, 'b': 2, 'res': {...}, 'c': 3, 'd': 4, 'dic': {...}}

dic['wangwen'] = '18岁'
print(wangwen) # 18岁  变量wangwen 两边不需要引号
print(dic)
# 'a': 1, 'b': 2, 'res': {...}, 'c': 3, 'd': 4, 'dic': {...}, 'wangwen': '18岁'}

# 如何用字符串批量创建全局变量
def func():
	dic = globals()
	for i in range(1,5):
		#批量在dic当中添加键值对,以创建全局变量
		k ='a'+str(i)
		dic[k] = i
		# dic["a1"] = 1
		# dic["a2"] = 2
		# dic["a3"] = 3
		# dic["a4"] = 4
func()
print(a1,a2,a3,a4)  #1 2 3 4
#  注意:变量a1,a2,a3,a4 两边都不需要引号




































