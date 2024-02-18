# compare time taken by two diffrent loops using time module
from email.utils import localtime
import time
initial = time.time() # storing time at this point 

k =0
while(k<45):
    print("this is python code from internet")
    #time.sleep(2) # this will stop every loop for 2 sec
    k = k +1
print("while loop ran in ", time.time() - initial, "seconds")

initial2 = time.time()
for i in range(45):
    print("this is another python program 2")
print("For loop ran in ", time.time() - initial2, "seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)