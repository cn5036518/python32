# ### 随机模块
import random

# 1 random()   [0,1)
res = random.random()
print(res)  #0.14971658126854637

# 2 randrange()    ***
res = random.randrange(3)
print(res)  #0 1 2 随机取一个

res = random.randrange(0,3)
print(res)  #0 1 2 随机取一个

res = random.randrange(0,4,2)
print(res)  #0  2 随机取一个

res = random.randrange(4,1,-2)
print(res)  #4 2 随机取一个

# 3 randint()  
res = random.randint(1,3)
print(res)  # 1 2 3 随机取一个

# 4 uniform() [0,2)范围内的随机小数  ***
res = random.uniform(0,2)
print(res)  #1.2813945384906544
res = random.uniform(2,0)
print(res)  #1.2185570489756168

# 5 choice()   # 单项选择   **
lst = ["孙凯喜","王永飞","于朝志","须臾间","含税小"]
res = random.choice(lst)
print(res)  #含税小

def mychoice(lst):
	index_num = random.randrange(len(lst))
	return lst[index_num]
print(mychoice(lst))

mychoice = lambda lst:lst[random.randrange(len(lst))]
print(mychoice(lst))

# 6 sample()  # 多项选择  **
tup = ("孙凯喜","王永飞","于朝志","须臾间","含税小")
res = random.sample(tup,2)
print(res)  #['含税小', '王永飞']

# 7 shuffle()  # 随机打乱序列中的值
lst = ["孙凯喜","王永飞","于朝志","须臾间","含税小"]
random.shuffle(lst)
print(lst)

# ### 验证码
def verification_code():
	strvar = ''
	for i in range(4):
		uppercase_letter = chr(random.randrange(65,91))
		lowercase_letter = chr(random.randrange(97,123))
		figure = str(random.randrange(10))
		lst = [uppercase_letter,lowercase_letter,figure]
		strvar += random.choice(lst)
	return strvar
res = verification_code()
print(res) #sCwE





























