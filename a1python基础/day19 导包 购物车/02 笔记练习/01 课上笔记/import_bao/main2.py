# ### import 导入包
"""
文件夹:包  文件:模块
当引入包时,会自动指定包中__init__.py的初始化文件,对包进行初始化
"""

# 1.import引入包的语法
# import package1
# 导入包的属性
# print(package1.ceshi1)

# 导入包下的某个模块
# 方法一
# import package1.mywork
# package1.mywork.myjoin()

# 方法二 as 起别名
# import package1.mywork as pm
# pm.myjoin()

# 方法三 把要引入的模块放到初始化文件当中进行引入,简化操作
# import package1
"""os.path.getsize()"""
# package1.mywork.mygetsize()


# 2.from .. import .. 引入包中具体的成员的语法
# 引入包中的属性
# from package1 import ceshi2
# print(ceshi2)

# 可以指定*号的范围 用__all__
# from package1 import *
# print(ceshi2) error
# print(ceshi3)

# 可以用as起别名
# from package1 import ceshi2 as c2,ceshi1 as c1
# print(c1)
# print(c2)

# 引入包中的模块
# from package1 import mywork
# mywork.myjoin()

# 引入包中模块下的成员
# from package1.mywork import mygetsize
# mygetsize()

# 3.单入口模式
"""使用相对路径进行导入"""
import package2.pkg1.pkg1_m2 as ppp2
# print(package2.pkg1.pkg1_m2.ceshi100)
print(ppp2.ceshi100)

单入口模式  main.py是单入口文件  文件和目录名不能数字开头
一  分模块(非main.py)是同级目录
1 main.py导入同级目录a001下的文件a001.txt
2 a001.txt文件中导入同级目录的文件a002.txt
  相对路径的注意点:
  1 在a001.txt中用相对路径引入a002.txt后,只能在main.py
     中执行才行(所以叫单入口模式),如果直接在a001.py中
	 运行代码,相对路径的引入会报错

二  分模块(非main.py)不是同级目录  main.py和分模块是3层
1 main.py导入同级目录a001下子目录a011下的文件a001.txt    --绝对路径  sys.path.append(r'')
2 a001.txt文件中导入目录a001下子目录a022下的文件a002.txt  --相对路径 .. 或. (这里也可以用绝对路径导入)
可以用相对路径导入
# 找上一级包中的具体某个模块
 from ..a001 import a002

三  分模块(非main.py)不是同级目录  main.py和分模块是2层  main.py a001 a002是同级目录
1 main.py导入同级目录a001下的文件a0011.txt    --绝对路径  sys.path.append(r'')
2 a001.txt文件中导入目录a002下的文件a0022.txt  --相对路径 .. 或. (这里也可以用绝对路径sys.path.append导入)
不能用相对路径导入  
报错是:ValueError: attempted relative import beyond top-level package
 找上一级包中的具体某个模块
 from ..a002 import a0022  #这行报错
报错原因是:从文件a0011.txt往上找一层后,是目录import_bao2,目录import_bao2已经是入口文件main.py的上一层目录了
最多只能是main.py的同级目录.(先记住这个结论,原理先放放,随之学习的深入,或许就明白原理了)
解决办法:
办法1:
	main.py和分模块从2层变成3层,即main.py和分模块a0011.txt之间加一层目录比如a0011,就可以了
办法2:
	a001.txt文件中导入目录a002下的文件a0022.txt  不适用相对路径,改成用绝对路径sys.path.append导入即可






































