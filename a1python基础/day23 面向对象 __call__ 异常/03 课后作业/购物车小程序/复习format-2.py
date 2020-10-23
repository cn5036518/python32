# ### 复习format

#1 指定传的参数类型必须是字符串   {:s}
strvar = "{:s}在吃东西"
res = strvar.format("赵沈阳")
print(res) #赵沈阳在吃东西

# 2关键字传参   {who}
strvar = '{who}在吃东西'
res = strvar.format(who='赵万里')
print(res) #赵万里在吃东西

# 3关键字传参 + 字符串类型 {who:s}
strvar = '{who:s}在吃东西'.format(who='刘玉波')
print(strvar)
#刘玉波在吃东西

# 4 容器类型传参  {dic[lyb]:s}  字典的键不加引号
strvar = '{dic[lyb]:s}在吃东西'.format(dic = {'lyb':'刘玉波'})
print(strvar)
#刘玉波在吃东西

# 5 容器类型传参 + 填充符号 + 指定类型  {dic[zwb]:*^10s}
strvar = '{dic[zwb]:*^10s}在吃东西'.format(dic={'zwb':'刘文波'})
print(strvar)
#***刘文波****在吃东西

# 6 容器类型传参 + 填充符号   {dic[zwb]:*^10}
strvar = '{dic[zwb]:*^10}'.format(dic={'zwb':'刘文波'})
print(strvar)
#***刘文波****

#7 容器类型传参 + 默认填充空格
strvar = '{dic[zwb]:^10}在吃东西'.format(dic={'zwb':'刘文波'})
print(strvar)
#   刘文波    在吃东西



















