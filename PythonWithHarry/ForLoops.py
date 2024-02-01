list1 = ["Diwakar","Prashant","Somu","Manish"]
list2 = [["Diwakar",1],["Prashant",2],["Somu",4],["Manish",6]] # list of ists 


for item in list1:
    print(item)

for item in list2:
    print(item)

for item,ranks in list2: #python will itself take first and second value from list of lists. 
    print(item, "and rank is ", ranks)


dict1 = dict(list2) # this will convert list into dictionary
print(dict1)

for items,ranks in dict1.items(): #using for loop in dictionary to get key abd value
    print(items,"and rank is ",ranks)

for item in dict1: # to get only the key 
    print(item)

#one quiz n=below - make a program to print avlues greater tahan 6 

items =[int,float,"Diwakar",5,3,3,22,31,45,7,8,5,6]
for item in items:
    if str(item).isnumeric() and item>= 6: #convert all numerc to string to bring uniformmity
        print(item)   # it will only print numbers because 