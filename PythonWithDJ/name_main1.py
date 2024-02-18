# this will be self made module which will be called in another file name_main2.py

from ast import main
from tkinter.tix import MAIN


def printdj(string):
    return f"this string will be used in another {string}"


def add(num1, num2):
    return num1+ num2 +5

# the below code will only run when this filename_main1.py is executed and will not run when this file is called in another program , only above filr will be executed
print("and the name is ", __name__) # means name of __name__ is __main__ and the below coe will run from this program only

if __name__ == '__main__':
    print(printdj("Harry1"))
    o =add(4,6)
    print(o)
 




