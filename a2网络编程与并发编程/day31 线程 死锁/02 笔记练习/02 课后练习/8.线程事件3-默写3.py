# (2) 模拟连接远程数据库
# """最多连接三次,如果三次都连接不上,直接报错."""
from threading import Thread,Event
import time,random

# wait   : 动态加阻塞 (True => 放行  False => 阻塞)
# is_set : 获取内部成员属性值是True 还是 False(默认是False)
# set    : 把False -> True
# clear  : 把True  -> False

e = Event()
print(e.is_set())  #False

# e.wait()
# print("代码执行中 ... ")

e.set()
print(e.is_set())  #True

e.wait()
print("代码执行中 ... ")

e.clear()
print(e.is_set())  #False

# e.wait()
# print("代码执行中 ... ")







































