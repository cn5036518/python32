# class Person():
	# def __init__(self,gun):
		# self.gun = gun
		
	# def fill(self,bullet_num):
		# self.gun.bulletbox.bullet_count += bullet_num
		# print('你本次新加了{}发子弹,剩余的子弹总数是{}发'.format(bullet_num,self.gun.bulletbox.bullet_count))
		
	# def fire(self,fire_count):
		# self.gun.shoot(fire_count)

class Police():
	def __init__(self,name,life,weapon,gender):
		self.name = name
		self.life = life
		self.weapon = weapon
		self.gender = gender
		
	def attack(self,fire_count,terrorist):
		terrorist.life -= fire_count  #第一次攻击
		# terrorist.life -= fire_count  #第二次攻击
		
		# terrorist.diaoxue(fire_count)  #第一次攻击
		# terrorist.diaoxue(fire_count)  #第二次攻击
		print('警察{}对恐怖分子{}发起攻击,恐怖分子掉血{},还剩余{}血'.format(self.name,terrorist.name,fire_count,terrorist.life))
		

class Terrorist():
	def __init__(self,name,life,weapon,gender):
		self.name = name
		self.life = life
		self.weapon = weapon
		self.gender = gender
		
	def attack(self,fire_count,police):
		police.life -= fire_count  #第一次攻击
		# police.life -= fire_count  #第二次攻击
		print('恐怖分子{}对警察{}发起攻击,警察掉血{},还剩余{}血'.format(self.name,police.name,fire_count,police.life))
		
	# def diaoxue(self,fire_count):
		# self.life -= fire_count
	

p1 = Police('jack',100,'ak47','man')
t1 = Terrorist('tom',100,'ak46','man')
p1.attack(10,t1)
p1.attack(11,t1)

t1.attack(10,p1)
t1.attack(11,p1)





















