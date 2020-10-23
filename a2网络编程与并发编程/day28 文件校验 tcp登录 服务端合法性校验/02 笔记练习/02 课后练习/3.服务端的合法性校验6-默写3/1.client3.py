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
	#b'\xbeY\x16\xbci\xf75\x8d\xcc\x11\xb7@2\\\xb2k5\xfb\xe3\x95l\xa3\xdc\\FM\x9dK\x1eo\xa5\x00'

	
	# 3 把32位随机字节流(要加密的内容-参数2)和密钥-关键字secret_key(字节流-参数1) 用hmac加密算法加密后
	hm = hmac.new(secret_key.encode(),bytes1)
	strvar = hm.hexdigest()  #字符串
	print(strvar)

	
	# 4 把加密结果发给server
	sk.send(strvar.encode())
	
	# 9 client接收结果
	res = sk.recv(1024).decode()
	return res



secret_key = '小兔儿乖乖,把门开开'

# 调用授权函数
res = auth(secret_key)
if res == 'True':
	print('服务端校验通过')
elif res == 'False':
	print('服务端校验不通过')




sk.close()

































