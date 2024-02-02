import argparse
from email import parser
from html.entities import name2codepoint
from unittest import result
    # two types of arguments -> 1) Positional (2.) optional

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="first number") #--number helps in optional argument and we can see what we are doing
    parser.add_argument("--number2",help="second number")
    parser.add_argument("--operation",help="operation",\
                                                          choices=["add"," multiply ","substract"])   
    
    args = parser.parse_args()
    
    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1=int(args.number1)
    n2=int(args.number2)
    result = None

    if args.operation == "add":
        result = n1+n2
    elif args.operation== "substract":
        result = n1-n2

    elif args.operation == "multiply":
        result= n1*n2

    else:
        print("unsupported operation")

    print(result) 

    """
    The program will run in command line- goto CMD and redirect to ths py file in cmd and run with arguments.
    example D:\python learning>python ArgPass.py 3 6 add
    outpot -3
            6
            add
            9   
# while in optional arumnets input format  will be 
D:\python learning>python ArgPass.py --number1 3 --number2 6 --operation add

    """