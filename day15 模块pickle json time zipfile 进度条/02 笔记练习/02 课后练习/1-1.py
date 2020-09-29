# ### pickle 序列化模块
import pickle
# 序列化: 把不能够直接存储在文件中的数据(6大标准数据类型 函数 迭代器等)变得可存储
# 反序列化:把存储在文化中的数据拿出来恢复成原来的数据类型
#
# 文件中只能写入字符串或者字节流bytes

lst = [1,2,3]
# 错误案例,文件不能直接存储容器类型
# with open("lianxi1.txt",mode="w",encoding="utf-8") as fp:
# 	fp.write(1)
	#TypeError: write() argument must be str, not int

# dumps 把任意对象序列化成一个bytes
res = pickle.dumps(lst)
print(res,type(res))
# b'\x80\x03]q\x00(K\x01K\x02K\x03e.' <class 'bytes'>

# 函数可以序列化么? 可以
def func():
	print('我是func函数')
res = pickle.dumps(func)
print(res,type(res))
# b'\x80\x03c__main__\nfunc\nq\x00.' <class 'bytes'>

# 迭代器可以序列化么?
it = iter(range(3))
res = pickle.dumps(it)
print(res,type(res))
#b'\x80\x03cbuiltins\niter\nq\x00cbuiltins\nrange\nq\x01K
# \x00K\x03K\x01\x87q\x02Rq\x03\x85q\x04Rq\x05K\x00b.' <class 'bytes'>
print('--------------1')

# loads 把任意bytes反序列化成原来的数据
res2 = pickle.loads(res)
print(res2,type(res2))
#<range_iterator object at 0x7f84d9f4bf90> <class 'range_iterator'>


# dump 把对象序列化后写入到file-like object(即文件对象)
lst = [1,2,3]
with open("lianxi1.txt",mode="wb") as fp:
	pickle.dump(lst,fp)
	
# load 把file-like object(即文件对象)中的内容拿出来,反序列化成原来的数据
with open('lianxi1.txt',mode='rb') as fp:
	res2 = pickle.load(fp)
print(res2,type(res2))  #[1, 2, 3] <class 'list'>

# dumps和loads 对文件进行写入读取字节流操作
# 写入字节流
lst = [1,2,3]
with open("lianxi2.txt",mode="wb+") as fp:
	res1 = pickle.dumps(lst)
	fp.write(res1)

# 读取字节流
with open("lianxi2.txt",mode="rb+") as fp:
	bytes_str = fp.read()
	res = pickle.loads(bytes_str)
print(res2,type(res2)) #[1, 2, 3] <class 'list'>














































