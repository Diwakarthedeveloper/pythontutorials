# x= input("Enter number 1: ")  # put any number
# y= input("Enter number 2: ")   # put 0 - this will throw a  exception error
# try:
#     z = int(x)/ int(y)    # try catch the block you think gives error
# except Exception as e:
#     print('Exception occured: ',e)
#     z=None
# print("Division is :",z)

# to handle multiple exceptions

x= input("Enter number 1: ")  # put any number
y= input("Enter number 2: ")   # put 0 - this will throw a  exception error
try:
    z = x / int(y)    # try catch the block you think gives error
except ZeroDivisionError as e:
    print('Division by zero exception')
    z=None
except TypeError as e:
    #print('exception type:', type(e).__name__)
    print('Type error exception')
    z = None

print("Division is : ", z)