# 改写推导式
# [val for i in iterable]

# 1.[1,2,3,4,5] => [2,4,6,8,10]
lst = [1,2,3,4,5]
lst_new = [i*2 for i in lst]
print(lst_new)  #[2, 4, 6, 8, 10]

# 2.带有判断条件的推导式
# """注意点:for后面紧跟的判断条件只能是单项分支.只有if,不能有else"""
# """[1,2,3,4,5,6,7,8,9,10] => [1,3,5,7,9 ... ]"""
lst = [1,2,3,4,5,6,7,8,9,10]
lst_new =[i for i in lst if  i % 2 == 1]
print(lst_new) #[1, 3, 5, 7, 9]

#方法2
lst_new =[lst[i] for i in range(0,len(lst),2)]
print(lst_new)  #[1, 3, 5, 7, 9]

# 3.多循环推导式 # 谁*谁  3*3
lst1 = ["孙杰龙","陈露","曹静怡"]
lst2 = ["王志国","邓鹏","合理"]
lst_new = [i+'*'+j for i in lst1 for j in lst2]
print(lst_new)
#['孙杰龙*王志国', '孙杰龙*邓鹏', '孙杰龙*合理', '陈露*王志国', '陈露*邓鹏', '陈露*合理', '曹静怡*王志国', '曹静怡*邓鹏', '曹静怡*合理']

# 4.带有判断条件的多循环推导式 3个一对一
lst1 = ["孙杰龙","陈露","曹静怡"]
lst2 = ["王志国","邓鹏","合理"]
lst_new = [i+'*'+j for i in lst1 for j in lst2 if lst1.index(i)== lst2.index(j)]
#AttributeError: 'list' object has no attribute 'find'
print(lst_new)
#['孙杰龙*王志国', '陈露*邓鹏', '曹静怡*合理']








































