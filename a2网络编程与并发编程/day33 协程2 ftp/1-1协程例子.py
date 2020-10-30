# ### 协程例子
# (1) spawn(函数,参数1,参数2,参数 .... ) 启动协程
# (2) join 阻塞,直到某个协程在任务执行完毕之后在放行
# (3) joinall 等待所有协程任务执行完毕之后放行;
	  # g1.join()  g2.join() <=> gevent.joinall( [g1,g2..] )
# (4) value 获取协程任务中的返回值 g1.value  g2.value
from gevent import monkey
monkey.patch_all()
import gevent,time,requests

def eat():
	print('eat1 开始吃 ... ')
	time.sleep(1)
	print('eat2 继续吃 ...')
	return '吃完了'
	
def play():
	print('play1 开始玩 ...')
	time.sleep(1)
	print('play2 继续玩...')
	return '玩完了'

# # 创建协程对象g1
# g1 = gevent.spawn(eat)
#
# # 创建协程对象g2
# g2 = gevent.spawn(play)
#
# # 等待所有协程任务执行完毕之后放行
# # gevent.joinall([g1])
# gevent.joinall([g1,g2])
# print('主线程执行结束')
#
# # 获取协程任务中的返回值
# print(g1.value)
# print(g2.value)

# eat1 开始吃 ... 
# play1 开始玩 ...
# eat2 继续吃 ...
# play2 继续玩...
# 主线程执行结束
# 吃完了
# 玩完了


# (2) 利用协程爬取数据

# HTTP 状态码
	# 200 ok
	# 400 bad request
	# 404 not found

import requests
response = requests.get('http://www.baidu.com')
# print(response,type(response))
# <Response [200]> <class 'requests.models.Response'>

# 获取状态码
print(response.status_code)  #200

# 获取网页中的字符编码
res = response.apparent_encoding
print(res)  #utf-8

# 设置编码集,防止乱码
print(response.encoding)  #ISO-8859-1
response.encoding = res
print(response.encoding)  #utf-8

# 获取网页内容
res = response.text
print(res)
# <!DOCTYPE html>
# <!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;
# charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always
 # name=referrer><link rel=stylesheet type=text/css 
 # href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css>
 # <title>百度一下，你就知道</title></head> <body link=#0000cc> 
 # <div id=wrapper> <div id=head> <div class=head_wrapper>
 # <div class=s_form> <div class=s_form_wrapper> <div id=lg>
 # <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> 
 # </div> <form id=form name=f action=//www.baidu.com/s class=fm> 
 # <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8>
 # <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1>
 # <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu>
 # <span class="bg s_ipt_wr">
 # <input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span>
 # <span class="bg s_btn_wr"><input type=submit id=su value=百度一下 class="bg s_btn">
 # </span> </form> </div> </div> <div id=u1> 
 # <a href=http://news.baidu.com name=tj_trnews class=mnav>新闻</a>
 # <a href=http://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> 
 # <a href=http://map.baidu.com name=tj_trmap class=mnav>地图</a> 
 # <a href=http://v.baidu.com name=tj_trvideo class=mnav>视频</a> 
 # <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>贴吧</a> 
 # <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;
 # tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>登录</a> 
 # </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">登录</a>');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">更多产品</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>关于百度</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>使用百度前必读</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>意见反馈</a>&nbsp;京ICP证030173号&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>
print('-----------------------1')

url_lst = [
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/"
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/"
	]

def get_url(url):
	reponse = requests.get(url)
	if reponse.status_code == 200:
		# print(response.text)
		pass
		
# (1) 正常爬取   同步  baidu爬取完毕后,才去爬取jd
startime = time.time()
for i in url_lst:
	get_url(i)
endtime = time.time()
print(endtime-startime)  #3.2201054096221924

# (2) 用协程的方法爬取数据  异步  一个线程的5个协程同时去爬取5个网站
# lst = []

# startime = time.time()
# for i in url_lst:
	# g = gevent.spawn(get_url,i)  #创建协程对象
	# lst.append(g)

# gevent.joinall(lst)
# endtime = time.time()
# print('主线程执行结束 ... 时间{}'.format(endtime-startime))













































