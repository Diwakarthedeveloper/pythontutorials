indian=["samosa","dosa","litti"]
chinese= ["noodles","fried rice","egg role"]
italian=["pizza","pasta","risotto"]
dish= input("Enter Dish Name:")
if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
        print("i dont know this",dish)
