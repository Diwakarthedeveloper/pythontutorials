# Write a function that when executed takes as input client name 
# one more function to retrive exercise or food for any client. 

# this below program is long - we could have written two functions for log and retrive and any name would have worked instead of three names

import datetime
def gettime():
    return  datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for exercise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("harry-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        
        elif(c==2):
            value = input("type here\n")
            with open("harry-food.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")

    elif(k==2):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            value = input ("type here \n")
            with open("rohan-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")

        if (c == 2):
            value = input ("type here \n")
            with open("rohan-food.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")

    elif(k==3):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            value = input ("type here \n")
            with open("hammad-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")

        if (c == 2):
            value = input ("type here \n")
            with open("hammad-food.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")

    else:
        print("plz ebter valid input (1- Harry), (2 - Rohan),(3- Hamad)")

def retrieve(k):
    if k ==1:
        c=int(input("enter 1 for exercise and 2 for food"))
        if (c==1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i, end = "")

        
        elif (c==2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end = "")

    elif k ==2:
        c=int(input("enter 1 for exercise and 2 for food"))
        if (c==1):
            # with open("rohan-ex.txt" ,"rt") as op:   #rt is not reqired its by default
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end = "")

        
        elif (c==2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end = "")                

    elif k ==3:
        c=int(input("enter 1 for exercise and 2 for food"))
        if (c==1):
            # with open("rohan-ex.txt" ,"rt") as op:   #rt is not reqired its by default
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end = "")

        
        elif (c==2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end = "")


    else:
        print("plz input valid name harry rohan hammad")

print("health management system: ")
a=int(input("press 1 for log the value and 2 for retrive the value"))        

if a == 1:
    b = int(input("press 1 for harry , 2 for rohan , 3 for hammad"))
    take(b)
else:
    b = int(input("press 1 for harry , 2 for rohan , 3 for hammad"))
    retrieve(b)
