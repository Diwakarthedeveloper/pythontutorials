#decorators allow us to wrap one function with another function so that we dont need to write two logics together as that will cluter the function
#lecture 25
#calculating time for a function to perform
import time

from numpy import array

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__+"took = " + str((end-start)*1000) + "mil sec")
        return result

    return wrapper
@time_it
def calc_square(numbers):
#    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number)
#    end = time.time()
#    print("calc_square took" + str((end-start)*1000)+"mil sec")
    return result

@time_it
def calc_cube(numbers):
#    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
#    end = time.time()
#    print("calc_cube took" + str((end-start)*1000)+ "mil sec")
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube =  calc_cube(array)
