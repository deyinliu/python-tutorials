#-*- coding:utf-8 -*-
from echo import echo
import sys

try:
    with open("./hahah.txt","a") as f:
        # f.readline()
        f.write(2)
        # 1/0
except :
    echo("exception error:{}".format(sys.exc_info()))
    raise