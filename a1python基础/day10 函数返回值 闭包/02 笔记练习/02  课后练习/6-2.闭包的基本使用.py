# 1 闭包的基本语法形式
def zsy_family():
	father = '马云'
	def hobby():
		print('我不看重钱,这是{}说的'.format(father))
		# print('我不看重钱,这是{:s}说的'.format(father))  #和上面行等效
	return hobby
	
func = zsy_family()
func()  #我不看重钱,这是马云说的

tup = func.__closure__  #如果tup不是空,说明是闭包
print(tup)
# (<cell at 0x7ffa234bfca8: str object at 0x7ffa23473030>,)

print(tup[0].cell_contents)
# 打印延长生命周期的局部变量的值
# 马云

# 2.闭包的复杂形式
def zwl_family():
	gege = '王思聪'
	didi = '高振宁'
	money = 1000
	
	def gege_hobby():
		nonlocal money
		money -= 500
		print('钱还剩下{}'.format(money))
	
	def didi_hobby():
		nonlocal money
		money -= 400
		print('钱还剩下{}'.format(money))
		
	def big_master():
		return [gege_hobby,didi_hobby]
		##内函数名本身gege_hobby,didi_hobby 就是局部变量
		
	return big_master
	
func = zwl_family()
print(func)  
#<function zwl_family.<locals>.big_master at 0x7f6242bc2378>
lst = func()
print(lst)
# [<function zwl_family.<locals>.gege_hobby at 0x7f6487d57268>, <function zwl_family.<locals>.didi_hobby at 0x7f6487d572f0>]

# 获取哥哥函数
gege = lst[0]
gege()  #钱还剩下500

# 获取弟弟函数
didi = lst[1]
didi()  #钱还剩下100

# 判断闭包
tup = func.__closure__
print(tup)
#(<cell at 0x7fb0fa4c3cd8: function object at 0x7fb0fa45f2f0>, <cell at 0x7fb0fa4c3d08: function object at 0x7fb0fa45f268>)

func1 = tup[0].cell_contents
print(func1.__closure__[0].cell_contents)  #100
func1()  #钱还剩下-300

func2 = tup[1].cell_contents
print(func2.__closure__[0].cell_contents)  #-300
























