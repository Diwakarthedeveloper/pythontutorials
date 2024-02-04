
while True:
    a = input("Enter the character whose ASCII value you need = ")
    print("The ASCII value of the charcter {a} is ", ord(a))

    replay = input("Do you want to find ASCII value of any other character , press y for YES and n for NO -> ")
    if replay == "n":
        break


