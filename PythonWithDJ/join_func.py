list1 = ["john","cena","randy","ortan","Jinder","Mahal","khali","sheamus"]

#-- below is old way to join list values. 
# for item in list1:
#     print(item, "and", end=" ")
# print("other wwe super stars")

#-------below is new way to joun the list values----

a = " and ".join(list1) # join command is used to join using and statement
print(a, "other wwe superstarts")