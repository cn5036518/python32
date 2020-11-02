import hashlib,os

def check_md5(filename):
	hs = hashlib.md5()
	filesize = os.path.getsize(filename)
	# print(filesize)
	with open(filename,mode='rb') as fp:
		# filesize 如果为空,循环终止;
		while filesize:
			content = fp.read(100)
			# """update 可以分批次进行加密  等价于一次性加密的结果"""
			hs.update(content)
			# 减去实际读取的字节长度
			filesize -= len(content)
			
		return hs.hexdigest()
	
res1 = check_md5('lianxi1.py')
res2 = check_md5('lianxi2.py')
print(res1 , res2)  
#dbe532cb0aef17a4eb36d27c2b80bd7c dbe532cb0aef17a4eb36d27c2b80bd7c




































