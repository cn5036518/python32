# ### 客户端
import socket
import hmac

sk = socket.socket()
sk.connect(("127.0.0.1" , 9003)) #元组

# 处理收发数据的逻辑
def auth(secret_key):
	# 2 client收到这个32位随机字节流后
	bytes1 = sk.recv(32)
	print(bytes1)
	
	# 3 把32位随机字节流(要加密的内容)和密钥-关键字secret_key(字节流) 用hmac加密算法加密后
	hm = hmac.new(secret_key.encode(),bytes1)
	strvar = hm.hexdigest()  #少写了hex
	print(strvar)  #字符串
	#fcc6e80123420a9e72ae647b050b57c3
	
	# 4 把加密结果发给server
	sk.send(strvar.encode())
	
	# 5 client接收结果
	res = sk.recv(1024).decode()
	if res == 'True':
		print('服务端校验通过')
	elif res == 'False':
		print('服务端校验不通过')
	


secret_key = '小兔儿乖乖,把门开开'

# 调用授权函数
res = auth(secret_key)


sk.close()

































