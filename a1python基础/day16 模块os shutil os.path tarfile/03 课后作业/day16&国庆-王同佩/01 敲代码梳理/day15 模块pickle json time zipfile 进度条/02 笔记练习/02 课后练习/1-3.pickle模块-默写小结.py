# ### pickle 序列化/反序列化模块
import pickle
# """
# 序列化:   把不能够直接存储在文件中的数据变得可存储
# 反序列化: 把存储在文件中的数据拿出来恢复成原来的数据类型

# php
	# serialize
	# unserialize

# 把所有的数据类型都通过pickle模块进行序列化	

# 文件不能直接存储容器 , 文件只能存储字符串str和字节流bytes

# lst = [1,2,3]
# with open("lianxi1.txt",mode="w",encoding="utf-8") as fp:
	# fp.write(lst) ##TypeError: write() argument must be str, not list
	# fp.write(1)  #TypeError: write() argument must be str, not int

#01 dumps 
# 把任意对象序列化成一个bytes
# 任意对象包括不限于:6大标准数据类型,函数,迭代器等
lst = [1,2,3]
res = pickle.dumps(lst)
print(res,type(res))
#b'\x80\x03]q\x00(K\x01K\x02K\x03e.' <class 'bytes'>
print('-------------1 dumps')

#函数可以序列化么? 可以
def func():
	print("我是func函数")
res3 = pickle.dumps(func)
print(res3,type(res3))
#b'\x80\x03c__main__\nfunc\nq\x00.' <class 'bytes'>

#迭代器可以序列化么? 可以
it = iter(range(2))
res3 = pickle.dumps(it)
print(res3,type(res3))
#b'\x80\x03cbuiltins\niter\nq\x00cbuiltins\nrange\nq\x01K\x00K\x02K\x01\x87q\x02Rq\x03\x85q\x04Rq\x05K\x00b.' <class 'bytes'>

#02 loads 
# 把任意bytes反序列化成原来数据
res2 = pickle.loads(res)
print(res2)  #[1, 2, 3]
print('-------------2 loads')


#03 dump  
# 把对象序列化后写入到file-like Object(即文件对象)
lst = [1,2,3]
with open('lianxi11.txt',mode='wb') as fp:
	pickle.dump(lst,fp)	  #写入的是bytes
print('-------------3 dump')

#04 load  
# 把file-like Object(即文件对象)中的内容拿出来,反序列化成原来数据
with open('lianxi11.txt',mode='rb') as fp:
	lst = pickle.load(fp) #将之前写入文件的bytes反解成原数据-list
print(lst)
#[1, 2, 3]
print('-------------4 load')


# 05 dumps 和 loads 对文件进行写入读取字节流操作
# 001写入字节流
lst = [1,2,3]
with open('lianxi12.txt','wb') as fp:
	bytesvar = pickle.dumps(lst)# 1 将列表转成bytes
	fp.write(bytesvar)   # 2 写入bytes到文件

# 002读取字节流
with open('lianxi12.txt','rb') as fp:
	bytesvar = fp.read()  #1读取文件中的字节流
	lst = pickle.loads(bytesvar) #2 反解字节流成原数据-list
	print(lst)  #[1, 2, 3]
	
	

#小结默写
#dumps
    # 任意对象==>字节流bytes
lst = [1,2]
bytesvar = pickle.dumps(lst)
print(bytesvar,type(bytesvar))
#b'\x80\x03]q\x00(K\x01K\x02e.' <class 'bytes'>
 
#loads
	# 字节流bytes==>原数据
lst = pickle.loads(bytesvar)
print(lst)  #[1, 2]

#dump
	# 任意对象==>字节流bytes==>写入文件对象
lst = [1,2]
with open('moxie1.txt','wb') as fp:
	pickle.dump(lst,fp) #参数1:数据  参数2:文件对象  2个参数

#load
	#文件==>读取字节流bytes==>原数据
with open('moxie1.txt','rb') as fp:
	lst = pickle.load(fp)
print(lst)
print('----------------------------1')

# dumps 和 loads 对文件进行写入读取字节流操作
# 写入bytes
# 1把list==>bytes  dumps
lst = [2,3]
bytesvar = pickle.dumps(lst)

# 2写入bytes到文件对象
with open('moxie2.txt','wb') as fp:
	fp.write(bytesvar)

# 读取bytes
# 1从文件对象读取内容--bytes
with open('moxie2.txt','rb') as fp:
	bytesvar = fp.read()

# 2将bytes==>原数据   loads
lst = pickle.loads(bytesvar)
print(lst)  #[2, 3]












































