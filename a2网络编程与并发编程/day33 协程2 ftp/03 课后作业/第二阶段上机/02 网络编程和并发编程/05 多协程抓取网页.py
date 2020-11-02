from gevent import monkey
monkey.patch_all()
import gevent
import time,requests

# url_lst = [
	# "http://www.baidu.com",
	# "http://www.jd.com/",
	# "http://www.taobao.com/",
	# "http://www.amazon.cn/",
	# "http://www.pinduoduo.com/",
	# "http://www.4399.com/"
# ]

url_lst = [
	"https://www.360.cn/"
	]


def get_url(url):
	response = requests.get(url)
	if response.status_code == 200:
		print(response.text)
		
lst = []
startime = time.time()
for i in url_lst:
	g = gevent.spawn(get_url,i)
	lst.append(g)
gevent.joinall(lst)
endtime = time.time()
print('主线程执行结束 ... 时间{}'.format(endtime-startime))































