# ### hashlib 
# """
# 场景: 网站密码加密
# hashlib模块的加密原则是单向不可逆的
# md5算法 : 可以把字符串变成具有固定长度的32位十六进制字符串
# """

# 撞库
# """
# 111222  => 00b7691d86d96aebd21dd9e138f90840
# 222333  => 00b7691d86d96aebd21dd9e138f90842
# """

import hashlib
import random

# ### 基本语法
# (一)md5对象
# 1.创建md5对象
hs = hashlib.md5()

# 2.把要加密的数据更新到对象中  [update => 把字节流更新到对象之后,进行加密]
hs.update('111222'.encode())

# 3.获取十六进制的字符串
res = hs.hexdigest()
print(res,len(res))
print('------------------------1')

# 加盐 (加key , 加一个关键字)
hs = hashlib.md5('XBOYww_'.encode())
hs.update('111222'.encode())
res = hs.hexdigest()
print(res) #623e0e8d4ecabd638c36a5e40189ba8f
print('------------------------2')

# 动态加盐
res = str(random.randrange(100000,1000000))
hs = hashlib.md5(res.encode())
hs.update('111222'.encode())
res = hs.hexdigest()
print(res) #77c23163ac9031fb71e9eee1a6184421
print('------------------------3')

# (二)sha系列算法
# """无论是加盐 还是 加密密码,都需要数据类型为二进制字节流"""
hs = hashlib.sha1()  # 结果是具有固定长度40位的十六进制字符串;
hs = hashlib.sha512('XGIRLww_'.encode())
# 结果是具有固定长度128位的十六进制字符串
hs.update('sha系列算法'.encode())
res = hs.hexdigest()
# """20c2502d0e00bf8fe35ebfbf097049d1f070e7968f30ef
# 3353ff33d311af50da6b3883bfb9ab411f9dc4cdcd2310b39
# f5815c6dc1c48cd138d07443a6bcdcd11 128"""
print(res,len(res))
print('------------------------4')

# (三)hmac加密算法
import hmac
import os
key = b"xdogaa_"
msg = b'112233'

# new(盐(字节流),密码(字节流) )
hm = hmac.new(key,msg)
res = hm.hexdigest()
print(res,len(res))
# eebe14b1c144092121236cb1e3da396a 32
print('------------------------5')

# 动态加盐
import os
# os.urandom(位数) #返回随机的二进制字节流
# res = os.urandom(10)
# print(res , len(res))
#b'\xab\xac2\xaa\x98[7\xad\xa7\xb5' 10
print('------------------------6')

key = os.urandom(64)
msg = b'112233'
hm = hmac.new(key,msg)
res = hm.hexdigest()
print(res,len(res))








































