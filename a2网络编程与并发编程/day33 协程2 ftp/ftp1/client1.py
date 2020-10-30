import socket,json

sk = socket.socket()
sk.connect(("127.0.0.1",9001) )

# 处理收发数据的逻辑
def auth(opt):
	usr = input("username : >>> ").strip()
	pwd = input("password : >>> ").strip()
	dic = {'user':usr,'passwd':pwd,'operate':opt}
	
	str_dic = json.dumps(dic)
	
	# 发送数据
	sk.send(str_dic.encode())
	
	# 接受数据
	strvar = sk.recv(1024).decode()  #bytes==>str
	dic = json.loads(strvar)  #str==>dict
	return dic

res = auth('register')
print(res)

sk.close()


























