# 3.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print(666,self.num)

config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
# for item in config_obj_list:
#     item.changelist(168)

StarkConfig(1).changelist(168)

# 1 168
# 2 168
# 666 3  #子类继承父类的构造方法
print('-----------------3')			
	
		
		
		
		
		
		
		
		
		
		
		
		



















