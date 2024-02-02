import time
import multiprocessing

square_result=[]

def calc_square(numbers):
    for n in numbers:
        print('square:', n*n)
        square_result.append(n*n)
    print('within a process: result' + str(square_result))
#above print is declared within a process as outside process it will not store the answer and data is not share outside the process
# to access data outside the process it should be shared memory 
def calc_cube(numbers):
    for n in numbers:
        print('cube:', n*n*n)

if __name__ == "__main__":
    arr = [2, 3, 8, 9]

    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

#p1.join asks to wait until each funtion once is finshed then only execute the below print statement to calculate the total time 
    p1.join()
    p2.join()
print('here it will not work as it outside the processt' + str(square_result))
print("done")




