# 2.1 python认知
###(1)python简介
    # 89年开发的语言,创始人范罗苏姆(Guido van Rossum),别称:龟叔(Guido).
    # python具有非常多并且强大的第三方库,使得程序开发起来得心应手.
    # python程序员的信仰:人生苦短,我用python!
    # 开发方向:机器学习人工智能,自动化运维&测试,数据分析&爬虫,python全栈开发
    
###(2)python版本
    # python 2.x 版本,官方在2020年停止支持,原码不规范,重复较多.
    # python 3.x 版本,功能更加强大且修复了很多bug,原码清晰,简单
    
###(3)编译型与解释型语音区别
    # 编译型:一次性,把所有代码编译成机器能识别的二进制码,再运行
        # 代表语音:c,c++
        # 优点:执行速度快
        # 缺点:开发速度慢,调试周期长
        
    # 解释型:代码从上到下一行一行解释并运行
        # 代表语音:python,php
        # 优点:开发效率快,调试周期短
        # 缺点:执行速度相对慢
    # *linx 操作系统默认支持python语言,可直接使用
    
###(4)python的解释器:
    # (1)Cpython(官方推荐)    
        # 把python转化成c语言能识别的二进制码
    # (2)Jpython
        # 把python转化成java语言能识别的二进制码
    # (3)其他语言解释器
        # 把python转化成其他语言能识别的二进制码
    # (4)pypy
        # 将所有代码一次性编译成二进制码,加快执行效率
        # (模仿编译型语言的一款python解释器)

# 2.2 注释:就是对代码的解释 方便大家阅读python代码
# (1)注释的分类
# (2)注释的注意点
# (3)注释的排错性

# (1)注释的分类:1.单行注释  2.多行注释
    # 1.单行注释  
        # 以#号开头,右边的所有东西都被当做说明文字,程序不进行编译运行.
    # print('hello world')
    
    # 2.多行注释
        # 三个单引号 或 三个双引号
        # """
        # 这是第一行
        # 这是第二行
        # """
        
# (2)注释的注意点
    # 如果外面使用三个单引号,里面使用三个双引号,反之亦然.
    
# (3)注释的排错性
    # 先注释一部分代码,然后执行另外一部分,看看是否报错,逐层缩小范围,
    # 找到最终错误点

# 2.3变量:可以改变的量,实际具体指的是内存中的一块存储空间
# (1) 变量的概念
# (2) 变量的声明
# (3) 变量的命名
# (4) 变量的交换

# *常量就是不可改变的量,python当中没有明确定义常量的关键字.
 # 所以约定俗成把变量名大写就是常量,表示不可改变
 
 # (1)变量的概念:
    # 可以改变的量就是变量.具体指代的是内存的一块空间
 # (2)变量的声明:
    # 1. a=1,b = 2
    # 2. a,b = 1,2
    # 3. a = b = 3
 # (3)变量的命名:
    # 字母数字下划线,首字母不能为数字
    # 严格区分大小写,且不能使用关键字
    # 变量命名有意义,且不能使用中文哦
 # (4)变量的交换:
    # a,b = b,a

# 2.4 python六大标准数据类型:
### 数据类型分类:
# (1)Number 数字类型(int float bool complex)
# (2)str    字符串类型
# (3)list    列表类型
# (4)tuple    元组类型
# (5)set      集合类型
# (6)dict     字典类型

### Number数字类型分类:
# int:        整数类型 (正整数 0 负整数)
# float:      浮点数类型(1普通小数  2科学计数法表示的小数 例: a = 3e-5)
# bool:       布尔值类型(真 True 和假 False)
# complex:    复数类型(声明复数的2种方法)(复数用作于科学计算中,表示高精度的数据,科学家会使用)

### 容器类型分类:五个
# str     "nihao"
# list    [1,2,3]
# tuple   (6,7,8)
# set     {'a',1,2}
# dict    {'a':1,'b':2}

# 2.4.1自动类型转换
# 当2个不同类型的数据进行运算的时候,默认向更高精度转换
# 数据类型精度从低到高: bool int float complex

# 2.4.2强制类型转换
# --> Number部分
# int:    浮点型  布尔类型  纯数字字符串
# floatL  整型    布尔类型   纯数字字符串
# complex:    整型  浮点型 布尔类型   纯数字字符串

# --> 容器类型部分
# str:    (容器类型数据 / Number类型数据 都可以)
# list:   字符串  元组  集合 字典
# tuple:  字符串 列表   集合 字典
# set:     字符串    列表  元组   字典 (注意:相同的值,只会保留一份)
# dict:   使用 二级列表,二级元组,二级集合(里面的容器数据只能是元组)

# 2.4.3 字典和集合的注意点
### 哈希算法
# 定义:
    # 把不可变的任意长度值计算成固定长度的唯一值,这个值可正可负,可大可小,但长度固定
    # 该算法叫做哈希算法(散列算法),这个固定长度值叫哈希值(散列值)
    
# 特点:
    # 1.计算出来的值长度固定且该值唯一
    # 2.该字符串是密文,且加密过程不可逆
    
# 用哈希计算得到一个字符串的用意?
    # 例如:比对两个文件的内容是否一致?
    # 例如:比对输入的密码和数据库存储的密码是否一致
    
# 字典的键和集合中的值都是唯一值,不可重复:
    # 为了保证数据的唯一性,
    # 用哈希算法加密字典的键得到一个字符串.
    # 用哈希算法加密集合的值得到一个字符串.自动去重
    
# 版本:
    # 3.6版本之前都是 字典和集合都是无序的
    # 3.6版本之后,把字典的字面顺序记录下来,当从内存拿数据的时候,
    # 根据字面顺序重新排序,所以看起来像有序,但本质上无序
    
# 可哈希的数据(不可变的数据):
    # number(int float bool complex) tuple str
# 不可哈希的数据(可变的数据):
    # list    set  dict

# 2.5 python运算符
# (1)算数运算符
    # + - * / // % **
    
# (2) 比较运算符
    # > < >= <=  == !=
    
# (3) 赋值运算符
    # = += -= *= /= //= %= **=
    
# (4) 成员运算符
    # in 和 not in (针对于容器型数据)
    
# (5) 身份运算符:
    # is 和 is not (检测两个数据在内存当中是否是同一个值)
    
# (6) 逻辑运算符:
    # and or not
    
# (7) 位运算符
    # &  |  ~  ^ <<   >>
    
# 算数运算符
    # %取余   //地板除  **幂运算
    
# 比较运算符
    # == 比较两个值是否相等
    # != 比较两个值是否不同
    
# 赋值运算符
    # a +=1 ==> a = a + 1
    
# 成员运算符:
    # in 或者 not in 判断某个值是否包含在(或不在)一个容器类型数据当中
    
# 身份运算符:
    # is 和 is not 用来判断内存地址是否相同
    
# 逻辑运算符:
    # 优先级  () > not > and > or
    
# 位运算符:
    # 优先级
     # (<< 或 >>) > & > ^ > |
     # 5 << 1 结果: 10
     # 5 >> 1 结果: 2

# 2.6 数据在内存中的缓存机制
# 2.6.1 在同一文件(模块)里,变量存储的缓存机制 (仅对python3.6版本负责)  

# --> Number 部分
# 1.对于整型而言, -5 ~ 正无穷大范围内的相同值id一致
# 2.对于浮点数而言,正浮点数 和 0.0 0.00...范围内的相同值id一致
# 3.布尔值而言,值相同情况下,id一致
# 4.复数在 实数 + 虚数 这样的结构中永不相同(只有正虚数的情况例外)

# --> 容器类型部分
# 5.字符串 和 空元组 值相同的情况下.id地址相同
# 6.列表,元组,字典,集合无论什么情况下,id都不同(空元组例外)





























