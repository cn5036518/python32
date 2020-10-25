import re
strvar = '1-2*(-5-6/-2*2)+(40 -  7)'  #32.0
# strvar = '1-2*((60-30+-8*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'  #2776672.6952380957
# print(eval(strvar)) #2776672.6952380957  验算



# 去掉多余符号  -- ==> +
def operate_sign(strvar):
	strvar = strvar.replace('--','+')
	strvar = strvar.replace('++','+')
	strvar = strvar.replace('-+','-')
	strvar = strvar.replace('+-','-')
	return strvar

	
# 计算乘除
def calc_res(strvar):
	if '*' in strvar:
		a,b = strvar.split('*')
		res = float(a) * float(b)
		return res
	elif '/' in strvar:
		a,b = strvar.split('/')
		res = float(a) / float(b)
		return res	

		
# 计算小括号里面的值
def calc_exp(strvar):  #(-5-6/-2*2)
	while True:
		# 3 计算最内层小括号内表达式的值  
	#a 计算乘除表达式
		# 01匹配第一个乘除表达式  正则2
		obj = re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?',strvar)
		# print(obj)  #<_sre.SRE_Match object; span=(4, 8), match='6/-2'>
		if obj:
			chengchu = obj.group()
			print(chengchu) #6/-2	
		
		# 02计算乘除表达式的值
			chengchu_res = calc_res(chengchu)
			print(chengchu_res)  #-3.0
		
		# 03 将02步的值替换01步的乘除表达式
			strvar = strvar.replace(chengchu,str(chengchu_res))
			print(strvar) #(-5--3.0*2)  #第一次循环
			#(-5--6.0)  第二次循环
		
		# 04 匹配下一个乘除表达式,直到没有乘除表达式,退出死循环
		else:
			break
			
	#b 去掉多余的符号
	strvar = operate_sign(strvar)
	print(strvar)  #(-5+6.0)
	
	#c 计算加减表达式
	# 01匹配两个或者多个数表达式  正则3
	lst = re.findall(r'[+-]?\d+(?:\.\d+)?',strvar)
	print(lst)  #['-5', '+6.0']
	
	total = 0
	for i in lst:
		total += float(i)
	# print(total) #1.0
	return total
	
	


# 去掉小括号
def remove_bracket(strvar):
		# 2 匹配出第一个最内层小括号  正则1
	# 3 计算最内层小括号内表达式的值  
		# 匹配乘除表达式  正则2
		# 匹配出多个数的加减表达式  正则3
	# 4 用第3步的值,替换第一个最内层小括号内的表达式
	# 5 回到第2步,循环找下一个最内层小括号
	
			# 2 匹配出第一个最内层小括号  正则1
			# 01 小括号开头,小括号结尾
			# 02 中间没有小括号
			# 03 两个小括号之间的字符不是空
			
	while True:
		obj = re.search(r'\([^\(\)]+\)',strvar)	
		print(obj)  #<_sre.SRE_Match object; span=(4, 15), match='(-5-6/-2*2)'>
		
		if obj:
			bracket = obj.group() 
			print(bracket) #(-5-6/-2*2)
				
			bracket_res = calc_exp(bracket)
			print(bracket_res)  #1.0
		# 3 计算最内层小括号内表达式的值  
			# 匹配乘除表达式  正则2		
			# 匹配出多个数的加减表达式  正则3
			
			# 4 用第3步的值,替换第一个最内层小括号内的表达式
			strvar = strvar.replace(bracket,str(bracket_res))
			print(strvar)  #1-2*1.0+(40-7)	  #第一次循环
			# 1-2*1.0+33.0  #第二次循环
	
		# 5 回到第2步,循环找下一个最内层小括号,直到没有小括号,退出死循环
		else:
			break #
			
	return strvar
	
	
# 主函数调用
def main(strvar):
	# 1 去掉多余的空格
	# 2 匹配出第一个最内层小括号  正则1
	# 3 计算最内层小括号内表达式的值  
		# 匹配乘除表达式  正则2
		# 匹配出多个数的加减表达式  正则3
	# 4 用第3步的值,替换第一个最内层小括号内的表达式
	# 5 回到第2步,循环找下一个最内层小括号
	# 6 直到没有小括号,最后走第3步
	
	# 1 去掉多余的空格
	strvar = strvar.replace(' ','')
	print(strvar)  #1-2*(-5-6/-2*2)+(40-7)	
	
	# 2 匹配出第一个最内层小括号  正则1
	res = remove_bracket(strvar)
	print(res) #1-2*1.0+33.0
	
	# 6 直到没有小括号,最后走第3步
	res2 = calc_exp(res)
	print(res2) #32.0
	return res2


res = main(strvar)
print(res)  #32.0
#1-2*(-5-6/-2*2)+(40-7)





































