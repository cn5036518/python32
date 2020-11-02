import  json
class Myclass():

	lst=[]

	def aaa(self):
		with open("data.json", mode="r", encoding="utf-8") as fp:
			for i in fp:
				dic = json.loads(i.strip())
				self.lst.append(dic)

obj=Myclass()
print(obj.lst)






