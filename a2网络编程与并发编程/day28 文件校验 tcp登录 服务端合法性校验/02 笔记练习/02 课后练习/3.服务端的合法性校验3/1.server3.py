# ### 服务端

import socketserver
import hmac
import os

class MyServer(socketserver.BaseRequestHandler):

	secret_key = '小兔儿乖乖,把门开开'
	
	def auth(self):
		conn = self.request
		
		# 1 创建一个随机的32位字节流
		msg = os.urandom(32)
		
		# 2 把字节流发送给客户端
		conn.send(msg)
		
		# 7 服务端进行数据校验
		#  hmac.new(   key(字节流) ,  要加密的内容(字节流)  )
		# 把32位随机字节流(要加密的内容)和密钥-关键字secret_key 用hmac加密算法加密
		# hm = hmac.new(self.secret_key,msg)
		hm = hmac.new(self.secret_key.encode(),msg)
		ser_res = hm.hexdigest()  #str类型
		
		# 8 服务端接受客户端发送过来的数据结果
		cli_res = conn.recv(1024).decode()
		
		# 9 进行比对,如果ok 返回True , 反之,返回False
		if ser_res == cli_res:
			return True
		else:	
			return False	
	
	def handle(self):
		if self.auth():
			self.request.send('True'.encode())
		else:
			self.request.send('False'.encode())
			
	
	
server = socketserver.ThreadingTCPServer(("127.0.0.1" , 9000),MyServer)	
# 开启,让一个端口绑定多个程序;  模块.类.属性 = True
socketserver.TCPServer.allow_reuse_address = True
server.serve_forever()

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
   # 对比client发过来的值和自己计算的值是个相同,如果相同,说明授权通过
    # (client可以调用或者使用server的功能)
   # 不同的话,授权不通过













































