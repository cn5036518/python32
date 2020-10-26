# 定义枪类

class Gun():

	def __init__(self,bulletbox):
		self.bulletbox = bulletbox

	def shoot(self,firenum):

		if self.bulletbox.bulletboxcount < firenum:
			while self.bulletbox.bulletboxcount > 0:
				print("哒~",end="")
				self.bulletbox.bulletboxcount -= 1
				if self.bulletbox.bulletboxcount == 0:
					print(" 弹药不足,请装弹")
		else:
			self.bulletbox.bulletboxcount -= firenum
			print("哒~"*firenum,"子弹剩余{}发".format(firenum))


