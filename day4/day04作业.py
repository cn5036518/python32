''''''
'''
1.99//4  ,  99%4 ,  -99 %4  ,  -99 %-4值是多少
    99//4 =24
    99%4 = 3
    -99%4 = 1   
    -99%-4 = -3   #两个负数,正常结果加上-

2.成员和身份运算符如何使用
    成员运算符  in 和not in
        in用于容器类型的数据,判断一个数据是否是容器的一个元素,如果是,返回True,否则,返回False
        not in用于容器类型的数据,判断一个数据是否不是容器的一个元素
            str
            tuple
            list
            set
            dict 判断一个数据是否是字典的键

3.逻辑运算符优先级?逻辑短路在什么情况下发生?
    () > not > and >or
    逻辑短路:
        True or, 不管后面接的是什么,最终结果都是True
        Flase and,不管后面接的是什么,最终结果都是False
        上述2个情况会出现逻辑短路,会直接返回前者,后面的代码就不执行了

4.优先级最高和最低的运算符是?
    优先级最高的是:**(幂运算)
    优先级最低的是: =(赋值运算符)    

5.左移右移后的值如何计算?按位非的公式?
   左移的计算:
       做乘法,n乘以2的n次幂
   
   右移的计算:
      做除法,n除以2的n次幂
   
   按位非的计算:
       -(n+1)  

6.~(-25) ~25 推导一下过程
    -25   负数 符号位1 三码不一致
    原码: 100... 011001
    反码: 111... 100110   #取反符号位不变
    补码: 111... 100111   #
    
     补码:   111... 100111
    按位非:  000... 011000    #符号位也取反,每位都取反
                              符号位是0,正数,三码一致

    补码:000... 011000 
    反码:000... 011000 
    原码: 000... 011000   #24
    
      25   正数 符号位0 三码一致
    原码: 000... 011001
    反码: 000... 011001
    补码: 000... 011001
    
     补码:   000... 011001
    按位非:  111... 100110   #符号位也取反,每位都取反
                              

    补码:111... 100110    #符号位是1 负数,三码不一致
    反码:100... 011001    #取反符号位不变
    原码:100... 011010   #-26

7.res = 17>15 or 78<11 or 7 and 8 and not True is True  res=?
    res = 17>15 or 78<11 or 7 and 8 and not True is True 
    res = True or False or 7 and 8 and False is True   #is(身份运算符) > and(逻辑运算符)
    res = True or False or 7 and 8 and False    # and > or
    res = True or False or  8 and False
    res = True or False or False
    res = True  or False
    res = True   #已经验证--ok

8.计算表达式的值
    True or 和False and 逻辑短路

    1).6 or 2 > 1    
        6 or True ==>6
      
    2).3 or 2 > 1    
        3 or True ==>3
      
    3).0 or 5 > 4  
        0 or True ==> True
        
    4).5 < 4 or 3    
        False or 3 ==>3   
          
    5).2 > 1 or 6    
        True or 6 ==> True    
      
    6).3 and 2 > 1    
        3 and True ==>True    
     
    7).0 and 3 > 1    
        0 and True ==> 0
            
    8).2 > 1 and 3   
        True and 3 ==>3
         
    9).3 > 1 and 0    
        True and 0 ==>0
    
    10).3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
        True and 2 or True and 3 and 4 or True  # and > or
        2 or 3 and 4 or True
        2 or 4 or True
        2 or True  ==>2
        2        
    
    11)not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
        False and True or False and True and True or False
        True or False  and True or False  # and > or
        True or False  or False  # and > or
        True   or False  #  ==>True
        True  # 
    
    True or 和False and 逻辑短路
    
9.提示用户输入 "如何在dnf中变得更强?". 如果输入的是充钱,打印"马化腾爱你" ,反之输出,"你想一想,不充钱怎么可能变得更强"
'''

content = input('如何在dnf中变得更强?')
if content == '充钱':
    print('马化腾爱你')
else:
    print('你想一想,不充钱怎么可能变得更强')

res = 17>15 or 78<11 or 7 and 8 and not True is True
print(res)



















