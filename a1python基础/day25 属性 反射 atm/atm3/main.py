from package.view import View
from package.operation import Operation



class Main():
	
	@staticmethod   #类和对象都可以调,且不会额外传递参数
	def run():
		if View.login():  #返回True
			obj = Operation() # 新建对象
			while True:
				choice = input('请选择需要办理的业务:')
				if choice == '1':
					pass
				elif choice == '2':
					pass
				elif choice == '0':
					obj.save()
					break










if __name__ == '__main__':  #入口文件 这行之下只能当前文件执行
# 如果是被别的模块导入,这行之下就无法执行
	Main.run()

























