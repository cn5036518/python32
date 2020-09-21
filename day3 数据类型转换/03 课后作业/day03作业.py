''''''

'''
1.int,float,complex,bool 分别可以强转哪些数据
  int (float bool 纯数字字符串)
  float (int bool 纯数字字符串)
  complex (int float bool 纯数字字符串)
  bool (任意数据类型)

2.强转布尔类型为假的值有哪些?
    number
        int  0
        float  0.0
        bool   False
        complex  0j
    str    ''
    tuple   ()
    list    []
    set     set()
    dict    {}

3.强转字典的条件
    #必须是等长的二级容器,并且里面的元素个数是2个

4.bingo如何获取
setlist = [1,2,3,4,[5,6,7,[8,9,10,(11,{"a":{"bb":98},"pp":{"d":'bingo'}})]]] 
print(setlist[-1][-1][-1][-1]['pp']['d'])

5. 哪个不能转换成字典,为什么?  #第四个
    (1){('a',1),{'b',2}}
    (2){('a',1),('b',2)}
    (3){('a',1),"c3"}  #{'a': 1, 'c': '3'}  #这个可以
    (4){('a',1),"b88"}  #必须是等长的二级容器,并且里面的元素个数是2个
    #ValueError: dictionary update sequence element #0 has length 3; 2 is required
'''

setlist = [1,2,3,4,[5,6,7,[8,9,10,(11,{"a":{"bb":98},"pp":{"d":'bingo'}})]]]
print(setlist[-1][-1][-1][-1]['pp']['d'])

setvar = {('a',1),"b88"}
setvar = {('a',1),"c3"}
dic = dict(setvar)
print(dic)


strvar = 'jack'
res = '_'.join(strvar)
print(res)  #j_a_c_k

strdict = {'name':'jack','age':18}
res = '-'.join(strdict)
print(res)  #name-age





