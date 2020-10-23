# 7.读程序写结果.(不执行)
class JustCounter:
	__secretCount = 0
	def count(self):
		print(self.__secretCount) # 获取
		self.__secretCount += 1 

	def count3():
		print(JustCounter.__secretCount)
		JustCounter.__secretCount += 1
		print(JustCounter.__secretCount)

class Bars(JustCounter):
	def count2(self):
		print(self.__secretCount)

#  情况一
counter1 = JustCounter()
counter1.count() #0   #对象1的私有成员
counter1.count()  #1 对象1只能使用类的成员,无法修改类的成员  关键点 对象和类的空间是独立的
JustCounter.count3()  #0 1  #类的私有成员
#  情况二
counter2 = Bars() 
counter2.count()  #1 对象2的私有成员,获取的是类的私有成员,此时是1
counter2.count()  #2 对象2的私有成员
#  情况三
JustCounter.count3()	#1 2  #类的私有成员	
print('-----------------7')			
		
		
		
		
		
		
		
		
		
		
		



















