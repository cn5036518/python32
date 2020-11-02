from gevent import monkey ; monkey.patch_all()
import gevent
import requests

url_lst = [
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/"
]

def get_url(url):
	response = requests.get(url)
	if response.status_code == 200:
		pass

lst = []
for i in url_lst:
	g = gevent.spawn(get_url, i)
	lst.append(g)
gevent.joinall(lst)
print("主线程执行结束...")