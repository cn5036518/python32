# ''''''
# '''

# ### 字符串相关练习
1.有变量name = "aleX leNb" 完成如下操作：

移除 name 变量对应的值两边的空格,并输出处理结果
1)移除name变量左边的"al"并输出处理结果
2)移除name变量右面的"Nb",并输出处理结果
3)移除name变量开头的a与最后的"b",并输出处理结果
4)判断 name 变量是否以 "al" 开头,并输出结果
5)判断name变量是否以"Nb"结尾,并输出结果
6)将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
7)将name变量对应的值中的第一个"l"替换成"p",并输出结果
8)将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
9)将name变量对应的值根据第一个"l"分割,并输出结果。
10)将 name 变量对应的值变大写,并输出结果
11)将 name 变量对应的值变小写,并输出结果
12)将name变量对应的值首字母"a"大写,并输出结果
13)判断name变量对应的值字母"l"出现几次，并输出结果
14)如果判断name变量对应的值前四位"l"出现几次,并输出结果
15)从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
16)从name变量对应的值中找到"N"对应的索引(如果找不到则返回-1)输出结果
17)从name变量对应的值中找到"X le"对应的索引,并输出结果
18)请输出 name 变量对应的值的第 2 个字符?
19)请输出 name 变量对应的值的前 3 个字符?
20)请输出 name 变量对应的值的后 2 个字符?
21)请输出 name 变量对应的值中 "e" 所在索引位置?

2.实现一个整数加法计算器(两个数相加)：
如：content = input("请输入内容:") 用户输入：5+9或3+ 9或5 + 6，然后进行分割再进行计算

3.升级题：实现一个整数加法计算器（多个数相加）：
如：content = input("请输入内容:") 用户输入：5+9+6 +12+  13，然后进行分割再进行计算。

4.计算用户输入的内容中有几个整数（以个位数为单位）。
如：content = input("请输入内容：")   # 如fhdal234slfh98769fjdla

5.等待用户输入内容，是否包含敏感字符？
如果存在敏感字符提示“存在敏感字符请重新输入”，敏感字符：“粉嫩”、“铁锤”


6.制作趣味模板程序需求：等待用户输入名字、地点、爱好
拼装数据打印出：敬爱可亲的xxx，最喜欢在xxx地方xxx


# ### 列表相关练习
1.li = ["alex", "WuSir", "xboy", "oldboy"]
1)列表中追加元素"seven",并输出添加后的列表
2)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
3)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
4)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行
代码实现，不允许循环添加。
5)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
6)请删除列表中的元素"alex",并输出添加后的列表
7)请删除列表请删除列表中的第2至4个元素，并输出删除元素后的列表
8)删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
9)请将列表所有得元素反转，并输出反转后的列表
10)请计算出"alex"元素在列表li中出现的次数，并输出该次数。

2，写代码，有如下列表，利用切片实现每一个功能
li = [1, 3, 2, "a", 4, "b", 5,"c"]
1)通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
2)通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
3)通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
4)通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
5)通过对li列表的切片形成新的列表l5,l5 = ["c"]
6)通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]

3,写代码，有如下列表，按照要求实现每一个功能。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
1)将列表lis中的"tt"变成大写。
2)将列表中的数字3变成字符串"100"。
3)将列表中的字符串"1"变成数字101

4,li = ["alex", "eric", "rain"]
利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"

5.利用for循环打印出下面列表的索引。
li = ["alex", "WuSir", "xboy", "oldboy"]

6.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。

7.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来

8.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
li = ["xboy ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]

9.敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到新列表中。

10.li = [1, 3, 4, "alex", [3, 7, “23aa”,8, "xboy"], 5,(‘a’,’b’)]
循环打印列表中的每个元素,并转化为小写，遇到列表则再循环打印出它里面的元素。


11.tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
a.讲述元组的特性
b.请问tu变量中的第一个元素 "alex" 是否可被修改？
c.请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
d.请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"



# '''























