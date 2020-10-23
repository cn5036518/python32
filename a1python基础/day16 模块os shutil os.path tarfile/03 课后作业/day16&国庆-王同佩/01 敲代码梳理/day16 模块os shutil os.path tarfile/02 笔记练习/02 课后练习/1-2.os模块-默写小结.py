# ### os 模块
import os

#01 system()  在python中执行系统命令
# os.system('ifconfig') # linux
# os.system('rm -f ceshi.txt')
os.system('pwd')  #当前py文件所在的目录  pwd两端有引号
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习
print('----------------------1 os.system')

#02 popen()   执行系统命令返回对象,通过read方法读出字符串
obj = os.popen('pwd')  #pwd两端有引号
print(obj)
#<os._wrap_close object at 0x7fa0d37ea9e8>
print(obj.read())
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习
print('----------------------2 os.popen')

#03 listdir() 获取指定文件夹中所有内容的名称列表 ***
lst = os.listdir()
print(lst)
#['1-1os模块.py', '1-2.os模块.py', '1.os模块.py', '2-1os shutil.py', '2.os_shutil.py', 
# '3-1.os_path.py', '3.os_path.py', '4-1.tarfile.py', '4.tarfile.py', '__init__.py']
print('----------------------3 os.listdir')

#04 getcwd()  获取当前文件所在的默认路径 ***
# 001 路径
res = os.getcwd()  # os.system('pwd')  #和这个等效
print(res)
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习
print('----------------------4 os.getcwd')

# 002 路径+文件   ***
print(__file__)
# /mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习/1-2.os模块.py
print(os.path.dirname(__file__))  #路径
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习
print(os.path.basename(__file__))  #文件名
#1-2.os模块.py
print('----------------------4-2 __file__')

#05 chdir()   修改当前文件工作的默认路径
# 目前文件的工作目录是py文件所在的目录.即
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习
os.system('pwd')
#/mnt/hgfs/ubuntu_gx/python32/day16 模块os shutil os.path tarfile/02 笔记练习/02 课后练习
os.chdir('/home/wangtongpei/mywork')
os.system('touch 2.txt')  #如果已经存在就覆盖
os.system('pwd') #/home/wangtongpei/mywork
print('----------------------5 os.chdir()')

#06 environ   获取或修改环境变量

# [windows]
# (1)右键qq属性找路径
# (2)右键我的电脑属性->高级系统设置->环境变量->path 
  # 打开环境变量添加对应路径
# (3)cmd => QQScLauncher

# [linux]
# (1)在家目录中创建个文件夹,里面创建个文件wangwen,写入ifconfig
# (2)增加wangwen的可执行权限 chmod 777 wangwen 测试一下 sudo ./wangwen
# (3)添加环境变量在os.environ["PATH"] 中拼接wangwen所在的绝对路径
# (4)os.system("wangwen")

# 总结: 环境变量path的好处是,让系统自动的找到该命令的实际路径进行执行;
# print(os.environ)
print(os.environ['PATH'])
#/home/wangtongpei/bin:/home/wangtongpei/.local/bin:/usr/local/sbin:
# /usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

os.environ['PATH'] += ':/home/wangtongpei/mywork'
# 临时添加.重启linux后,应该就没有了
print(os.environ['PATH'])
# /home/wangtongpei/bin:/home/wangtongpei/.local/bin:/usr/local/sbin:/usr/local/bin:
# /usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:
# /home/wangtongpei/mywork
os.system('wangwen2')
print('----------------------6 os.environ')


#--os 模块属性  属性后面没有()
#01 name 获取系统标识   linux,mac ->posix      windows -> nt
print(os.name)  #posix

#02 sep 获取路径分割符号  linux,mac -> /       window-> \ ***
print(os.sep)  #/

#03 linesep 获取系统的换行符号  linux,mac -> \n    window->\r\n 或 \n
print(os.linesep) #空行 看不见
print(repr(os.linesep))  #'\n'  显示空行


# 小结:
# 方法6个
os.system('pwd')
print('-------------------1 os.system()')

obj = os.popen('pwd')
res = obj.read()
print(res)
print('-------------------2 os.popen()')

print(os.listdir())
print('-------------------3 os.listdir()')

print(os.getcwd())  #当前文件所在的路径
print('-------------------4 os.getcwd()')

print(__file__)
print(os.path.dirname(__file__))
print('-------------------4-1 __file__')

# os.chdir('/home/wangtongpei/mywork')  #
os.chdir(os.path.dirname(__file__))  #
print(os.getcwd())
print('-------------------5 os.chdir()')

os.environ['PATH']
print('-------------------6 os.environ')
print('-------------------1 方法')

# 属性3个
print(os.name) #posix
print(os.sep)  # /
print(repr(os.linesep))  # '\n'
print('-------------------2 属性')





































