
# ### (1) 导入导出 不要加分号
导出数据库
1.退出mysql
2.选择要导出的默认路径
  /home/wangtonpei
3.mysqldump -uroot -p db001 > db001.sql


导入数据库
1.登录到mysql之后
2.创建新的数据库
  进入到新的数据库 use db007
3.source 路径+文件  
   source /home/wangtongpei/db001.sql;
   
   
navicat 
导出数据库
1 右键目标数据库--转储sql文件--结构和数据db001.sql文件

导入数据库
1  右键新建数据库
2  右键新建的数据库--运行sql文件.
    选中导出数据库的db001.sql文件
3 右键-刷新数据库如果看不到新导入的表
   使用先关闭新建的数据库,然后打开新建的数据库即可看到



# ### (2) 配置linux下的编码集
!includedir  /etc/mysql/conf.d/       客户端的修改
# 设置mysql客户端默认字符集
default-character-set=utf8
!includedir  /etc/mysql/mysql.conf.d/ 服务端的修改
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8

service mysql restart

问题:
mysql的字符集(客户端和服务端)从latin1修改成utf8后,mysql里面无法输入中文

解决办法:
只将服务端的字符集从latin1修改成utf8即可
客户端的字符集不要修改,保持默认即可,将添加的
default-character-set=utf8 给注释后,就可以在mysql中输入中文了
# 设置mysql客户端默认字符集
#default-character-set=utf8



win下 mysql的配置文件
D:\MySQL5.7\mysql-5.7.25-winx64\my.ini

[mysql]  #客户端配置
# 设置mysql客户端默认字符集
default-character-set=utf8
[mysqld]  #服务端配置
# 设置3306端口
port = 3306
# 设置mysql的安装目录
basedir=D:\MySQL5.7\mysql-5.7.25-winx64
# 设置mysql数据库的数据的存放目录
datadir=D:\MySQL5.7\mysql-5.7.25-winx64\data
# 允许最大连接数
max_connections=200
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB


mysql> \s   #查看win下 mysql的配置
--------------
mysql  Ver 14.14 Distrib 5.7.25, for Win64 (x86_64)

Connection id:          2
Current database:
Current user:           root@localhost
SSL:                    Not in use
Using delimiter:        ;
Server version:         5.7.25 MySQL Community Server (GPL)
Protocol version:       10
Connection:             localhost via TCP/IP
Server characterset:    utf8
Db     characterset:    utf8
Client characterset:    utf8
Conn.  characterset:    utf8
TCP port:               3306
Uptime:                 2 hours 21 min 44 sec


linux下 mysql的配置文件    /etc/mysql/my.cnf
wangtongpei@wangtongpei-virtual-machine:~$ sudo find / -name 'my.cnf'
[sudo] wangtongpei 的密码： 
find: `/run/user/1000/gvfs': 权限不够
/var/lib/dpkg/alternatives/my.cnf
/etc/alternatives/my.cnf
/etc/mysql/my.cnf

wangtongpei@wangtongpei-virtual-machine:~$ more /etc/mysql/my.cnf
!includedir /etc/mysql/conf.d/   #客户端的修改
!includedir /etc/mysql/mysql.conf.d/  #服务端的修改

#客户端的修改  (修改配置文件前,先cp备份)
wangtongpei@wangtongpei-virtual-machine:/etc/mysql/conf.d$ pwd
/etc/mysql/conf.d
wangtongpei@wangtongpei-virtual-machine:/etc/mysql/conf.d$ ls
mysql.cnf
wangtongpei@wangtongpei-virtual-machine:/etc/mysql/conf.d$ sudo nano mysql.cnf

将
# 设置mysql客户端默认字符集
default-character-set=utf8
添加到mysql.cnf文件的最下方

#服务端的修改  (修改配置文件前,先cp备份)
wangtongpei@wangtongpei-virtual-machine:/etc/mysql/conf.d$ cd /etc/mysql/mysql.conf.d/
wangtongpei@wangtongpei-virtual-machine:/etc/mysql/mysql.conf.d$ ls
mysqld.cnf
wangtongpei@wangtongpei-virtual-machine:/etc/mysql/mysql.conf.d$ sudo cp mysqld.cnf mysqld_bak.cnf 
wangtongpei@wangtongpei-virtual-machine:/etc/mysql/mysql.conf.d$ ll

将
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
添加到mysql.conf.d文件的最下方


修改了配置文件,重启mysql服务后,修改生效
sudo service mysql restart



mysql> \s             #查看linux下 mysql的配置
--------------
mysql  Ver 14.14 Distrib 5.7.32, for Linux (x86_64) using  EditLine wrapper

Connection id:		36
Current database:	db007
Current user:		root@localhost
SSL:			Not in use
Current pager:		stdout
Using outfile:		''
Using delimiter:	;
Server version:		5.7.32 MySQL Community Server (GPL)
Protocol version:	10
Connection:		Localhost via UNIX socket
Server characterset:	latin1          #这里需要修改成utf8   # 服务端使用的字符集默认为8比特编码的latin1字符集
Db     characterset:	utf8
Client characterset:	utf8
Conn.  characterset:	utf8
UNIX socket:		/var/run/mysqld/mysqld.sock
Uptime:			1 hour 30 min 42 sec















































