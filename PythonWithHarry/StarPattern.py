# WAP tp print straight forward star patter is input is true and doward star when input is false.

print("Patter Printing")
num = int(input("Enter num how many rows you want: "))
print("Enter 1 or 0")
bool_val= input("1 for True value or for False")
if bool_val=="1":
    for i in range (0,num+1):
        print("*"*i)

if bool_val=="0":
    for i in range(num,0,-1):
        print("*"* i)