# 6.读程序写结果.(不执行)
class StarkConfig():
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)
    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print(666,self.num)

class AdminSite():
    def __init__(self):
        self._registry = {}
    def register(self,k,v):
        self._registry[k] = v

site = AdminSite()
site.register('lyd',StarkConfig(19))
site.register('yjl',StarkConfig(20))
site.register('fgz',RoleConfig(33))

# self._registry = {'lyd':StarkConfig(19),'yjl':StarkConfig(20),'fgz',RoleConfig(33)}

# for k,row in site._registry.items():
    # row.changelist(5)
for k,row in site._registry.items():
    row.run()	
	
# StarkConfig(19).run()
# StarkConfig(20).run()
# RoleConfig(33).run()  #子类的方法重写了服了的同名方法

# 19 5
# 20 5
# 666 33  #子类继承父类的构造方法

# 19 999
# 20 999
# 666 33	#子类的方法重写了服了的同名方法
print('-----------------6')			
		
	
		
		
		
		
		
		
		
		
		
		
		



















