# F(fast) strings are a way to format strings in a more Readable way 
#-------------------------------------------------------------------------
#below are earlier ways of formtting
import math 

me="Harry"
a1 = 3

# a = "this is %s %s " %(me, a1)
# print(a)

# b = "This is {1} {0}"
# c= b.format(me, a1) # me will goto 0 and a1 will goto 1 
# print(c)

#-----------------------------------------------------------------------------------
#Belwo are F strings 

a = f"this is {me} {a1} {4*65 } {math.cos(65)}"
print(a)

