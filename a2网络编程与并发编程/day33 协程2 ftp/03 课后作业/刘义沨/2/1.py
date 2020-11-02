import os,hashlib
def check_md5(filename):
    hs=hashlib.md5()
    filesize=os.path.getsize(filename)
    print(filesize)
    with open(filename,mode="rb") as fp:
        while filesize:
            content = fp.read(1024)
            hs.update(content)
            filesize -=len(content)
        return hs.hexdigest()
res1=check_md5("lianxi1.py")
res2=check_md5("lianxi2.py")
print(res1,res2)
