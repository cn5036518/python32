lst1=[]
lst2=[]
lst3=[]

with open("usr.txt",mode="r+",encoding="utf-8") as fp:
    lst=fp.readlines()
    for i in lst:
        print(i)
        name,pwd=i.strip().split(":")
        lst1.append(name)
        lst2.append(pwd)
    sign=True
    while sign:
        name=input("请输入用户名:")
        if name in lst1:
            with open("black.txt",mode="r+",encoding="utf-8") as fp:
                lst=fp.readlines()
                for j in lst:
                    lst3.append(j)
            if name in lst3:
                print("您已被纳入黑名单")
                break
            else:
                a=lst1.index(name)
                pwd=lst2[a]
                while True:
                    pwd1=input("请输入密码:")
                    if pwd1==pwd:
                        print("登录成功")
                        sign=False
                        break
                    else:
                        times=1
                        while times<=3:
                            print("密码错误,您还剩{}次机会".format(3-times))
                            if times==3:
                                with open("black.txt",mode="a",encoding="utf-8") as fp:
                                    fp.write("name"+"\n")
                                    break
                            times +=1
        else:
            print("用户不存在")
        




































