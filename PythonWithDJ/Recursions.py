#recursions means funtions inside a funtion

#below factorial code in iterative method not recursive method
def factorial_iterative(n):
    """
    :param n: Integer
    :return: n* n-1 * n-2 * n-3.....1
    
    """

    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac

#number = int(input("Enter the number"))
#factorial_iterative(number))

#------------------------------------------

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n* factorial_recursive(n-1) #here we see we are calling the function inside a function.

        # 5*factorial_recursive(4)
        # 5*4*factorial_recursive(3)
        # 5*4*3*2*factorial_recursive(2)
        # 5*4*3*2*factorial_recursive(1)
        # 5*4*3*2*1 = 120
#--------------------------------------------------------------------------

# Q. Calculate fibonacci series using recursion method, ex- 0 1 1 2 3 5 8 13 so 5th num is 3 
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) #here we see functions called inside function multiple times 



#calling all the 3 functions here 
number = int(input("Enter the number = "))
print("Factorial Using Iterative Method", factorial_recursive(number))
print("Factorial Using Iterative Method", factorial_iterative(number))
print("Fibonacci Series = ",fibonacci(number))
