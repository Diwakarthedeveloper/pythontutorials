myline = "diwakar is a good boy"
print(len(myline))
print(myline[0:18])
print(myline[0:18:2])
print(myline[0::2])
print(myline[0:])
print(myline[:10])
print(myline[:])
print(myline[::])
print(myline[-4:])
print(myline[-4:-2])
print(myline[::-1]) # reverse the string
print(myline[::-2])

print(myline.isalnum()) #this should show false as the statement is not alpha numeric
print(myline.endswith("boy")) #this should show true
print(myline.count("o"))
print(myline.capitalize()) #this will captalize the first letter
print(myline.upper())
print(myline.lower())
print(myline.find("is")) #this will find the starting index of value is
print(myline.replace("is","are"))


