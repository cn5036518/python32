def outer():
	def inner():
		print('我是inner函数')

def outer():
	def inner():
		def smaller():
			print('我是smaller函数')
		smaller()
	inner()
outer()  #我是smaller函数

























