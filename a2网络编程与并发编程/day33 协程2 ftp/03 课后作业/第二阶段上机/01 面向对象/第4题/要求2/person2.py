class Person():
	def __init__(self,name,life,weapon,gender):
		self.name = name
		self.life = life
		self.weapon = weapon
		self.gender = gender
		
	def attack(self,fire_count,obj):
		obj.life -= fire_count  #第一次攻击


class Police(Person):
	pass
		
class Terrorist(Person):
	pass

	

p1 = Police('jack',100,'ak47','man')
t1 = Terrorist('tom',100,'ak46','man')
p1.attack(10,t1)
print('警察{}对恐怖分子{}发起攻击,恐怖分子掉血{},还剩余{}血'.format(p1.name,t1.name,10,t1.life))
p1.attack(11,t1)
print('警察{}对恐怖分子{}发起攻击,恐怖分子掉血{},还剩余{}血'.format(p1.name,t1.name,11,t1.life))

t1.attack(10,p1)
print('恐怖分子{}对警察{}发起攻击,警察掉血{},还剩余{}血'.format(t1.name,p1.name,10,p1.life))
t1.attack(11,p1)
print('恐怖分子{}对警察{}发起攻击,警察掉血{},还剩余{}血'.format(t1.name,p1.name,11,p1.life))




















