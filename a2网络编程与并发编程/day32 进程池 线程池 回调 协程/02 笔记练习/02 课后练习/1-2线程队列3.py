# ### 线程队列

from queue import Queue

# put 存放 超出队列长度阻塞
# get 获取 超出队列长度阻塞
# put_nowait 存放,超出队列长度报错
# get_nowait 获取,超出队列长度报错


# (1) Queue 
# """先进先出,后进后出"""
q = Queue()
q.put(100)
q.put(200)
print(q.get())  #100
print(q.get())  #200
# print(q.get())  #阻塞

# print(q.get_nowait())  #报错
#queue.Empty  
print('-----------1') 

# Queue(3)  =>  指定队列长度, 元素个数只能是3个;
q2 = Queue(3)
q2.put(1000)
q2.put(2000)
q2.put(3000)
# q2.put(4000)  #阻塞

# q2.put_nowait(6000) #报错
# queue.Full

# (2) LifoQueue 
# """先进后出,后进先出(栈的特点)"""
from queue import LifoQueue
lq = LifoQueue()
lq.put(100)
lq.put(102)
lq.put(103)

print(lq.get())
print(lq.get())
print(lq.get())
# print(lq.get())  #阻塞
# 103
# 102
# 100
print('-----------2') 

# (3) PriorityQueue
# """按照优先级顺序进行排序存放(默认从小到大)"""
# """在一个优先级队列中,要放同一类型的数据,不能混合使用"""
from queue import PriorityQueue
pq = PriorityQueue()

# 1.对数字进行排序
pq.put(100)
pq.put(19)
pq.put(-90)
pq.put(88)

print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
# print(pq.get())  #阻塞

# -90
# 19
# 88
# 100
print('-----------3-1')

# 2.对字母进行排序 (按照ascii编码)
pq.put('wangwen')
pq.put('sunjian')
pq.put('wangwei')

print(pq.get())
print(pq.get())
print(pq.get())
# print(pq.get())  #阻塞

# sunjian
# wangwei
# wangwen
print('-----------3-2')


# 3.对容器进行排序
pq.put((22,"wangwen"))
pq.put((67,"wangyuhan"))
pq.put((3,"anxiaodong"))
pq.put((3,"liuyubo"))
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
# print(pq.get())  #阻塞

# (3, 'anxiaodong')
# (3, 'liuyubo')
# (22, 'wangwen')
# (67, 'wangyuhan')

# 4.注意点
# pq.put(100)
# pq.put("nihao")  #TypeError: '<' not supported between instances of 'str' and 'int'
# pq.put((1,2,3))
# """在一个优先级队列中,要放同一类型的数据,不能混合使用"""






























