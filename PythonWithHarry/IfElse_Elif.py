var1 = 6
var2 = 56
var3 = int(input()) #input will be taken as string , but to compare it with a number we need to convert it with a number

if var3>var2:
    print("Greater")
elif var3==var2:  #if we use IF insted of ELIF then the program will go through all IF even if condition is 
#     satisfied in first stement but in elif as soon as the condition in satisfied the program will not execute 
#     other conditions.
    print("Equal")
else:
    print("Lesser")


list1 = [5,7, 3]
print(7 in list1)  # this will show true or false
print(3 not in list1)
if 5 in list1:
    print("yes its in list")