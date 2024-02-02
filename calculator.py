first= input("enter the first number=")
operator = input("enter operator (+ or - or / or *)=")
second = input("enter the second number")

first = int(first)
second= int (second)

if operator == "+":
    print(first+second)

elif operator == "-":
    print(first-second)

elif operator == "*":
    print(first*second)


elif operator == "/": # use // for int division instead of float divison
    print(first/second)

elif operator == "%":
    print(first % second)

else:
    print("invalid operataor")
