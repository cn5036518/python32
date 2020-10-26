from package.bulletbox import BulletBox
from package.gun import Gun
from package.person import Person

obj=BulletBox(10)
ak47=Gun(obj)
libai=Person(ak47)
# libai.fire(3)

if __name__ == "__main__":  #这里如果__main__ 前后有空格,下面的代码就不会执行
# if __name__ == " __main__ ":  #这里如果__main__ 前后有空格,下面的代码就不会执行
    libai.fire(3)
    libai.fill(2)


