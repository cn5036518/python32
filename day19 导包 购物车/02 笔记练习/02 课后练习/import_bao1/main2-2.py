# ### import 导入包

# 文件夹:包  文件:模块(py文件)
# 当引入包时,会自动指定包中__init__.py的初始化文件,对包进行初始化

# 1.import引入包的语法
# import package1
# 导入包的属性
# print(package1.ceshi1)  #改变量ceshi1在包package1里的__init__.py定义了
# 初始化文件被执行 ... 
# ceshi1

# 导入包下的某个模块
# 方法一  包.模块
# import package1.mywork
# package1.mywork.myjoin()  #这是myjoin方法
# 包.模块.函数()
# mywork.myjoin()  #NameError: name 'mywork' is not defined

# 方法二 as 别名
# import package1.mywork as pm
# pm.myjoin()  #这是myjoin方法

# 方法三 把要引入的模块放到初始化文件当中进行引入,简化操作
# import package1
# """os.path.getsize()"""
# 这就是我们只导入了包os,没有导入模块path,却可以使用os.path的原因
# 因为os包的__init__文件 写了from os import path
# package1.mywork.mygetsize()
# package1包中的__init__ 写了from package1 import mywork

# 2.from .. import .. 引入包中具体的成员的语法
# 01引入包中的属性
# from package1 import ceshi2
# print(ceshi2)#ceshi2
# package1包中的__init__ 写了ceshi2 = "ceshi2"

# 02可以指定*号的范围 用__all__可以限定*号的范围
# as起别名
# from package1 import ceshi3 as c3
# from package1 import cesh12 as c2,ceshi1 as c1
# print(c3)  #ceshi3
# print(c1) error
# print(c2) error
#ImportError: cannot import name 'cesh12'  
#原因是package1包中的__init__ 写了__all__ = ["ceshi3"]

# 03引入包中的模块
# from 包名 import 模块
# from package1 import mywork
# mywork.myjoin() #模块.函数()
#这是myjoin方法

# 04引入包中模块下的成员
# from package1.mywork import mygetsize
#  from 包.模块 import 函数
# mygetsize()
#这是mygetsize方法

import sys
sys.path.append(r'/mnt/hgfs/ubuntu_gx/python32/day19/import_bao1/package2/pkg2')
print(sys.path)

# 3.单入口模式
# """这里使用相对路径进行导入  也可以使用绝对路径"""
import package2.pkg1.pkg1_m2 as ppp2
# import 包1.子包.模块 as 别名
print(ppp2.ceshi100)  #ceshi100




# 单入口模式
# 1 main.py导入同级目录001下的文件001.txt
# 2 001.txt文件中导入同级目录的文件002.txt
  # 单入口文件之外的其他文件之间的导入,必须使用相对路径,使用sys.path的绝对路径是不行的
  # 相对路径的注意点:
  # 1 在001.txt中用相对路径引入002.txt后,只能在main.py
     # 中执行才行(所以叫单入口模式),如果直接在001.py中
	 # 运行代码,相对路径的引入会报错











































