# ### 客户端
import socket
import hmac

sk = socket.socket()
sk.connect(("127.0.0.1" , 9004)) #元组

# 处理收发数据的逻辑
def auth(secret_key):
	#2 client收到这个32位随机字节流后
	bytes1 = sk.recv(32)
	print(bytes1)
	
	# 3 把32位随机字节流(要加密的内容)和密钥-关键字secret_key 用hmac加密算法加密后
	hm = hmac.new(secret_key.encode(),bytes1)
	strvar = hm.hexdigest()
	print(strvar)
	#d219a0535201e0ee38f8a110781dee4b
	
	
	# 4 把加密结果发给server
	sk.send(strvar.encode())
	
	#9 client接收结果
	res = sk.recv(1024).decode()
	print(res)
	return res


secret_key = '小兔儿乖乖,把门开开'

# 调用授权函数
res = auth(secret_key)
if res == 'True':
	print('服务端校验通过')
else:
	print('服务端校验不通过')

sk.close()


# 思路
# 1 server产生一个32位的随机字节流发给client
# 2 client收到后,用这个32位的随机字节流 和 密钥 ,通过hmac加密算法计算一个值
   # 把这个值发给server
# 3 server收到后,用第2步的办法,即用这个32位的随机字节流 和 密钥 ,通过hmac加密算法计算一个值
  # 对比着2个值,如果相同,就验证通过
  # 如果不同.就验证不通过
  
# 写法
# 1 把固定的架子写好
# 2 翻译上述思路
# 3 一步一打印,调试报错
  # 不怕慢就怕停
  # 重复多次默写--刻意练习重复

# 小结
# 将思路和写法分开
# 思路是提纲--设计
# 写法是文章--实现





























