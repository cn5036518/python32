

class Gun():
    def __init__(self,bulletbox):
        self.bulletbox=bulletbox

    def shoot(self,fcount):
        if self.bulletbox.bulletcount == 0:
            print("没子弹了")
            
        elif self.bulletbox.bulletcount < fcount:
            print("突!" * self.bulletbox.bulletcount  ,"没子弹了")

        else:
            self.bulletbox.bulletcount -= fcount
            print("突!" * fcount,"您还剩{}发子弹".format(self.bulletbox.bulletcount))
            





















