#  需求分析:

"""
弹夹类: 属性: 子弹数量 方法没有, 参数也没有

枪类 : 属性: 弹夹对象  方法: 射击  参数: 射击的次数

人类 : 属性: 枪对象, 方法: 1 上子弹, (上多少子弹的参数,)连贯调用弹夹的属性子弹,进行添加 2 开火; 参数(开火的次数) 间接调用gun的shoot方法!


"""
from package.danjia import DanJia
from package.gun import Gun
from package.peoson import Peoson

# 实例化出对象

d = DanJia()
g = Gun(d)
p = Peoson(g)

if __name__ == '__main__':
   p.fire(5)
   p.add_zi(7)
   p.fire(20) # 大了10发子弹,还有一个打不出来