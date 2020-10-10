# 1预定义字符集
# 2字符组

# 1量词
# 2贪婪和非贪婪
# 3边界符
# 4 ^ $

# 1分组
# 2|
# 3 search
# group
# groups


# 1预定义字符集
.  匹配任意一个字符,除了\n换行符
\d 匹配一个数字   d digit
\D 匹配非数字
\w 匹配字母 数字 下划线 中文  w-word
\W 匹配非字母  数字 下划线 中文
\s 匹配空白字符(空格 \t \n \r)
\S 匹配非空白字符
\n 匹配换行符
\t 匹配制表符

# 2字符组
[abc]  匹配其中一个字符
[^abc] ^用在字符组中,表示除了
\转义 () [] {} ^ - 等
正则和字符串,加r,避免转义

# 1量词
?  0个或1个
+  1个或多个
*  0次或多次
{m,n} m到n次
{m}   重复m次
{m,}  重复至少m次

# 2贪婪和非贪婪
写法
贪婪:  .+量词
非贪婪 .+量词+?

概念
贪婪:  尽可能多的匹配
非贪婪:尽可能少的匹配,匹配到符合条件的,就作为列表的元素返回,接着匹配第二个,直到没有匹配的  findall

# 3边界符  \b   边界 空格
\b  转义符  退格  back
\b  边界符 

左边界  \bw
右边界  d\b

# 4 ^ $
^ 匹配整个字符串的开头
$ 匹配整个字符串的结尾
可以严格卡位数

# 1分组
()  小括号内是一个整体  
	默认只显示分组内的
	显示全部  (?: )

# 2|   ab|cd 或

# 3 search  遇到第一个满足条件的,就返回,不再匹配了,返回的是对象
# obj.group() : 获取匹配到的内容   多
# obj.groups(): 获取分组里面的内容  少





















































