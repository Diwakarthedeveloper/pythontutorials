# we will use difflrent modules and their functins  to solve a problem

import random #random is a module


#below module will print any rndom number among  1 and 0

random_number = random.randint(0, 1) #randint is a function of module random 
print(random_number)


#below module will print any rndom number between 1-100
rand = random.random() *100 #first random is a module and second random is a function
print(rand)

# below will print any random tv channel from the list 
tvchannellist = ["Star PLus ","DD1","Aaj Tak","CodeWith HArry","CartoonNetworks"]
choice = random.choice(tvchannellist)  # choice is a function of module random 
print(choice)

# assignment - use 2 modules and use their 2 funtions of each modules .
# to install a module - pip install module_name