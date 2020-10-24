import re
strvar = '1-2*(-5-6/-2*2)+(40 -  7)'  #32.0
# strvar = '1-2*((60-30+-8*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'  #2776672.6952380957
# print(eval(strvar)) #2776672.6952380957  验算


# 去除多余的符号
def operate_sign(strvar):
	strvar = strvar.replace('--','+')
	strvar = strvar.replace('++','+')
	strvar = strvar.replace('-+','-')
	strvar = strvar.replace('+-','-')
	return strvar
	
# 计算乘除表达式的值
def calc_res(strvar):
	if '*' in strvar:
		a,b = strvar.split('*')
		res = float(a) * float(b)
		return res
	elif '/' in strvar:
		a,b = strvar.split('/')
		res = float(a) / float(b)
		return res	

# 计算加减表达式的值
def calc_add(strvar):	 
# -5+6.0  有负号,不能直接用-+分割,需要用正则匹配
	lst = re.findall(r'[+-]?\d+(?:\.\d+)?',strvar)
	print(lst) #['-5', '+6.0']
	return lst

		
# 匹配计算出对应的表达式(括号内的值)
def calc_exp(strvar):  #(-5-6/-2*2)
	while True:
		#1 将乘除表达式匹配出来  #正则2
		obj = re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?',strvar)
		# print(obj)  #<_sre.SRE_Match object; span=(8, 12), match='6/-2'>
		if obj:
			res1 = obj.group()
			print(res1)  #6/-2
			
			res2 = calc_res(res1)
			print(res2)  #-3.0
			
			strvar = strvar.replace(res1,str(res2))
			print(strvar,'-----1')
			# (-5--3.0*2) -----1  #第一次循环
			# (-5--6.0) -----1    #第二次循环			
		else:
			break
			
	#2 计算加减
	# 去除多余的符号
	strvar = operate_sign(strvar)
	print(strvar)  #(-5+6.0)
	
	lst = calc_add(strvar)  #['-5', '+6.0']
	
	total = 0
	for i in lst:
		total += float(i)
	print(total)  #1.0
	return total  #1.0
	

# 去除括号
def remove_bracket(strvar):
		# 1.通过正则匹配到最里层小括号
	# 2.计算括号里面的数值
	# 3.拿算好的数值替换原来的小括号
	# 4.循环再去匹配下一个小括号,依次类推 ...     while
	while True:
		obj = re.search(r'\([^\(\)]+\)',strvar)  #正则1
		# print(obj)  #<_sre.SRE_Match object; span=(4, 15), match='(-5-6/-2*2)'>
		if obj:
		#   1 通过正则匹配到最里层小括号
			res1 = obj.group()
			print(res1)  #(-5-6/-2*2)
			
			# 2 计算括号里面的数值
			res2 = calc_exp(res1)  #1.0
			
			#3.拿算好的数值替换原来的小括号
			strvar = strvar.replace(res1,str(res2))
			print(strvar)
			return strvar
			#1-2*1.0+(40-7)  #第一次循环
			# 1-2*1.0+33.0  #第二次循环			
		else:
			# pass
			break  #没有小括号,就跳出循环
	
	


# 主函数调用
def main(strvar):
	# 0.先去掉字符串当中出现的空格
	# 1.通过正则匹配到最里层小括号
	# 2.计算括号里面的数值
	# 3.拿算好的数值替换原来的小括号
	# 4.循环再去匹配下一个小括号,依次类推 ...	

	# 01先去掉字符串当中出现的空格
	strvar = strvar.replace(' ','')
	print(strvar)
	#1-2*(-5-6/-2*2)+(40-7)
	
	# 02移除表达式中的所有括号
	res = remove_bracket(strvar)

	#1-2*1.0+33.0 res   main ...
	
	# 03计算最后一次没有括号的那个表达式的结果
	res = calc_exp(res)
	return res

res = main(strvar)
print(res)  #32.0
#1-2*(-5-6/-2*2)+(40-7)





































