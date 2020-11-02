from collections import Iterator, Iterable
import socketserver
import hashlib
import json

class MyServer(socketserver.BaseRequestHandler):

	sign = False

	def get_md5_code(self, usr, pwd):
		hs = hashlib.md5(usr.encode())
		hs.update(pwd.encode())
		return hs.hexdigest()

	def auth(self):
		conn = self.request
		res = conn.recv(1024).decode()
		dic = json.loads(res)
		print(dic, type(dic))
		with open("userinfo.data", mode="r", encoding="utf-8") as fp:
			for i in fp:
				usr, pwd = i.strip().split(":")
				if usr == dic["username"] and pwd == self.get_md5_code(dic["username"], dic["password"]):
					dic_msg = {"code": 1, "msg": "登录成功"}
					json_str = json.dumps(dic_msg)
					conn.send(json_str.encode())
					self.sign = True
					break

			if self.sign == False:
				dic_msg = {"code": 0, "msg": "登录失败"}
				res = json.dumps(dic_msg).encode()
				conn.send(res)

	def handle(self):
		self.auth()
server = socketserver.ThreadingTCPServer(("127.0.0.1", 9001), MyServer)
socketserver.TCPServer.allow_reuse_address = True
server.serve_forever()
