# ### struct 模块使用
import struct

# pack     打包 
	# 把任意长度数字转换成具有固定4个字节长度的字节流
# unpack   解包
	# 把4个字节长度的值恢复成原来的数字,返回元组(注意点)

# pack
# i => int  要转换的当前类型是整型
# """范围: -21亿~21亿左右 控制在1.8G之内"""

res = struct.pack('i',999999998)
print(res,len(res)) #b'\xfe\xc9\x9a;' 4

res = struct.pack('i',1111111119)
print(res,len(res))  #b'\xcf5:B' 4

res = struct.pack('i',3)
print(res,len(res)) #b'\x03\x00\x00\x00' 4

res = struct.pack('i',2000000000)
# print(res,len(res)) #b'\x00\x945w' 4

# unpack
# i => 把对应的数据(4位字节流)转化成整型
tup = struct.unpack('i',res)
print(tup)  #元组
print(tup[0])
# (2000000000,)
# 2000000000

# 解决黏包场景:
	# 应用场景在实时通讯时,需要阅读此次发的消息是什么
# 不需要解决黏包场景:
	# 下载或者上传文件的时候,最后要把包都结合在一起,黏包也是可以的.


































