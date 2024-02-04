# n = int(input("Enter the number whose table you need = "))
# i = 1
# while i<=10:
#      print(f"{n} x {i} = ", n*i)
#      i=i+1

while True:
    n = int(input("Enter the number whose table you need = "))
    r = int(input("Enter the range or end of the table you need like till 10 or 15 or 50 = "))
    for i in range(1, r+1):
        print(f"{n} x {i} = ", n*i)

    repeat = input("Do you want next table then press y for YES or n for NO ->  ")
    if repeat == "n":
        break

print("Thanks for using our multiplication application")




