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

def register():
	res = auth('register')
	print(res)
	return res
	
def login():
	res = auth('login')
	print(res)
	return res
	
def myexit():
	opt_dic = {'operate':'myexit'}
	str_dic = json.dumps(opt_dic)
	bytes1 = str_dic.encode()
	
	sk.send(bytes1)
	exit('欢迎下次再来')  #退出代码执行
# myexit()	
# login()

# 1注册 2登录 3退出
operat_lst1 = [("注册",register),("登录",login),("退出",myexit)]
# (1, ('注册', <function register at 0x7ff1427faa60>))
# (2, ('登录', <function login at 0x7ff1427fa9d8>))
# (3, ('退出', <function myexit at 0x7ff1427faae8>))

def main(operat_lst):
	for i,tup in enumerate(operat_lst,start=1):
		#展示界面
		print(i,tup[0])
		# 1 注册
		# 2 登录
		# 3 退出
	# 提供操作
	num = input('请输入要执行的选项>>>').strip()
	if num.isdecimal():
		num = int(num)
		res = operat_lst[num-1][1]()
		return res
	else:
		print('请输入1-3的数字')

while True:
	# 开启第一套操作界面
	res = main(operat_lst1)
	print(res)


sk.close()


























