#-*-coding:utf-8-*-
from math import pi
from echo import echo

class test():
    pass
    kind = "immutable object"
    mutable = []
    # def a(self):
    #     echo("method of test")
    def __init__(self,data):
        echo("base class is invoked")
        self.data = data
        # mutable object
        self.trick = []

    def do_object(self):
        self.trick.append(self.data)
        self.mutable.append(self.data)
        return self.trick
    def printx(self):
        echo("base class")

class first():
    kind = "first"
    def a(self):
        echo("first method")

class first1(first):
    pass

class first2(first1):
    pass

class first3(first2):
    pass

class second():
    kind = "second"
    def a(self):
        echo("second method")

class second1(second):
    pass

class second2(second1):
    pass

class second3(second2):
    pass

class subtest(first2,second):
    def __init__(self):
        echo("sub class is invoked")
        echo("base class attribute",self.kind)

    def printxx(self):
        echo("ff")

span = "haha"
def scope_test():
    def local_scope():
        span = "local scope"

    def do_nonlocal():
        nonlocal span
        span = "nonlocal scope"

    def globe_scope():
        global span
        span = "global scope"

    span = "test scpoe"
    local_scope()
    echo("call local_scope:",span)
    do_nonlocal()
    echo("call nonlocal:",span)
    globe_scope()
    echo("call global:",span)
class Reverse():
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[-self.index-1]

if __name__ == '__main__':
   
    # x = subtest()
    # echo(x.kind)
    # x.a()
    # a = Reverse("index")
    # echo(a)
    def reserve(data):
        for index in range(len(data)):
            yield data[index]
    for i in reserve("index"):
        echo(i)