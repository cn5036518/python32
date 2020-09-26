# ### 生成器
# 生成器本质是迭代器,允许自定义逻辑的迭代器

# 迭代器和生成器的区别
	# 迭代器本身是系统内置的,重写不了
	# 生成器是用户自定义的,可以重写迭代逻辑
	
# 生成器可以用两种方式创建
	# 1 生成器表达式  (里面是元组推导式,外面用小括号)
	# 2 生成器函数	 (用def定义,里面含有yield)

# 1 生成器表达式 (里面是元组推导式,外面用小括号)
gen = (i for i in range(10))
print(gen)  #<generator object <genexpr> at 0x000001D97260B930>

# 判断类型
# from collections import Iterator,Iterable 
from collections.abc import Iterator

print(isinstance(gen,Iterator))  #True

# 1 next 调用生成器
print(next(gen))  #0
print(next(gen))  #1

# ２ for next 调用生成器
for i in range(3):
	print(next(gen)) # 2 3 4
	
# 3 for 调用生成器所有数据
for i in gen:
	print(i)  # 5 6 7 8 9
	
# 4 list强转生成器,瞬间得到所有数据
gen = (i for i in range(10))
print(list(gen))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(next(gen))  #StopIteration



































