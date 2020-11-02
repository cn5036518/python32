# 2.取出当前表达式最里层小括号的值3+(5*4+4/3-(3-8/2*2))并计算结果
import re

def calc_exp(strvar):
	while True:
		obj = re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?',strvar)
		if obj:
			multi_div = obj.group()
			print(multi_div)
			
			multi_div_res = calc_multi_div(multi_div)
			print(multi_div_res)
			
			strvar = strvar.replace(multi_div,str(multi_div_res))
			print(strvar)
			#(-5--3.0*2)
			#(-5--6.0)
		else:
			break
			
	# strvar = operate_sign(strvar)
	# print(strvar)  #(-5+6.0)
	
	calc_add_res = calc_add(strvar)
	print(calc_add_res)  #1.0
	
	return calc_add_res  #1.0

# 乘除
def calc_multi_div(strvar):  #6/-2  ===> -3.0
	if '*' in strvar:
		a,b = strvar.split('*')
		res = float(a) * float(b)
		return res   #-3.0
	elif '/' in strvar:
		a,b = strvar.split('/')
		res = float(a) / float(b)
		return res

# 加减
def calc_add(strvar):  #(-5+6.0)  ===> 1.0
	lst = re.findall(r'[+-]?\d+(?:\.\d+)?',strvar)
	print(lst)  #['-5', '+6.0']
	
	total = 0
	for i in lst:
		total += float(i)
	print(total)  #1.0
	return total   #1.0


# 去掉多余符号
# def operate_sign(strvar):
	# strvar = strvar.replace('--','+')
	# strvar = strvar.replace('++','+')
	# strvar = strvar.replace('-+','-')
	# strvar = strvar.replace('+-','-')
	# return strvar
	
strvar = '3+(5*4+4/3-(3-8/2*2))'
obj = re.search(r'\([^\(\)]+\)',strvar)
res2 = obj.group()
print(res2)  #(3-8/2*2)

res = calc_exp(res2)
print(res)  #-5














