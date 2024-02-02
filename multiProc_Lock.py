#Lock is used so that only one process use the shared memory at a time , when the one process completes its work then only second process touches the shared memory else it may cause issues in some cases

import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d=multiprocessing.Process(target=deposit, args=(balance,lock))
    w=multiprocessing.Process(target=withdraw   , args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)




