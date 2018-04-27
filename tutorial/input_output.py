#-*-coding:utf-8-*-

import math
from echo import echo

import json

echo("asahj{0:.3f}".format(math.pi))

table = {"orange":3234,"pear":123,"apple":77879}

for key, value in table.items():
    # pass
    echo("{0:10}=>{1:10d}".format(key, value))

echo("pear:{0[pear]};orange:{0[orange]:d};apple:{0[apple]:d}".format(table))

echo("pear:{pear};orange:{orange};apple:{apple}".format(**table))

with open("json.json","r+") as f:
    x = json.dumps(table)
    # f.write("ffff")
    echo(type(x))
    echo(table)
    # echo(type(f.readline()))
    x = f.readline()
    echo(x)

