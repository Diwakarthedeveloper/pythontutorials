Planets = 9
"""
# this is a way to dument strings
this function takes 2 arguments which are integer numbers and it will return sum of them as an output
"""

def sum(a,b=0):  #b=0 is default argument - means if  value of B is not provided then B = 0 is used.
    print("a:",a)
    print("b:",b)

    total = a+b
    print("total inside function:", total)
    return total

n=sum(b=5,a=6)
# print(total) total cannot be called here as it is a local variable not a globall variable. 
print("Total outside function:",n)
print(Planets) # planets is a global variable so it will be printed inside and outside the function.