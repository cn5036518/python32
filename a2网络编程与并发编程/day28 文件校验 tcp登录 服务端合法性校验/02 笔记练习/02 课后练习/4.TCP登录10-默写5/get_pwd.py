import hashlib
import hmac

def get_pwd(user,pwd):
	hm = hmac.new(user.encode(),pwd.encode())  #参数1:key-盐-bytes 参数2:要加密的内容-bytes
	strvar = hm.hexdigest()
	print(strvar)
	
get_pwd('wangwen','111')	 # 49e00e36d304de871b64810697767a24
get_pwd('lisi','222')	# a53706c2566a50402b677165b403c88f	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	