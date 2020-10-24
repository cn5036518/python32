import re
strvar = '1-2*(-5-6/-2*2)+(40 -  7)'  #32.0
# strvar = '1-2*((60-30+-8*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'  #2776672.6952380957
# print(eval(strvar)) #2776672.6952380957  验算


# 去除多余的符号
def operate_sign(strvar):
	strvar = strvar.replace('--','+')
	strvar = strvar.replace('-+','-')
	strvar = strvar.replace('+-','-')
	strvar = strvar.replace('++','+')
	return strvar
	
# 计算乘除表达式的值
def calc_res(strvar):
	if '*' in strvar:
		a,b = strvar.split('*')
		res = float(a) * float(b)
		return res
	elif "/" in strvar:
		a,b = strvar.split('/')
		res = float(a) / float(b)
		return res
		
# 匹配计算出对应的表达式
def calc_exp(strvar):
	print(strvar , "strvar ... ") # (-5-6/-2*2) 

	# ### part1 只计算乘除
	while True:  #循环匹配乘除  然后计算内括号表达式的值   #关键点1
			# 1.写一条正则匹配出乘除表达式 (2个int或者float相乘除)
			# \d+(\.\d+)? 匹配int或者float
			# [*/] 匹配乘除
			# [+-]? 匹配正负号
		obj = re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?',strvar)
		print(obj)  #<_sre.SRE_Match object; span=(4, 8), match='6/-2'>
		if obj:
			pass
			# 2.匹配出乘除表达式
			res = obj.group()
			print(res,type(res))  # #6/-2 <class 'str'>
			
			# 2.计算当前表达式的结果
			res2 = calc_res(res)
			print(res2)  #-3.0
			
			# 3.用结果替换原乘除表达式
			strvar = strvar.replace(res,str(res2))
			print(strvar)  #(-5--3.0*2)

			#(-5--3.0*2) strvar ... 1111  第一次循环
			#(-5--6.0) strvar ... 1111   第二次循环
		else:
			break
	
	# ### part2 只计算加减
	# 01把表达式当中多余的符号做一个替换
	strvar = operate_sign(strvar)
	print(strvar)  #(-5+6.0)
    #(-5+6.0) 2222
	
	# 02计算这个表达式+-结果
	# 将+-表达式中的符号前后的int或者float数匹配出来,放到列表
	lst = re.findall(r'[+-]?\d+(?:\.\d+)?',strvar)
	print(lst)  #['-5', '+6.0']
	
	# 03计算累加和
	total = 0
	for i in lst:
		total += float(i)
	print(total)  #1.0
	return total
	

# 去除括号
def remove_bracket(strvar):
	while True:  #循环匹配内括号  关键点2
				#匹配出第一个最里层的小括号里面的表达式  不用findall 用search
				# 最里层的小括号 :(开头,)结尾,中间没有()
				# ()有特殊含义,表示分组,\(\)转义
				#'1-2*(-5-6/-2*2)+(40 -  7)'   中的  (-5-6/-2*2)

		obj = re.search(r'\([^\(\)]+\)',strvar)  #正则1 匹配内层括号
		# print(obj)
			#<_sre.SRE_Match object; span=(4, 15), match='(-5-6/-2*2)'>
		if obj:
			pass
			# 匹配括号里面的表达式
			res1 = obj.group()  #(-5-6/-2*2)
			print(res1)
			#(-5-6/-2*2) res1 ... ... ..  
			
			# 计算括号里面的表达式
			res2 = calc_exp(res1)
			print(res2,'res2 ... remove_bracket')  #1.0
			#1.0 res2 ... remove_bracket
			
			# 用计算的结果替换原来的括号(及其里面的表达式)
			strvar = strvar.replace(res1,str(res2))
			print(strvar,'------1')  #1-2*1.0+(40-7) ------1

			#1-2*1.0+(40-7)	  #第一次循环
			# 1-2*1.0+33.0	  #第2次循环		
		else: #注意缩进
			return strvar  #括号去完了,只剩下表达式了


# 主函数调用
def main(strvar):
	# 0.先去掉字符串当中出现的空格
	# 1.通过正则匹配到最里层小括号
	# 2.计算括号里面的数值
	# 3.拿算好的数值替换原来的小括号
	# 4.循环再去匹配下一个小括号,依次类推 ...	

	# 先去掉字符串当中出现的空格
	strvar = strvar.replace(' ','')
	print(strvar)
	#1-2*(-5-6/-2*2)+(40-7)
	
	# 移除表达式中的所有括号
	res = remove_bracket(strvar)

	#1-2*1.0+33.0 res   main ...
	
	# 计算最后一次没有括号的那个表达式的结果
	res = calc_exp(res)
	return res

res = main(strvar)
print(res)  #32.0
#1-2*(-5-6/-2*2)+(40-7)





































