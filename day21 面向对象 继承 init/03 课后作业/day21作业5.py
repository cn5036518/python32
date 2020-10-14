# 4.读程序写结果.(不执行)
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

config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
config_obj_list[1].run()  
config_obj_list[2].run()	
# 2 999
# 666 3		#子类继承父类的构造方法
print('-----------------4')			
		
		
		
		
		
		
		
		
		
		
		
		
		



















