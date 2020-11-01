import socket
import json
import struct
import os

sk = socket.socket()
sk.connect(("127.0.0.1",9002))

# 定义接受数据的方法  处理黏包
def myrecv(info_len = 1024 ,sign=False): #默认参数

	if sign == True:  #处理黏包
		info_len = sk.recv(4)
		info_len = struct.unpack("i",info_len)[0]  #元组

	info = sk.recv(info_len).decode() #bytes-->str
	dic = json.loads(info) #str-->dict
	return dic
	
def mysend(dic):
	str_dic = json.dumps(dic)  #dict-->str
	sk.send(str_dic.encode())  #str-->bytes
	
	
# 处理收发数据的逻辑
def auth(opt):
	usr = input('username : >>> ').strip()
	pwd = input('password : >>> ').strip()
	dic = {'user':usr,'passwd':pwd,'operate':opt}
	
	# 发送数据
	# str_dic = json.dumps(dic)  #dict-->str
	# sk.send(str_dic.encode())  #str-->bytes
	mysend(dic)
	
	# 接受数据
	# info = sk.recv(1024).decode()  #bytes-->str
	# dic = json.loads(info)  #str-->dict
	dic = myrecv()
	return dic	
	
def register():
	res = auth('register')
	print(res)
	return res
	
def login():
	res = auth('login')
	print(res)
	return
	
def myexit():
	opt_dic = {"operate":"myexit"}
	sk.send(json.dumps(opt_dic).encode())
	exit('欢迎下次再来')
	
def download():
	operate_dict = {
		"operate":"download",
		"filename":"studey_info.mp4"
	}
	
	# 把要下载的请求发送给服务端
	sk.send(json.dumps(operate_dict).encode())
	# print(1)
	
	# (1) 接受服务端返回的消息
	res = myrecv(sign=True)
	print(res)
	# {'result': True, 'info': '文件可以下载'}
	
	if res['result']:
		# 给用户创建个文件夹(存放下载的文件)
		try:
			os.mkdir('mydownload2')
		except:
			pass
			
		# (2) 接受文件大小和文件名
		dic = myrecv(sign=True)
		print(dic)
		# {'filename': 'studey_info.mp4', 'filesize': 72274155}
		
		# (3) 接收文件中的内容
		base_path = os.path.dirname(__file__)  #当前文件所在目录的绝对路径
		filename2 = os.path.join(base_path,'mydownload2',dic['filename'])
		# with open('./mydownload2/'+dic['filename'],mode='wb') as fp:  
		# 拼接相对路径
		with open(filename2,mode='wb') as fp:
			while dic['filesize']:
				content = sk.recv(102400)
				fp.write(content)
				dic['filesize'] -= len(content)
		print("客户端下载完毕 ... ")
		
	else:
		print('文件不存在,不能下载')
	

# login()
# myexit()
download()

sk.close()














































