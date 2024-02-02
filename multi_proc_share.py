#this programs shows how to share data in multiprocessing 

import multiprocessing
import numbers
from unittest import result

from numpy import number

def calc_square(numbers, result,v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        result[idx] = n*n
#above is the child process where value from parent process is transfered

#below is the parents process where data/value is generated
if __name__== "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('i',3)
    v=multiprocessing.Value('d', 0.0)
    p=multiprocessing.Process(target=calc_square,args=(numbers, result, v))


    p.start()
    p.join()
#again from the child the value is sent to the parent process below
    print(v.value)