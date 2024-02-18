# lamba funtions are one liner funtions and is same as funtions but we have to write less code. 

def minus(x,y):
    return x-y
#print(minux(9,4))

# Above is the normal function and below is the lambda function with same purpose. 

minux = lambda x,y: x-y

print(minux(9,4))

#----------------------------------------------------------------

def a_first(a):# here funcion is created
    return a[1]

a = [[1,14], [5,6], [8,23]] #
a.sort(key=a_first) #function is called here and sorted. 
print(a)

# Above is the normal function and below is the lambda function with same purpose. 
a = [[1,14], [5,6], [8,23]]
a.sort(key=lambda x:x[1])
print(a)


