punc = '''!@#$%^&*()_-+={}[];:'"<>,./?'''
string = input("Enter your sentance here where puntuations needs to be removed")

empty_str =""

# in below loop i will go through each character in the sentence and if there is no special character and puntuation then it will 
#store that character in th eemply string

for i in string:
    if i not in punc:
        empty_str = empty_str + i

print(empty_str)