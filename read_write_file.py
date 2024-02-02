# f = open("D:\\python learning\\funny.txt","a")
# f.write("\n I love Python") #\n to add new sentance in a new line , print(f.read())- to read all line
# f.close()
# r = read, w = write , overwrite, a = append
# r+ = open file for both reading and writting, 
# w+= open file for both reading and writting if file does not exist it will create a new one and if exist it will over write it 
#---------------------------------------------------------------------------------

# f= open("D:\\python learning\\funny.txt","r")
# print(f.read())
# f.close()
# ----------------------------------------------------------------------------------
# f= open("D:\\python learning\\funny.txt","r")
# for line in f:
#     print(line)

# f.close()
# -------------------------------------------------------------------------------------
#to calculate length of a sentence
# f= open("D:\\python learning\\funny.txt","r")
# f_out=open("D:\\python learning\\funny_wc.txt","w")
# for line in f:
#     tokens=line.split(' ')
#     f_out.write("wordcount:"+str(len(tokens))+line)
# f.close()
# f_out.close()
# -------------------------------------------------------------------------------------
with open("D:\\python learning\\funny.txt","r") as f: #with statement automatically closes the file no need to use close statement
    print(f.read())
print(f.closed)  #this will print true or false as it will check the with statement is closed or not.