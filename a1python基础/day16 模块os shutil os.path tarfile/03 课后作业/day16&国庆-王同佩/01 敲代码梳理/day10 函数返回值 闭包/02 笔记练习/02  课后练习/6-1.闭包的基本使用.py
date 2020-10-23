# ### 闭包函数
# 互相嵌套的两个函数,如果内函数使用了外函数的局部变量
# 并且外函数把内函数返回出来的过程,叫做闭包
# 里面的内函数叫做闭包函数

# 是不是闭包?
# 1 内函数用了外函数的局部变量
# 2 外函数返回内函数

# 1.基本语法形式
def zhaoshenyang_family():
	father = '马云'
	def hobby():
		print('我不看重钱,这是我爸爸{}说的'.format(father))
	return hobby

func = zhaoshenyang_family()
func()  #hobby()  #我不看重钱,这是我爸爸马云说的

tup = func.__closure__
print(tup) #这里不是空,就是闭包   #判断闭包
#(<cell at 0x000002D916961888: str object at 0x000002D916942870>,)
print(tup[0].cell_contents)  #马云 #获取延长生命周期的局部变量
# 局部变量本来是函数调用完毕或是,内存就回收的
print('----------------------1')

# 2.闭包的复杂形式
def zhaowanli_family():
	gege = '王思聪'
	didi = '高振宁'
	money = 1000
	
	def gege_hobby():  #闭包函数1
	# 该内函数使用了局部变量money
		nonlocal money  #修改最近一层的局部变量的值
		money -= 500
		print('钱还剩下{}'.format(money))
		
	def didi_hobby():#闭包函数2
	# 该内函数使用了局部变量money
		nonlocal money
		money -= 400
		print('钱还剩下{}'.format(money))

	def big_master():  #闭包函数3
	# 因为该内函数使用了外函数的局部变量(gege_hobby,didi_hobby)
		return [gege_hobby,didi_hobby]
		#函数名也是变量
		#内函数的函数名 也是局部变量
		
	return big_master
	#返回内函数

func = zhaowanli_family()
print(func)  #big_master这个函数对象
#<function zhaowanli_family.<locals>.big_master at 0x00000252558E5E18>

lst  = func()  # big_master()
print(lst)  #打印gege_hobby,didi_hobby这2个函数的对象
#[<function zhaowanli_family.<locals>.gege_hobby at 0x0000021AE7B65D90>, 
# <function zhaowanli_family.<locals>.didi_hobby at 0x0000021AE7B65E18>]

# 获取哥哥函数
gege = lst[0]
gege()   #gege_hobby()  #钱还剩下500

# 获取弟弟函数
didi = lst[1]
didi()  #didi_hobby()  #钱还剩下100

# 小结:局部变量money如果不是在闭包场景,函数调用完了,空间就回收了
# 局部变量money在闭包下,延长生命周期1000-500-400 = 100

# 3.使用 __closure__,  cell_contents 判断闭包
tup = func.__closure__
print(tup)
# (<cell at 0x00000299C28718B8: function object at 0x00000299C28E5D90>, 
#<cell at 0x00000299C28718E8: function object at 0x00000299C28E5950>)
# 如果返回的元组中有数据说明是闭包,如果没有数据,说明不是闭包
# 谁的生命周期被延长就打印谁

# 先获取第一个单元格   cell_contents 获取对象中的内容
func1 = tup[0].cell_contents
print(func1)
#<function zhaowanli_family.<locals>.didi_hobby at 0x000001B2B6525E18>
res = func1.__closure__[0].cell_contents
print(res)  #100

# 打印闭包函数didi_hobby中,生命周期被延长的属性
func1()  #钱还剩下-300   #didi_hobby()  100-400= -300
print('--------------------------3')


# 再获取第二个单元格  cell_contents 获取对象中的内容
func2 = tup[1].cell_contents
print(func2)  
#<function zhaowanli_family.<locals>.gege_hobby at 0x0000027077FC5950>
"""打印闭包函数gege_hobby中,生命周期被延长的属性"""
res = func2.__closure__[0].cell_contents
print(res)  #-300  #money的当前值

func2()  #钱还剩下-800   #gege_hobby()  -300 -500 = -800











































