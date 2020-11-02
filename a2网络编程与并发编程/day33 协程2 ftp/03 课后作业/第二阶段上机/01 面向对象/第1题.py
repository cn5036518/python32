# 1.两个有序列表，合并后去重且保持有序
# lst1 = [1,3,4,5] , lst2 = [1,2,3,5]
# 输出样例：[1,2,3,4,5]

lst1 = [1,3,4,5] 
lst2 = [1,2,3,5]

# lst2.sort()
# print(lst2)

lst1.extend(lst2)
print(lst1)  #[1, 3, 4, 5, 1, 2, 3, 5]

setvar = set(lst1)
print(setvar)  #{1, 2, 3, 4, 5}

lst3 = list(setvar)
print(lst3)  #[1, 2, 3, 4, 5]

lst3.sort()
print(lst3)  #[1, 2, 3, 4, 5]
 
































