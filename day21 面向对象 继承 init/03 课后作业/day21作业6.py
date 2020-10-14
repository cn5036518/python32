# 5.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)
    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print(666,self.num)

class AdminSite(object):
    def __init__(self):
        self._registry = {}
    def register(self,k,v):
        self._registry[k] = v

site = AdminSite()
print(len(site._registry))  #0  
site.register('range',666)
site.register('shilei',438)
print(len(site._registry)) #2 

site.register('lyd',StarkConfig(19))
site.register('yjl',StarkConfig(20))
site.register('fgz',RoleConfig(33))
print(len(site._registry))  #5  
print(site._registry)	
#{'range': 666, 
# 'shilei': 438,
# 'lyd': <__main__.StarkConfig object at 0x7fee9786fe48>, 
# 'yjl': <__main__.StarkConfig object at 0x7fee9786fe80>,
# 'fgz': <__main__.RoleConfig object at 0x7fee9786feb8>}	
print('-----------------5')	
		
	
		
		
		
		
		
		
		
		
		
		
		



















