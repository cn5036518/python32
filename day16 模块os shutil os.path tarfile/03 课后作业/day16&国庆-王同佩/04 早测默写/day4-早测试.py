# 1.布尔值为假的十中情况
numbers
	int    0
	float	0.0
	bool 	False
	complex  0j

容器
	str   	''
	tuple	()      逗号
	list    []
	dict	{}
	set     set()
None 

# 2.True和False 在强制转换为int float complex时的值
	  int float complex
True   1   1.0	1+0j
False  0   0.0   0j


# 3. Number的自动类型转换原则
从低精度到高精度自动转换
bool==>int==>float==>complex

# 4.容器类型转换的特点
容器
	str   	
		可以转换任意类型,两边加上引号  eval  json
		
	tuple	
		str  把字符串的每个字符,单独拿出来,作为元组的元素
		dict  把dict的键拿出来,作为元组的元素			
		list/set 把两端的[]或者{}换成()	
	
	list    
		str  把字符串的每个字符,单独拿出来,作为list的元素
		dict  把dict的键拿出来,作为list的元素			
		tuple/set 把两端的()或者{}换成[]	
		
	dict	
		1 等长的二级容器且  --nok
		2 二级容器的长度是2
		
		外层是列表,元组, 里层是列表或者元组的等长二级容器
		外层是集合 , 里层是元组的等长二级容器
		
		lst = [ ["a",1] , ("b",2) ]
		dic = dict(lst)
		print(dic , type(dic)) # {'a': 1, 'b': 2} <class 'dict'>
	
	set   
		str  把字符串的每个字符,单独拿出来,作为set的元素
		dict  把dict的键拿出来,作为set的元素			
		tuple/list 把两端的()或者[]换成{}

# 5.写一个等长的二级容器
	lst = [[1,2],(3,4)]

# 6.什么样的类型可以转化成字典
	dict	
		1 等长的二级容器且 
		2 二级容器的长度是2
		
		外层是列表,元组, 里层是列表或者元组的等长二级容器
		外层是集合 , 里层是元组的等长二级容器
		
		lst = [ ["a",1] , ("b",2) ]
		dic = dict(lst)
		print(dic , type(dic)) # {'a': 1, 'b': 2} <class 'dict'>

# 7.[1，2,3，4,[5，6,7,[8，9,10，(11，{ "a":{ "bb":98}，"pp": { "d" :'bingo'})]]]获取bingo
lst = [1，2,3，4,[5，6,7,[8，9,10，(11，{ "a":{ "bb":98}，"pp": { "d" :'bingo'})]]]
lst[-1][-1][-1][-1]['pp']['d']

# 8.判断类型的方法有几个
type
isinstance(数据,(str,list,tuple,set,dict)) #推荐




















