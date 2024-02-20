def factorial(num):
    fact = 1
    while num!=0:
        fact = fact*num
        num = num -1
    return fact

num=int(input("Enter any number"))
print("the factorial of the number is:", factorial(num))
