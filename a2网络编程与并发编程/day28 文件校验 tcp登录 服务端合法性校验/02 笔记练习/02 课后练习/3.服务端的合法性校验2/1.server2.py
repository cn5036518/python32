# ### 服务端

import socketserver
import hmac
import os

class MyServer(socketserver.BaseRequestHandler):
	
		secret_key = '小兔儿乖乖,把门开开'
		# conn = self.request
		
		def auth(self):
			conn = self.request
			
			# 创建一个随机的32位字节流
			msg = os.urandom(32)
			
			# 把32位随机字节流发送给客户端
			conn.send(msg)
			
			# 服务端进行数据校验
			hm = hmac.new(self.secret_key.encode(),msg)
			ser_res = hm.hexdigest()
			
			# 服务端接受客户端发送过来的数据结果
			cli_res = conn.recv(1024).decode()
			
			# 进行比对,如果ok 返回True , 反之返回False
			return True if ser_res == cli_res else False
			
		def handle(self):
			# conn = self.request
			if self.auth():
				self.request.send('True'.encode())
			else:
				self.request.send('False'.encode())

server = socketserver.ThreadingTCPServer(("127.0.0.1" , 9001),MyServer)
# 开启,让一个端口绑定多个程序;  模块.类.属性 = True
socketserver.TCPServer.allow_reuse_address = True
server.serve_forever()



















































