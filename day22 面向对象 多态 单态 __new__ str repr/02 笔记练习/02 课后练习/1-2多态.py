# ### 多态: 不同的子类对象调用相同的父类方法,得到不同的执行结果
# 继承  --子类和父类
# 重写  
	# 调用方:不同的对象.
	# 方法:相同的父类方法
	# 返回:不同的结果 

class Soldier():
	def attack(self):
		pass
	
	def back(self):
		pass
		
# 陆军
class Army(Soldier):
	def attack(self):
		print('[陆军]进攻')

	def back(self):
		print('[陆军]撤退')

# 海军
class Navy(Soldier):
	def attack(self):
		print('[海军]进攻')

	def back(self):
		print('[海军]撤退')

# 空军
class AirForce(Soldier):
	def attack(self):
		print('[空军]进攻')
		
	def back(self):
		print('[空军]撤退')

#创建士兵
obj1 = Army()
obj2 = Navy()
obj3 = AirForce()

lst = [obj1,obj2,obj3] #三个对象放在列表中

strvar = '''
将军请下令:
1.全体出击
2.全体撤退
3.海军上,其他兵种撤退
'''

num = input(strvar)
for i in lst:
	# print(i)
	# <__main__.Army object at 0x7f0bfbfdc908>
# <__main__.Navy object at 0x7f0bfbfdc940>
# <__main__.AirForce object at 0x7f0bfbfdc978>
	if num == '1':
		i.attack()
			# [陆军]进攻
			# [海军]进攻
			# [空军]进攻
	elif num == '2':
		i.back()
		# [陆军]撤退
		# [海军]撤退
		# [空军]撤退
	elif num == '3':
		if isinstance(i,Navy):
			i.attack()
		else:
			i.back()
		# [陆军]撤退
		# [海军]进攻
		# [空军]撤退
	else:
		print('我没听见')
		break  #不加这个,上面行会打印3次


























