print(4/2) #floating decimal
print(2//4) # for integer output
print(2**3) # to the power
print(2**0.5) # to find sqareroute
print(round(2**0.5,4)) # this will give output upto 4 digits after decimal
print(3%2) # to get remainder
print(2**3/2*6-4*(3-4/2)) # python uses parenthesis rule
print(2**3**2) # here calculates is L to R- first 3**2= 9, then 2**9= 512

name ="Diwakar"
age = 24
print("%s is %d years old" %(name, age))

data = ("John", "Doe", 53.44)
format_string = "Hello, %s %s . Your current balance is $%s"
print(format_string % data)