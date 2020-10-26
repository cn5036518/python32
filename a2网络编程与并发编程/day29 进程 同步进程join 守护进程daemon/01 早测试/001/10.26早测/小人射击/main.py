from package.bulletbox import BulletBox
from package.gun import Gun
from package.person import Person

obj=BulletBox(10)
ak47=Gun(obj)
libai=Person(ak47)

if __name__ == "__main__":
    libai.fire(3)


