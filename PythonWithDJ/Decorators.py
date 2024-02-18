def function1():
    print("Follow the rules")

func2 = function1
del function1
func2() #func2 is called here, 

#------------------------------------------

def funcret(num):
    if num==0:
        return print
    if num==1:
        return int
a = funcret(1)
print(a)


