#try except tries to execute the program if error it will print the error and print the other part of program which is necessary to print

print("enter num 1")
num1 = input()
print("enter num 2")
num2 = input()

try: 
    print("The sum of two numbers is ", int(num1)+int(num2))

except Exception as e:  # if we give wrong input then error will be in except and will also be printed and furture program will execute
    print(e)

print("This line is important to for you") # this print statement is necessary in all cases even if above program
                                              # fails so try-except is used in the above program

# so the print atement at line14 will execute in all conditions because of try-except
#such program is used in program when internet is used - if internet  not accessible the also the program should proceed. 
