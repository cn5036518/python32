# ### 读代码,写答案
# 1.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print('666')
		
# 创建了一个列表,列表中有三个对象(实例)
config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
for item in config_obj_list:
    print(item.num)	 # 1 2 3
print('-----------------1')		

print(StarkConfig(1).num)  #1  StarkConfig(1)是对象
print(StarkConfig(2).num)  #2
print(RoleConfig(3))
print(RoleConfig(3).num)  #3 继承父类的构造方法

	
		
		
		
		
		
		
		
		
		
		
		



















