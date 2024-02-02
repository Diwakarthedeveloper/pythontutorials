#factorial calculation using recursion(a functon that calls itself is a recursive function)

def calculateFactorial(x):
    if x ==1:
        return 1
    else:
        return(x * calculateFactorial(x-1))
num = 4
factorial_number = calculateFactorial(num)
print("Factorial of ", num,"is 1*2*3*4 =", factorial_number)