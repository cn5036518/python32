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

# 2.把要加密的数据更新到对象中  
# [update => 把字节流更新到对象之后,进行加密]
hs.update('111222'.encode())  #参数是bytes

# 3.获取十六进制的字符串
res = hs.hexdigest()
print(res,len(res)) #00b7691d86d96aebd21dd9e138f90840 32

# 02 加盐 (加key , 加一个关键字,bytes)
hs = hashlib.md5('XBOYww_'.encode())  #参数是bytes
hs.update('111222'.encode()) #参数是bytes
res = hs.hexdigest()
print(res)  #623e0e8d4ecabd638c36a5e40189ba8f
 
# 03 # 动态加盐1
res = str(random.randrange(10000,100000))  #随机6位
hs = hashlib.md5(res.encode()) #参数是bytes
hs.update('111222'.encode())
res = hs.hexdigest()
print(res)  #结果每次都不一样


# (二)sha系列算法
# """无论是加盐 还是 加密密码,都需要数据类型为二进制字节流"""
# hs = hashlib.sha1()  # 结果是具有固定长度40位的十六进制字符串;
hs = hashlib.sha512('XGIRLww_'.encode())
# 结果是具有固定长度128位的十六进制字符串
hs.update('sha系列算法'.encode())
res = hs.hexdigest()
print(res,len(res))


# (三)hmac加密算法
import hmac
import os
key = b"xdogaa_"
msg = b"112233"

# new(盐(字节流),密码(字节流) )
hm = hmac.new(key,msg)
res = hm.hexdigest()
print(res,len(res))
#eebe14b1c144092121236cb1e3da396a 32

# 01动态加盐2
# os.urandom(位数) 返回随机的二进制字节流
res = os.urandom(10)  #返回随机10位的二进制字节流
print(res,len(res))
#b'\xf7\xff\xa8\x90\x06\xfe\xc9\x17\x87o' 10

key = os.urandom(64)  #返回随机64位的二进制字节流
msg = b'112233'
hm = hmac.new(key,msg)
res = hm.hexdigest()
print(res,len(res))
#ea628ec5090b3d490de37b129f377f46 32 每次都不一样






































