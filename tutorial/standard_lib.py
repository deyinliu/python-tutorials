# -*-coding:utf-8-*-
from echo import echo
import os
import shutil
import glob
import sys

echo(os.getcwd())

# a = os.chdir("/Users/deyinliu/Desktop")
# os.system("rm i.py")

# shutil.copyfile("./standard_lib.py","./standard_lib1.py")
# echo(help(glob.glob))
echo(glob.glob("*.py"))
echo(sys.argv)
# print("  \bdd\nfsaf")
from timeit import Timer
echo(Timer("a = 1;b = 2").timeit())
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()
print(r"dadhja\na")