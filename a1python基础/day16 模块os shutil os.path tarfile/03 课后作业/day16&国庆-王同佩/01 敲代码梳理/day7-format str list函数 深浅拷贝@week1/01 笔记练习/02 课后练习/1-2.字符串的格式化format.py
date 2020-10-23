# ### 字符串的格式化format
# (1)顺序传参
strvar = '{}向{}开了一枪'.format('赵沈阳','许保张')
print(strvar) #赵沈阳向许保张开了一枪

# 2 索引传参
strvar = '{1}向{0}开了一枪'.format('赵沈阳','许保张')
print(strvar) #许保张向赵沈阳开了一枪

# 3 关键字传参
strvar = '{who1}摸了{who2}一下'.format(who1='王伟',who2='马春妮')
print(strvar) #王伟摸了马春妮一下

# 4 容器类型数据(列表或元组)传参
# 方法一
strvar = '{0[0]}摸了{1[0]}一下'.format(['杨源涛'],('王雨涵',))
print(strvar) #杨源涛摸了王雨涵一下

# 方法二(推荐)
strvar = '{group1[0]}摸了{group2[0]}一下'.format(group1=['杨源涛'],group2=('王雨涵',))
print(strvar) #杨源涛摸了王雨涵一下

# 方法三(推荐) 注意一.如果该容器是字典,通过键取值时,不需要加引号  
#注意二.通过下标取值时,不能使用负号(逆向索引)
strvar = '{group1[zsc]}摸了{group2[0]}一下'.format(group1={'zsc':'赵世超'},group2=('王雨涵',))
print(strvar)  #赵世超摸了王雨涵一下

























