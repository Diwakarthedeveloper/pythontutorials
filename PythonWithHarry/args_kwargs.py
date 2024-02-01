# below is the poor  way to define and call a function as this is non scalable 
# def new_name_func(a,b,c,d,e):
#     print(a,b,c,d,e)

# new_name_func("Harry","Diwakar","rohan","coddy","larry") # the above function is called here

#---------------------------------------------------------

# def funargs(*args):
#     # print(type(args)) # only to check args type which is always a tuple
#     # print(args[0])
#     for item in args:
#         print(item)

# friendslist =["Harry","Diwakar","rohan","coddy","larry"]
#     # this is scalable new names can be easily added in the list all will go as tuple in args
# funargs(*friendslist) # function is called here passing the above list
#----------------------------------------------------
#below is args with normal argument and kwargs

#def funargs(djnormal,*argsrohan, **kwargshero): # it can be as per we want but not a standard practise

def funargs(normal,*args, **kwargs): # normal argument should first args in second and kwargs in 3rd
    # print(type(args)) # only to check args type which is always a tuple
    # print(args[0])
    print(normal)
    for item in args:
        print(item)
    print("\nNow introducing some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


friendslist =["Harry","Diwakar","rohan","coddy","larry"]
    # this is scalable new names can be easily added in the list all will go as tuple in args
normal = "I am a normal argument here for testing purpose"
kw={"Rohan":"Monitor","Harry":"SrEng","Diwakar":"Eng","Rahul":"Trainer","Shayam":"Singer",}

funargs(normal,*friendslist, **kw) # function is called here passing the above list

