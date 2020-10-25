import re
strvar = '1-2*(-5-6/-2*2)+(40 -  7)'  #32.0
# strvar = '1-2*((60-30+-8*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'  #2776672.6952380957
# print(eval(strvar)) #2776672.6952380957  验算




def operate_sign(strvar):
	strvar = strvar.replace('--','+')
	strvar = strvar.replace('++','+')
	strvar = strvar.replace('-+','-')
	strvar = strvar.replace('+-','-')
	return strvar

def calc_res(strvar):#6/-2
	if '*' in strvar:
		a,b = strvar.split('*')
		res = float(a) * float(b)
		return res
	elif '/' in strvar:
		a,b = strvar.split('/')
		res = float(a) / float(b)
		return res

def calc_add(strvar):
	lst = re.findall(r'[+-]?\d+(?:\.\d+)?',strvar)  # 正则3
	print(lst)  #['-5', '+6.0']
	total = 0
	for i in lst:
		total += float(i)
	print(total)  #1.0
	return total
	
# 计算最内层括号的值
def calc_exp(strvar):    #(-5-6/-2*2)
	while True:
		obj = re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?',strvar)  # 正则2
		# print(obj) #<_sre.SRE_Match object; span=(4, 8), match='6/-2'>
		if obj:
			multi_div = obj.group()
			print(multi_div) #6/-2
			
			multi_div_res = calc_res(multi_div)
			print(multi_div_res)  #-3.0
			
			strvar = strvar.replace(multi_div,str(multi_div_res))
			print(strvar)
			#(-5--3.0*2)
			# (-5--6.0)
		else:
			break
			
	strvar = operate_sign(strvar)
	print(strvar)  #(-5+6.0)
	
	res = calc_add(strvar)
	print(res) #1.0
	return res


# 去括号
def remove_bracket(strvar):
	while True:
		obj = re.search(r'\([^\(\)]+\)',strvar)  #正则1
		# print(obj) #<_sre.SRE_Match object; span=(4, 15), match='(-5-6/-2*2)'>
		if obj:
			bracket = obj.group()
			print(bracket)  #(-5-6/-2*2)
			
			bracket_res = calc_exp(bracket)
			print(bracket_res)  #1.0
			
			strvar = strvar.replace(bracket,str(bracket_res))
			# print(strvar)
			#1-2*1.0+(40-7)
			#1-2*1.0+33.0
		else:
			break
			
	return strvar
	
	
# 主函数调用
def main(strvar):
	strvar = strvar.replace(' ','')
	print(strvar)  #1-2*(-5-6/-2*2)+(40-7)
	
	res = remove_bracket(strvar)
	print(res)  #1-2*1.0+33.0
	
	res2 = calc_exp(res)
	print(res2)
	return res2

res = main(strvar)
print(res)  #32.0
#1-2*(-5-6/-2*2)+(40-7)





































