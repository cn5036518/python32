# 2.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):
    pass
	
# 创建了一个列表,列表中有三个对象(实例)
config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
for item in config_obj_list:
    item.changelist(168)
print(config_obj_list[0].num)
# 1 168
# 2 168
# 3 168
# 1		
print('-----------------2')			
		
	
		
		
		
		
		
		
		
		
		
		
		



















