import re

strvar = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

def process_sign(strvar):
	strvar = strvar.replace("++","+")
	strvar = strvar.replace("--", "+")
	strvar = strvar.replace("+-", "-")
	strvar = strvar.replace("-+", "-")
	return strvar

def calc(strvar):
	if "*" in strvar:
		a,b = strvar.split("*")
		return float(a) * float(b)
	elif "/" in strvar:
		a,b = strvar.split("/")
		return float(a) / float(b)

def calc_exp(strvar):
	while True:
		obj = re.search(r"\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?",strvar)
		if obj:
			res1 = obj.group()

			res2 = calc(res1)
			strvar = strvar.replace(res1, str(res2))
		else:
			break

	strvar = process_sign(strvar)
	# print(strvar)
	lst = re.findall(r"[+-]?\d+(?:\.\d+)?",strvar)

	total = 0
	for i in lst:
		total += float(i)
	return total
	# print(total)

def remove(strvar):
	while True:
		obj = re.search(r"\([^\(\)]+\)",strvar)
		if obj:
			res1 = obj.group()
			# print(res1)
			res2 = calc_exp(res1)
			strvar = strvar.replace(res1,str(res2))

		else:
			return strvar

def main(strvar):
	#取最里层括号内容
	res = remove(strvar)
	# print(res)
	res2 = calc_exp(res)
	print(res2)

main(strvar)