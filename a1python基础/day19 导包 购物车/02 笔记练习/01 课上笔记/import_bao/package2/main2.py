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
# import package2.pkg1.pkg1_m2 as ppp2
import pkg1.pkg1_m2 as ppp2
# print(package2.pkg1.pkg1_m2.ceshi100)
print(ppp2.ceshi100)

# 单入口模式
# 1 main.py导入同级目录001下的文件001.txt
# 2 001.txt文件中导入同级目录的文件002.txt
  # 单入口文件之外的其他文件之间的导入,必须使用相对路径,使用sys.path的绝对路径是不行的
  # 相对路径的注意点:
  # 1 在001.txt中用相对路径引入002.txt后,只能在main.py
     # 中执行才行(所以叫单入口模式),如果直接在001.py中
	 # 运行代码,相对路径的引入会报错



