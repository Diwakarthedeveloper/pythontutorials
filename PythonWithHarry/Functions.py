#Function is a code which can be used in other code instead of writting same code everytime with diffrent value


def function2(a,b):  # function2 is name of the programa , a and b are user input
    """This is function to calculate average of two nu,ber """  #this is doc string which tells about function
    
    average = (a+b)/2
    print (average)
    return average #if return is not used then when the function is called somewhere else it will not return anything  

#program starts below then it goes to def function2 then at last return value to v and stores in v
v = function2(5,7) #here the above function is called with new input values and stored in new variable suing same logic
print(v)

function2(4,5) #calling above funtion with diffrent values 
function2(12,5)

print(function2.__doc__) # doc of this function is defined above so if anyone wants to know the use of fuction he can use print(functionname.__doc__)
