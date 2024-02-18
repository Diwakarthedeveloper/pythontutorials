# WAP to if user gives num>100 say congrats if <100 try again 

while (True):
    inp =int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats, You have entered a number greater than 100")
        break
    else:
        print("Try again \n")
        continue