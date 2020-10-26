
from package.bulletbox import BulletBox
from package.gun import Gun
from package.person import Person
# 实例化
danxia = BulletBox(20)

qiang = Gun(danxia)

soider = Person(qiang)


if __name__ == '__main__':
    soider.fire(10)
    soider.fire(20)
    soider.fill(10)
    soider.fire(20)
