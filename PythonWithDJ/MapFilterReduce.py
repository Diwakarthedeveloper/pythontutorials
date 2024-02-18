# Q ) convert string list to int list and add using Map ilter 
from warnings import filters


numbers = [ "3", "34", "64"]

# below is the old technique using for loo(not a prefered way as it runs for loop every time)
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers[2] = numbers[2] + 1 # 2 is or the second index in the list 
# print(numbers[2])

# - ---------------------------------------------------------------------------------#
# below is the new  technique using for map function
numbers = list(map(int,numbers)) # int(funtion to be applied)- should be at fist location, and (numbers - where the it will be applied)- should be in second position
# new list with int will be stored in numbers 

numbers[2] = numbers[2] + 1 # 2 is or the second index in the list 
print(numbers[2])

# - ---------------------------------------------------------------------------------#
# in below program we use map and funtion to sqaure a number
def sq(b):
    return b*b

num = [2,3,4,5,6,7,8,9]
square_num = list(map(sq, num))
print(square_num)

# - ---------------------------------------------------------------------------------#
#using lambda instead of function to square the numbers
num = [2,3,4,5,56,75,24,9]
square_num = list(map(lambda x: x*x, num))
print(square_num)

# - --------------------MAP--BELOW-------------------------------------------------#
#lambda function to square cube for first 5 elements  = 0 1 2 3 4 
def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]

for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)
 # - ---------------------------------------------------------------------------------#
#filter function - it creates a list in which the given function return true, Filter funtion is used to filter with the condition
list1 = [1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5, list1)) # filter(function, objects to be filtered )
print(gr_than_5) # will print values greater than 5 in above list 


# - ------------REDUCE ---------------------------------------------------------------------#
from functools import reduce

list1 = [1,2,3,4] # need to add these
num= reduce(lambda x,y:x+y, list1) # reduce function is used here instaead of using loop to add.
print(num)