import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n)

def calc_cube(numbers):
    print("calculate cube of the numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n*n*n)

arr = [2, 3, 8, 9]
t = time.time()

#without multithreading the program with complete one funtin then only move to next and will take time more
t1=threading.Thread(target=calc_square , args=(arr,))
t2=threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

#t1.join asks to wait until each funtion once is finshed then only execute the below print statement to calculate the total time 
t1.join()
t2.join()

print("done in :", time.time()-t)
print("Hah.. I am done with all my work now!")


