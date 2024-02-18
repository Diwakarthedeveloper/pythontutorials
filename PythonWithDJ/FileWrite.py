f= open("Diwakar.txt","w") # this "w" will create a new file and write else update the old file completely witth new data
#f.write("Diwakar is a very good Boy")
a=f.write("Diwakar is a very good Boy") #this will count the number of characters written
print(a)


f.close

#Handle both read and write

# f=open("Diwakar1.txt", "r+")  #r+ means read and write
# print(f.read())
# f.write("thank you")