
#same global variable can be used as global and loacal variable
#x= "I am global variable"
#def somefunction():
#    print("x inside functions:",x)
#somefunction()
#print("x outside functions:",x)


#for both local and global variable
#def someFunctions():
#    global x # global command allows you to use x inside and outside the function at same time.
#    x= 500
#    print("x inside functions:",x)
#    someFunctions()
#print("x outside functions:", x) 

#local variable scope
#def somesimpleFunction():
#    x=500
#    print("x inside function", x)
#somesimpleFunction()
#print("x outside Functions", x) # this will show error as x is a local variable and works inside function only
    

def outerFunction():
    x = "I am local value"
    def innerFunction():
        nonlocal x
        x="I am non -local value"
        print("inner function value of X:", x)
    innerFunction()
    print("outer function value of x:", x)
outerFunction()