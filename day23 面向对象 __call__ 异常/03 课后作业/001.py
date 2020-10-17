lst = []
def func():
	global  lst
	# lst = [1,2333]
	lst.append(1)
	print(lst)

func()	
print(lst)
print('------------1')

d = 50
def func():
	global d
	d = 1
	print(d) #1
func()
print(d)  #1
print('------------2')