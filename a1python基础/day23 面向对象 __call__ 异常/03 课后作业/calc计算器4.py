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
	if "*" in strvar:
		a,b = strvar.split('*')  #str
		res = float(a) * float(b)
		return res
	elif '/' in strvar:
		a,b = strvar.split('/')  #str
		res = float(a) / float(b)
		return res
		

# 计算加减表达式的值
def calc_add(strvar):	 
	pass

		
# 匹配计算出对应的表达式(括号内的值)
# 2.计算最里层小括号里面的数值
def calc_exp(strvar):  #(-5-6/-2*2)
    #01 计算乘除
	while True:
		#1 先用正则匹配出第一个乘除表达式   正则2
		# [+-]? 匹配*/后面数的符号是正负
		obj = re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?',strvar)
		# print(obj) #<_sre.SRE_Match object; span=(4, 8), match='6/-2'>
		if obj:
			chengchu = obj.group()
			print(chengchu)  #6/-2
			
			# 2计算乘除表达式的值
			chengchu_res = calc_res(chengchu)
			print(chengchu_res) #-3.0
			
			# 3 用乘除表达式的计算结果替换乘除表达式  replace
			strvar = strvar.replace(chengchu,str(chengchu_res))   #产生新str
			print(strvar) #(-5--3.0*2)  #第一次循环   这里的strvar必须和35行的strvar保持一致 注意点1
			# (-5--6.0)  #第二次循环
			
			# 4用正则匹配出第一个乘除表达式 走32行 while True
			 
		else:
			break  #如果没有匹配到乘除表达式,就跳出死循环
			
	#02 去除多余的符号
	strvar = operate_sign(strvar)
	print(strvar)  #(-5--6.0)   ==>  (-5+6.0)
	
	#03 计算加减
	# 加减表达式可能是  -1+2-3+4   即不止2个数  有负数,所以用-分割可能不行
	# 用正则匹配出2个或多个数的加减表达式    正则3  findall
	#r'[+-]\d+(?:\.\d+)?'
	# [+-]? 匹配的是正负号,而不是加减号  ?是0或1 可以是0
	# \d+(?:\.\d+)?  匹配整数和小数
	# ?: 会去掉小括号内的优先显示
	lst = re.findall(r'[+-]?\d+(?:\.\d+)?',strvar)
	print(lst)  #['-5', '+6.0']
	
	total = 0
	for i in lst:
		total += float(i)
	print(total)  #1.0
	return total	
	

# 去除括号 
# 1.通过正则匹配到最里层小括号
def remove_bracket(strvar):
	pass
		# 1.通过正则匹配到第一个最里层小括号
	# 2.计算括号里面的数值
	# 3.拿算好的数值替换原来的小括号
	# 4.循环再去匹配下一个(第二个)最里层小括号,依次类推 ...	
	
	while True:
		obj = re.search(r'\([^\(\)]+\)',strvar) #正则1
		print(obj) 
		#<_sre.SRE_Match object; span=(4, 15), match='(-5-6/-2*2)'>
		if obj:
			bracket = obj.group()
			print(bracket)  #(-5-6/-2*2)
			
			# 2.计算括号里面的数值
			bracket_res = calc_exp(bracket)
			print(bracket_res)  #1.0
			
			# 3.拿算好的数值替换原来的小括号  replace
			# 原来 	#1-2*(-5-6/-2*2)+(40-7)
			strvar = strvar.replace(bracket,str(bracket_res))
			print(strvar)
			#1-2*1.0+(40-7) 第一次循环
			#1-2*1.0+33.0  第二次循环
		else:
			break  #没有小括号,就退出死循环
			
			# 4.循环再去匹配下一个(第二个)最里层小括号,依次类推 ...	 走90行  while True
	
	#5 拿最后没有小括号的表达式调
	#计算最后一次没有括号的那个表达式的结果
	# #1-2*1.0+33.0
	res = calc_exp(strvar)
	return res
	
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
	print(res)

	
	# 03计算最后一次没有括号的那个表达式的结果


res = main(strvar)
print(res)  #32.0
#1-2*(-5-6/-2*2)+(40-7)





































