# ### os 模块
import os

# system()  在python中执行系统命令
# os.system('ifconfig')  #linux

# os.system('ipconfig') windows
#### os.system('rm -f 12.txt')

# popen()  执行系统命令返回对象,通过read方法读出字符串
# obj = os.popen('ifconfig')
# print(obj)  #<os._wrap_close object at 0x7f16c5b64ba8>
# print(obj.read())

# listdir()  获取指定文件夹中所有内容的名称列表  ***
lst = os.listdir()
print(lst)
#['1-1os模块.py', '1.os模块.py', '2-1os shutil.py', 
# '2.os_shutil.py', '3.os_path.py', '4.tarfile.py', '__init__.py']

# getcwd() 获取当前文件所在的默认路径  ***
# 当前路径(绝对路径)
res = os.getcwd()
print(res)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile

# 当前路径+文件名(绝对路径)
print(__file__)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/1-1os模块.py

#chdir() 修改当前文件工作的默认路径
os.chdir('/home/wangtongpei/mywork')
print(__file__)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/1-1os模块.py
os.system('touch 2.txt')

# environ 获取或修改环境变量
# windows
# 1 右键qq属性找路径
# 2 右键我的电脑属性-高级系统设置-环境变量--path
  # 打开环境变量添加对应路径
# 3 cmd ==> qqsclauncher或者QQScLauncher.exe

# linux
# 1 在家目录中创建一个文件夹,里面创建一个文件wangwen.写入ifconfig
# 2 增加wangwen的可执行权限 chmod 777 wangwen 
  # 测试一下 sudo ./wangwen
# 3 添加环境变量在os.environ['path']中拼接wangwen文件的绝对路径
# 4 os.system('wangwen')

# 总结:环境变量path的好处是.让系统自动的找到该命令的实际路径进行执行
print(os.environ)
print(os.environ['PATH'])  #打印linux下的环境变量 路径之间是:隔开
# /home/wangtongpei/bin:/home/wangtongpei/.local/bin:/usr/local/sbin:
# /usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:
# /usr/games:/usr/local/games:/snap/bin

# os.environ['PATH'] = os.environ['PATH'] + '/home/wangtongpei/mywork'
os.environ['PATH'] += ':/home/wangtongpei/mywork'  #注意点  /home前面必须加上
# 路径分隔符:  否则,环境变量就没有添加成功
print(os.environ['PATH'])
# /home/wangtongpei/bin:/home/wangtongpei/.local/bin:/usr/local/sbin
# :/usr/local/bin:/usr/sbin:/usr/bin
# :/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/wangtongpei/mywork
os.system('wangwen')














