# its MapReduce where MAP - distribution of work load(code+input) equally to all the cores in the machine
# # REDUCE = collection of all the output from all cores and display together. So large work gets done faster by breaking parallely

from multiprocessing import Pool
import time

def f (n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == "__main__":

    t1 = time.time()               #t1 stores time at this point of ec=xecution
    p = Pool()
    result = p.map(f,range(10000))
    p.close()
    p.join() # so the output comes only when all above execution is complete in p.map

    print("Pool took",time.time()-t1)

# performance is measured by using time diffrence beywwen above code(pool) and below code(serial)

    t2= time.time()
    result= []
    for x in range(10000):
        result.append(f(x))

    print("Serial processing took:", time.time()-t2)

# from the output of time we will see pool takes half of time due to parallel multicore processing
