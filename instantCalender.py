import calendar

Y = int(input("Enter the calender year you need = "))
M = int(input("Enter the calender month you need = "))
calendar = calendar.month(Y,M)
print(calendar)