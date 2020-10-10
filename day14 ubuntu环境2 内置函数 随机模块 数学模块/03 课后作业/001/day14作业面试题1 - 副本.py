# 1.结果
def extendList(val,list=[]):
	print(val)  #'a'
	print(list)  #[]
	list.append(val)
	return list
list1 = extendList(10)
print(list1)   #[10]
list2 = extendList(123 , [])   #列表重新写了
print(list2)  #[123]
list3 = extendList('a')   
print(list3)   #['a']

# 10
# []
# [10]

# 123
# []
# [123]

# a
# [10]  #关键点  list是引用类型,一变都变
# [10, 'a']
print('-------------------1')
















