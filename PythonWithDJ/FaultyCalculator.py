#make a calculator which shows wrong answeer for 45*3=555, 56+9 = 77, 56/6 =4, rest all should be coreect. 


num1= int(input("Enter the First Number="))
opr= input("Enter the Operator + - * / ")
num2= int(input("Enter the First Number="))


if num1==45 and num2==3 and opr == "*":
    print("555")
elif num1==56 and num2==9 and opr == "+":
    print("77")
elif num1==56 and num2==6 and opr == "/":
    print("4")

elif opr == "+":
    print(int(num1+num2))

elif opr == "-":
    print(int(num1-num2))

elif opr == "*":
    print(int(num1*num2))

elif opr == "/":
    print(float(num1/num2))
