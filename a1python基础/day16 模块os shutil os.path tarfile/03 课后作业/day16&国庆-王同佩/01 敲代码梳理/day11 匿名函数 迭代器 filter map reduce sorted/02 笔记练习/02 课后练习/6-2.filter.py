# 1.只要列表中所有的偶数
lst = [1,2,34,5,65,6,56,7,56,756,7567,11]

# 普通写法
lst_new = []
for i in lst:
	if i % 2 == 0:
		lst_new.append(i)
print(lst_new)  #[2, 34, 6, 56, 56, 756]

# 方法2 filter
def func(n):
	if n % 2 == 0:
		return True
	
it = filter(func,lst)
print(list(it))  #[2, 34, 6, 56, 56, 756]

it  = filter(lambda n :True if n%2 == 0 else False,lst)
# SyntaxError: invalid syntax   匿名函数中的三元表达式,必须要有eles.否则报错
print(list(it))





































