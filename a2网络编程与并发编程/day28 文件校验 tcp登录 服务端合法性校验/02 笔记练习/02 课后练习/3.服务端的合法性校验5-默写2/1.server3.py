import hmac
import os 
import socketserver

# 思路
# 密钥  secret_key = '小兔儿乖乖,把门开开'
# 32位随机字节流
# hmac 加密算法(服务端和客户端约定好,都用hmac算法)
# 上述3个给密码进行加密
# 加密方法:
# 把32位随机字节流(要加密的内容)和密钥-关键字secret_key 用hmac加密算法加密
#  需要知道上述3个,才能解密

# 步骤
# 服务端和客户端(双方)约定好
 # 1 都用hmac算法
 # 2 密钥都是 secret_key = '小兔儿乖乖,把门开开'
# 1 server把32位随机字节流发给client
# 2 client收到这个32位随机字节流后
	# 把32位随机字节流(要加密的内容)和密钥-关键字secret_key 用hmac加密算法加密后
	# 把加密结果发给server
# 3 server也用和client相同的加密方法 即
   # 32位随机字节流(要加密的内容)和密钥-关键字secret_key 用hmac加密算法加密后
   # 对比client发过来的值和自己计算的值是否相同,如果相同,说明授权通过
    # (client可以调用或者使用server的功能)
   # 不同的话,授权不通过
  # 4 server把结果发给client
  # 5 client接收结果
   
class MyServer(socketserver.BaseRequestHandler):
	secret_key = '小兔儿乖乖,把门开开'
	
	def auth(self):
		bytes1 = os.urandom(32)
		print(bytes1)
		
		# 1 server把32位随机字节流发给client
		conn = self.request
		conn.send(bytes1)

		
		# 5 server接收client的加密结果
		str_cli = conn.recv(1024).decode()
		print(str_cli)  #31716d6eea4139f43933d94fa94e42e9

		
		#6  把32位随机字节流(要加密的内容-参数2)和密钥-关键字secret_key(字节流-参数1) 
		# 用hmac加密算法加密后
		# hm = hmac.new(self.secret_key.encode(),bytes1)  #没有写encode
		hm = hmac.new(self.secret_key.encode(),bytes1)
		str_ser = hm.hexdigest()
		print(str_ser)	
		
		#7 对比client发过来的值和自己计算的值
		if str_ser == str_cli:
			return True
		else:
			return False	
	
	# def handler(self): #拼写错误
	def handle(self):
	#8 server把结果发给client
		if self.auth():
			print('服务端校验通过')
			self.request.send('True'.encode())
		else:
			print('服务端校验通过')
			self.request.send('False'.encode())
	
	
	
server = socketserver.ThreadingTCPServer(("127.0.0.1" , 9003),MyServer)
  # 开启,让一个端口绑定多个程序;  模块.类.属性 = True
socketserver.TCPServer.allow_reuse_address = True
server.serve_forever()
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   