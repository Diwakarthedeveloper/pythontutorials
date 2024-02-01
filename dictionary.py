d = {"john":7546874512, "tom":9236756343, "tim":9087678954}
print(d)   

d["sam"]= 9876543211 # to append in the dictionary 
print(d)

del d["tom"]  #to delete a dictionary
print(d)

for i in d:
	print("KEY",i,"VALUE",d[i]) # to print each KEY VAlUE in the dictionary
print("-------------------------------------------------------")

for a,b in d.items():
	print("KEY:",a,"VALUE",b) # to print each KEY VAlUE in the dictionary