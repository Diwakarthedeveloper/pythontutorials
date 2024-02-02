# A number is hidden and the player have to guess the number, if he enters a number greater than hidden number
#  print it should be lesser and if less than hidden number then print it should be higher
# Also if he takes more than 9 gusses the game is over
# print the number of gusses he took to guess the hidden number 

hidden_number = 18
no_of_gusses = 1 
print("you will get 6 chances to play this game") 

while (no_of_gusses<7):
    inp =int(input("Enter the hidden Number="))


    if inp>18:
        print("Sorry, You have entered a number greater than Hidden number, enter a smaller number")

    elif inp<18:
        print("Sorry, You have entered a number smaller than Hidden number, enter a greater number")

    else:
        print("you won \n")
        break

    print(6 - no_of_gusses, "n0. of gussess left")
    no_of_gusses = no_of_gusses+1

if(no_of_gusses==7):
    print("game over")
