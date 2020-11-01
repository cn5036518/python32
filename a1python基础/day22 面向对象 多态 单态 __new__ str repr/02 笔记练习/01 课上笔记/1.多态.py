# ### 多态: 不同的子类对象调用相同的父类方法,得到不同的执行结果
# """继承 重写父类的方法 """
	# 调用方:不同的子类对象.
	# 方法:相同的父类方法
	# 返回:不同的结果 

class Soldier():  #这里父类的方法体是pass
	def attack(self):
		pass
		
	def back(self):
		pass
		
# 陆军
class Army(Soldier):
	def attack(self):
		print("[陆军]开坦克装甲部队,开大炮轰炸敌方根据地,拼刺刀,手撕鬼子")
		
	def back(self):
		print("[陆军]为了一条性命,夜行八百,日行一千,回家")
	
# 海军
class Navy(Soldier):
	def attack(self):
		print("[海军]开航空母舰,扔鱼叉,撒网捆住敌人,收网")
	
	def back(self):
		print("[海军]直接跳水,下海喂鱼,原地爆炸")

# 空军
class AirForce(Soldier):
	def attack(self):
		print("[空军]空对地投放原子弹,空对空发射巡航导弹")
	
	def back(self):
		print("[空军]直接跳机,落地成盒")
	
# 创建士兵
obj1 = Army()
obj2 = Navy()
obj3 = AirForce()

# 
lst = [obj1,obj2,obj3]   #三个军种的对象放入列表
# lst = [Army(),Navy(),AirForce()]

strvar = """
将军请下令:
1.全体出击
2.全体撤退
3.海军上,其他兵种撤退
"""

num = input(strvar)
for i in lst:
	# print(i)
	if num == "1":
		i.attack()  #全体出击
	elif num == "2":
		i.back()  #全体撤退
	elif num == "3":
		if isinstance(i,Navy): #判断对象属于哪个类
			i.attack()  #海军出击
		else:
			i.back()  #其他兵种撤退
	else:
		print("风太大,小弟听不见")
		break












































