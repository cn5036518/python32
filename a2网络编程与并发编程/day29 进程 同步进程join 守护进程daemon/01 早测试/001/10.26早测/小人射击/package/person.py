from .gun import Gun
class Person():
    def __init__(self,gun):
        self.gun=gun
        
    def fill(self,num):
        self.gun.bulletbox.bulletcount +=num

    def fire(self,fcount):
        self.gun.shoot(fcount)
        print(1)

# obj=Person()
# obj.fire(2)



