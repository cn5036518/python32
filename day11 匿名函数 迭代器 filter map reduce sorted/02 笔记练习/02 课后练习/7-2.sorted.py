# sorted

tup = (-90,89,78,3)
# 1.从小到大
lst = sorted(tup)
print(lst)  #[-90, 3, 78, 89]


# 2.从大到小
lst = sorted(tup,reverse=True)
print(lst)  #[89, 78, 3, -90]

# 3.按照绝对值进行排序
lst = sorted(tup,key=abs)
print(lst)  #[3, 78, 89, -90]

# 4.按照自定义函数进行排序
tup = (19,23,42,87)  #按照%10的余数

def func(n):
	return n%10
lst = sorted(tup,key=func)
print(lst)  #[42, 23, 87, 19]









































