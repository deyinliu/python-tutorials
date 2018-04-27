#-*-coding:utf-8-*-

def echo(*x,end=" "):
    for i in x:
        print(i,end=end)
    print(end="\n"+"-"*60+"\n")
    # print("-"*60)