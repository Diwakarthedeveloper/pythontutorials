list_items =[] #normal list
for i in range(1,11): # in list all items in the list are of the same category while in tuple all contents may be diffrent
    list_items.append(i)
print(list_items)

list_items_comprehensive = [i for i in range(1,11)] #list comprehensive

print(list_items_comprehensive)

list_comp_odd = [i for i in range(1,11,2)]
print(list_comp_odd)