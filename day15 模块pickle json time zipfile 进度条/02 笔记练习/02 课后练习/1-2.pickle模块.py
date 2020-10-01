#  ### pickle 序列化/反序列化模块
import pickle


# with open("lianxi1.txt",mode="w",encoding="utf-8") as fp:
# 	fp.write(1
	# TypeError: write() argument must be str, not int

# dumps 
lst = [1,2]
res = pickle.dumps(lst)
print(res,type(res))  #b'\x80\x03]q\x00(K\x01K\x02e.' <class 'bytes'>

# def func():
# 	print('我是func函数')
# res = pickle.dumps(func)
# print(res,type(res))
# # b'\x80\x03c__main__\nfunc\nq\x00.' <class 'bytes'>
#
# it = iter(range(3))
# res = pickle.dumps(it)
# print(res,type(res))
# b'\x80\x03cbuiltins\niter\nq\x00cbuiltins\nrange\nq
# \x01K\x00K\x03K\x01\x87q\x02Rq\x03\x85q\x04Rq\x05K\x00b.' <class 'bytes'>

# loads 
res2 = pickle.loads(res)
print(res2,type(res2))
# [1, 2] <class 'list'>


# dump 
lst = [1,2]
with open('lianxi.txt',mode='wb') as fp:
	pickle.dump(lst,fp)

# load 
with open('lianxi.txt',mode='rb') as fp:
	res2 = pickle.load(fp)
print(res2,type(res2))
# [1, 2] <class 'list'>


# dumps 和 loads 对文件进行写入读取字节流操作
# 写入字节流
lst = [1,2]
with open('lianxi2.txt',mode='wb') as fp:
	res1 = pickle.dumps(lst)
	print(res1)  #b'\x80\x03]q\x00(K\x01K\x02e.'
	fp.write(res1)

# 读取字节流
with open('lianxi.txt',mode='rb') as fp:
	bytes_str = fp.read()
	print(bytes_str) # b'\x80\x03]q\x00(K\x01K\x02e.'
	res = pickle.loads(bytes_str)
print(res2,type(res2)) # [1, 2] <class 'list'>
print('-------------------1')

# 小结:
lst = [1,2,3]
#dumps 把任意对象序列化成一个bytes
res = pickle.dumps(lst)
print(res , type(res))

#loads 把任意bytes反序列化成原来数据
res2 = pickle.loads(res)
print(res2 , type(res2))

#dump  把对象序列化后写入到file-like Object(即文件对象)
lst = [1,2,3]
with open("lianxi1.txt",mode="wb") as fp:
	pickle.dump(lst,fp)

#load  把file-like Object(即文件对象)中的内容拿出来,反序列化成原来数据
with open("lianxi1.txt",mode="rb") as fp:
	res2 = pickle.load(fp)
print(res2 , type(res2))





























