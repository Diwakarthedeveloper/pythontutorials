f = open("Diwakar.txt", "r")
content = f.read()
#content = f.read(4) it will read only first 4 letters
#content = f.read(50) it will run after the first 4 letters
print(content)


# print(f.readline()) # to print first line , line by lines
# print(f.readlines()) # to print all  lines in one line

# for line in f:
#     print(line) # this will print character by character

# for line in content:
#     print(line, end ="") # this will print line by line


f.close() #always close the file as resources are running if not closed 

