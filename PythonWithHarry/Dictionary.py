#Dictionary is key value pair, it is denoted by curly braces
d1 = {}  # this is blank dictionary
d2 = {"Diwakar":"Paratha","Guudu":"Soyachunk","Ram":"Roti"}

print(d2)
print(d2["Ram"])
# below is a dictionary inside a dictionary
d3 = {"Diwakar":"Paratha","Guudu":"Soyachunk","Ram":{"Breakfast":"Maggie","Lunch":"Roti","Dinner":"Sabzi"}}
#value of a Key in a dictionary can be a tuple dictionary list, but key will be immutable
print(d3["Ram"])
print(d3["Ram"]["Lunch"])
#adding new key:value to dictionary

d2["Ankit"]="Chips"
print(d2)
#del d2["Ankit"] # this will delete the key Ankit


d4=d2
del d3["Guudu"] #this will delete Guudu from the d2 also , so use copy command
print(d2)

d4=d2.copy()
del d3["Diwakar"] #this will not delete Guudu from the d2 , so use copy command
print(d2)


d2.update({"Sita":"Tofee"})
print(d2)

print(d2.keys())

print(d2.items())



