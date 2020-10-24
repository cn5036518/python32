import hashlib

def get_pwd(user,pwd):
	hs = hashlib.md5(user.encode())
	hs.update(pwd.encode())
	res = hs.hexdigest()
	print(res)
	
# get_pwd('lisi','222')
# get_pwd('wangwen','111')