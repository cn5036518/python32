import re
strvar = '1-2*((60-30+-8*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
def operate_sign(strvar):
   strvar = strvar.replace("--","+")
   strvar = strvar.replace("++","+")
   strvar = strvar.replace("-+","-")
   strvar = strvar.replace("+-","-")
   return strvar
def calc_res(strvar):
   if "/" in strvar:
      a,b = strvar.split("/")
      return float(a) / float(b)
   elif "*" in strvar:
      a,b = strvar.split("*")
      return float(a) * float(b)
def calc_exp(strvar):
   while True:
      obj = re.search(r"\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?",strvar)
      if obj:
         res1 = obj.group()
         res2 = calc_res(res1)
         strvar = strvar.replace(res1,str(res2))
      else:
         break
   strvar = operate_sign(strvar)
   lst = re.findall("[+-]?\d+(?:\.\d+)?",strvar)
   total = 0
   for i in lst:
      total += float(i)
   return total
def remove_bracket(strvar):
   while True:
      obj = re.search(r"\([^\(\)]+\)",strvar)
      if obj:
         res1 = obj.group()
         res2 = calc_exp(res1)
         strvar = strvar.replace(res1,str(res2))
      else:
         return strvar
def main(strvar):
   strvar = strvar.replace(" ","")
   res = remove_bracket(strvar)
   return calc_exp(res)
res = main(strvar)
print(res)