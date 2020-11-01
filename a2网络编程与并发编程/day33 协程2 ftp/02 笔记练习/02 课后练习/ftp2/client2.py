import socket
import json

sk = socket.socket()
sk.connect(("127.0.0.1",9001))
# 处理收发数据的逻辑
def auth(opt):
	usr = input('username : >>> ').strip()
	pwd = input('password : >>> ').strip()
	dic = {'user':usr,'passwd':pwd,'operate':opt}
	str_dic = json.dumps(dic)  #dict-->str
	
	# 发送数据
	sk.send(str_dic.encode())  #str-->bytes
	
	# 接受数据
	info = sk.recv(1024).decode()  #bytes-->str
	dic = json.loads(info)  #str-->dict
	return dic	
	
def register():
	res = auth('register')
	print(res)
	return res
	
def login():
	res = auth('login')
	print(res)
	return

login()

sk.close()














































