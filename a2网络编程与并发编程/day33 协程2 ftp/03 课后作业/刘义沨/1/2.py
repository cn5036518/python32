import re

def chengchu(strvar):
	if "*" in strvar:
		a, b = strvar.split("*")
		return float(a) * float(b)
	if "/" in strvar:
		a, b = strvar.split("/")
		return float(a) / float(b)


def jisuan(strvar):
	while True:
		obj = re.search("\d+(\.\d+)?[*/]\d+(\.\d+)?", strvar)
		if obj:
			res1 = obj.group()

			res2 = chengchu(res1)
			strvar = strvar.replace(res1, str(res2))
		else:
			break
	total = 0

	lst = re.findall("[+-]?\d+(?:\.\d+)?", strvar)

	for i in lst:
		total += float(i)
	return total


def main(strvar):
	obj = re.search("\([^()]+\)", strvar)

	strvar = obj.group()

	return jisuan(strvar)


strvar = "3+(5*4+4/3-(3-8/2*2))"
res = main(strvar)
print(res)