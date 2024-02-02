#As multiprocess have there own shared space data is not shared directly to other processes
#in this program we will see data share in multiprocessing using Q
# Q(data structure FIFO) is a shared memory used to store results/data

#note : pythod also has a module Q- which is used to share data between threads, its diffrent from multi processing Q as it has in process memory not shared memory

import multiprocessing
import numbers

def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)
        
#here we see Q is used to share data from the main process below to child process above

if __name__ == "__main__":
    numbers = [2, 3, 5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())




