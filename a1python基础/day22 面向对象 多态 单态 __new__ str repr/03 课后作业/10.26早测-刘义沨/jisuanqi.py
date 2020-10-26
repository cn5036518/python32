import re 

def D(strvar):
    strvar=strvar.replace("--","+")
    strvar=strvar.replace("-+","-")
    strvar=strvar.replace("+-","-")
    strvar=strvar.replace("++","+")
    return strvar


def C(strvar):
    if "*" in strvar:
        a,b=strvar.split("*")
        return float(a) * float(b)
    elif "/" in strvar:
        a,b=strvar.split("/")
        return float(a) / float(b)
        
        
def B(strvar):

    while True:
        obj = re.search(r"\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?", strvar)
        if obj:
            res=obj.group()
            res1=C(res)
            strvar=strvar.replace(res,str(res1))
        else:
            break
    total = 0

    strvar=D(strvar)
    lst = re.findall(r"[+-]?\d+(?:\.\d+)?", strvar)
    for i in lst:
        total+=float(i)
    return total

def A(strvar):
    while True:
        obj = re.search(r"\([^()]+\)", strvar)
        if obj:
            res=obj.group()
            res1=B(res)
            strvar=strvar.replace(res,str(res1))
        else:
            return strvar
            
    
def main(strvar):
    strvar=strvar.replace(" ","")
    res=A(strvar)
    return B(res)

strvar="1+2*(4+5)/6-7+8"
res=main(strvar)
print(res)
print(eval(strvar))