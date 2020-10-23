# ### 客户端
import socket
import hmac

sk = socket.socket()
sk.connect(("127.0.0.1" , 9000)) # 元组

# 处理收发数据的逻辑
def auth(secret_key):
	# 3接受服务端发送过来的32位随机二进制字节流
	msg = sk.recv(32)
	
	# 4 hmac.new(   key(字节流) ,  要加密的内容(字节流)  )
	hm = hmac.new(secret_key.encode(),msg)
	# 把32位随机字节流(要加密的内容)和密钥-关键字secret_key 用hmac加密算法加密
	
	# 5 hmac返回的是具有固定32位长度的十六进制字符串
	cli_res = hm.hexdigest()
	
	# 6 把最后计算的结果发送给服务端进行校验
	sk.send(cli_res.encode())
	
	# 9 接受服务端给予的校验结果
	res = sk.recv(1024).decode()
	# 这里收发是交叉进行的,不会出现黏包,只有连续收或者连续发,才会出现黏包
	
	return res	
	
# secret_key = "不开,老妈没回来"
secret_key = '小兔儿乖乖,把门开开'	
# 调用授权函数
res = auth(secret_key)

if res == "True":
	print('服务器校验通过,你可以调用服务端的功能了')
else:
	print('服务器校验失败,你无权使用服务端的功能')


sk.close()











































