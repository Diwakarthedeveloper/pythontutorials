from cgi import print_arguments


name = "Diwakar Jha"
print('w' in name)
print("line A \n line B \n line c") # for next line
print("My\tDiwakar")  # this \t gives one tab space
print("this is blackslash\\") # to print one blackslash use two blash slash
print("Diww\bakar") #\b deleted one alphabet

# Q) get output ->Line A \n Line B and -> \" \' 
print("Line A \\n Line B")
print("\\\" \\\'")

# print -> \\  then-> /\/\/\/\/\  then-> he is       awesome -> \" \n \t \'
print("\\\\")
print("/\\/\\/\\/\\/\\ ")
print("he is \tawesome")
print("\\\" \\n \\t \\'")

# use escape sequence as normal text without using double \\
print(r"line A \n line B ") # r make escape sequence as normal line

#print emoji from https://unicode.org/emoji/charts/full-emoji-list.html , put 000 in place of +
print("\U0001F606") 