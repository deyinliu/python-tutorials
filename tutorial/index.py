# -*- coding:utf8 -*-

from echo import echo

list = [1,2,3,"ff"]

echo(list)

a,b,c = 1,2,3
echo(c)

# try:
#     x = int(input("请输入int类型数据\n"))
#     echo(x)
# except:
#     echo("输入错误")

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# key=lambda pair: pair[1]
pairs.sort(key=lambda pair: pair[1])

def fun():
    """Do you know the function

The function is a demo.
    """
echo(fun.__doc__)

def fun_annotation(age:int,name:str)->str:
    return "my name is "+name+"and "+str(age)+" years old"

echo(fun_annotation(11,"haha"))

x1 = [(y0**2,y0) for x0 in range(9) for y0 in range(4,13) if y0>x0]
echo(x1)
# echo(x0)

martix = [[i**j for j in range(3)] for i in range(4)]
echo(martix)
t_martix = [[r[i] for r in martix] for i in range(3)]
echo(t_martix)

c = 1,2,3,4
d = 2,3,4,5
s = {1,2,3,4,3,2,3,4,3,2}
echo(s)

dic = dict(a=1,b=2,c=3)
for k ,v in dic.items():
    print(k,":",v)
    print("-"*60)
echo(dic)
echo(enumerate(dic))
for k,v in enumerate(s):
    print(k,v)
    print("-"*60)

questions = ['name', 'quest', 'favorite color',"age"]
answers = ['lancelot', 'the holy grail', 'blue',12]
for q, a in zip(questions, answers):
   echo('What is your {0}?  It is {1}.'.format(q, a))

fruit = ["apple","orange","pear","apple","orange"]
echo([f for f in sorted(set(fruit))])

s = "laozhongyi\n"
echo(repr(s))
echo(s)
# print("dasda","asdsad",sep="",end="\n")
echo(repr(2),repr(3).ljust(8),repr(3).rjust(4))
echo(fruit)
print("my name is {1},my brother is {0}".format("haha","aha"),end="\n"+"-"*60+"\n")
print("my name is {haha},my brother is {aha}".format(aha = "haha",haha = "aha"),end="\n"+"-"*60+"\n")
print("my name is {!r},my brother is".format(s),end="\n"+"-"*60+"\n")