#use while loop and break continue to write a program to print numbers from 5 to 44

i = 0

while(True):  # in break-continue its not necessary to put condition in while statement and put continue below
    if i+1<5:
        i=i+1
        continue
    print(i+1, end= " ") # print print from 1 to infinity 
    if(i == 44): # to stop the loop at 44
        break #stop the loop
    i = i +1