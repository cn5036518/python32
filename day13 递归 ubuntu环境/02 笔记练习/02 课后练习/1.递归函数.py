# ### 递归函数
"""
递归函数 : 自己调用自己的函数 , 叫做递归函数
递 : 去
归 : 回
一去一回叫做递归
"""

def digui(n):
    print(n,"<==1==>")
    if n > 0:
        digui(n-1)
    print(n,"<==2==>")

digui(5)

"""
# 去的过程
n = 5 print(5,"<==1==>")  if 5 > 0:   digui(5-1) =>  digui(4) 代码阻塞在第12行
n = 4 print(4,"<==1==>")  if 4 > 0:   digui(4-1) =>  digui(3) 代码阻塞在第12行
n = 3 print(3,"<==1==>")  if 3 > 0:   digui(3-1) =>  digui(2) 代码阻塞在第12行
n = 2 print(2,"<==1==>")  if 2 > 0:   digui(2-1) =>  digui(1) 代码阻塞在第12行
n = 1 print(1,"<==1==>")  if 1 > 0:   digui(1-1) =>  digui(0) 代码阻塞在第12行
n = 0 print(0,"<==1==>")  if 0 > 0: 不成立 print(0,"<==2==>") 到此最后一层函数空间彻底执行完毕

# 回的过程
回到上一层函数空间  n = 1 代码在第12行的位置,继续往下执行  print(1,"<==2==>")
回到上一层函数空间  n = 2 代码在第12行的位置,继续往下执行  print(2,"<==2==>")
回到上一层函数空间  n = 3 代码在第12行的位置,继续往下执行  print(3,"<==2==>")
回到上一层函数空间  n = 4 代码在第12行的位置,继续往下执行  print(4,"<==2==>")
回到上一层函数空间  n = 5 代码在第12行的位置,继续往下执行  print(5,"<==2==>")

到此递归函数执行结束..
打印 543210012345
"""

"""
每次调用函数时,都要单独在内存当中开辟空间,叫做栈帧空间,以运行函数中的代码

递归总结:
	(1)递归实际上是不停的开辟栈帧空间和释放栈帧空间的过程,
		开辟就是去的过程,
		释放就是回的过程
	(2)递归什么时候触发归的过程:
		1.当最后一层栈帧空间执行结束的时候,触发归的过程.
		2.当遇到return返回值的时候终止当前函数,触发归的过程.
	(3)递归不能无限的去开辟空间,可能造成内存溢出,蓝屏死机的情况,所以一定要给予跳出的条件(如果递归的层数太大,不推荐使用)
	(4)开辟的一个个栈帧空间,数据是彼此独立不共享的.
"""


# 递归不能不限开辟空间
"""官方说法最大默认是1000层."""
def deepfunc():
	deepfunc()
deepfunc()


















