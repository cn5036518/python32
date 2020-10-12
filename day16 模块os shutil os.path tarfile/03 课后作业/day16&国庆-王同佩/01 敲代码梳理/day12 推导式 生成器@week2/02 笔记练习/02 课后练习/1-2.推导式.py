# ### 推导式

#1 普通写法
lst = []
for i in range(3):
	lst.append(i)
print(lst)  #[0, 1, 2]

#2 改写推导式
lst = [i for i in range(3)]
print(lst)  #[0, 1, 2]

# 小练习
# 1.[1,2,3,4,5] => [2,4,6,8,10]
lst = [i*2 for i in range(6)]
print(lst) # [0, 2, 4, 6, 8, 10]

# 2.带有判断条件的推导式
#注意点:for后面紧跟的判断条件只能是单项分支.只有if,不能有else
# [1,2,3,4,5,6,7,8,9,10] => [1,3,5,7,9 ... ]
# 普通写法
lst = [1,2,3,4,5,6,7,8,9,10]
lst_new = []
for i in lst:
	if i % 2 == 1:
		lst_new.append(i)
print(lst_new)  #[1, 3, 5, 7, 9]

# 推导式
lst_new = [i for i in lst if i % 2 == 1]
print(lst_new)  #[1, 3, 5, 7, 9]
print('---------------------------2')

# 列表推导式 [三元运算符 + 推导式]  了解
lst_new = [i if i%2 == 1 else 0 for i in lst]
print(lst_new) #[1, 0, 3, 0, 5, 0, 7, 0, 9, 0]

# 3.多循环推导式 # 谁@谁
lst1 = ["孙杰龙","陈露","曹静怡"]
lst2 = ["王志国","邓鹏","合理"]
# 普通1   3*3 
lst_new = []
for i in lst1:
	for j in lst2:
		lst_new.append(i+'@'+j)
print(lst_new)
# ['孙杰龙@王志国', '孙杰龙@邓鹏', '孙杰龙@合理', '陈露@王志国',
# '陈露@邓鹏', '陈露@合理', '曹静怡@王志国', '曹静怡@邓鹏', '曹静怡@合理']

# 推导式1
lst = [i+'@'+j for i in lst1 for j in lst2 ]
print(lst)

## 4.带有判断条件的多循环推导式
# 普通2   1*3
lst_new = []
for i in lst1:
	for j in lst2:
		if lst1.index(i) == lst2.index(j):  #取下标 index(i)而不是index[i]
			lst_new.append(i +'@'+ j)
print(lst_new)
# ['孙杰龙@王志国', '陈露@邓鹏', '曹静怡@合理']

# 推导式2
lst = [i+'@'+j for i in lst1 for j in lst2 if lst1.index(i)== lst2.index(j)]
print(lst)
# ['孙杰龙@王志国', '陈露@邓鹏', '曹静怡@合理']



























