# ### import 导入模块
import mymodule1
# """注意点:模块导入时,导入一次,终身受益,并不会重复导入"""

# 1.import导入的基本使用
# (1) 模块.变量
print(mymodule1.cat)  #甜甜

# (2) 模块.函数
mymodule1.jump()  #小猫能上树

# (3) 模块.类
res = mymodule1.Classroom().name
print(res)  #python32

# 2.导入任意模路径下的任意模块
# 默认导入当脚本文件同级目录下的模块等..
# 系统执行流程:首先看一下sys.path里面有没有想要导入的这个模块路径,
# 如果有,默认导入,如果没有,需要手动追加
import sys
print(sys.path)
# ['/mnt/hgfs/ubuntu_gx/python32/day19/import_bao1',
 # '/mnt/hgfs/ubuntu_gx/python32', 
 # '/usr/lib/python36.zip', 
 # '/usr/lib/python3.6',
 # '/usr/lib/python3.6/lib-dynload', 
 # '/usr/local/lib/python3.6/dist-packages',
 # '/usr/lib/python3/dist-packages']

#导入绝对路径  是导入路径,而不是路径后面+py文件名
# sys.path.append(r'C:\Users\Administrator\Desktop\ubuntu_gx\python32\day13 递归 ubuntu环境') #win下
sys.path.append(r'/mnt/hgfs/ubuntu_gx/python32/day13 递归 ubuntu环境') #linux

import mymodule2
print(mymodule2.bird) #小鸟

# 3.from .. import .. 基本使用
# """from .. 从哪里 import .. 引入具体的某个成员"""

# 导入单个成员
from mymodule1 import dog
print(dog)  #旺财

# 导入多个成员
from mymodule1 import jump,lookdoor
jump()  #小猫能上树
lookdoor() #小狗能看门

# 导入所有成员 *导入所有
from mymodule1 import *
print(dog)  #旺财
print(cat)  #甜甜

# 设置引入成员的别名 as
from mymodule1 import cat as c,lookdoor as ld
print(c) #甜甜
ld() #小狗能看门

# 4.__name__的使用
# """
# 返回模块名字的魔术属性 __name__
    # 如果当前文件是直接运行的,返回"__main__"字符串
    # 如果当前文件是间接导入的,返回当前文件名(模块名)
# """

res = __name__
print(res,type(res))
#__main__ <class 'str'>




























