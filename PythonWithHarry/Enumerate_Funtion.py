# Enumerate makes our work easier 

list1=  ["Bhindi","Alloo","chopsticks","chowmein","piyaz"]

# traditional way below
# i = 1
# for item in list1:
#     #if i%2 is not 0:
#     if i%2 != 0:
#         print(f"Jarvis please buy {item}")
#     i = i +1

    #-------------------------------------------------
    #using enumeration function below
for index, item in enumerate(list1): #index is the position and item is the names in the list
    if index%2==0:  # we need even vegetables
            print(f"Jarvis please buy {item}")
 