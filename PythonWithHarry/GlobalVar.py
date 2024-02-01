# #how global and local  variable works

# l = 10 #global variable
# def function1(n):
#    # l=5 #local variable
#     m=8 #LOcal

#     global l  # to bring global variable in local use this will give it permission to use global variable

#     l = l +45
#     print(l , m)
#     print(n,"I have printed")

#---------------------------------------------------------------------------------------
x=89
def diwakar():
    x=20
    def rohan():
        global x # when global is used it seaches out the program at the top of files mostly here only 20 is avlable so it will be 20
        x = 88
    print("Before calling rohan()",x) #this will be 20
    rohan()
    print("after calling rohan()",x)# this will also be 20 as it the only global variable here
diwakar()
print(x)