import random



print ("Welcome to Rock Paper Scissor")
user1score = 0
roboscore = 0
ties = 0
username = input("Hey, whats your Name ?")
print(""""
    Winning Rules
    1. Paper vs Rock -> Paper
    2. Rock vs Scissor -> Rock
    3. Paper vs Scissor -> Scissor
    """)

while True:
    print(""""Choices are :
        1. Rock
        2. Paper
        3. Scissor
        """)

    choice = int(input ("Enter your Choice from 1 or 2 or 3 = "))
    print()

    # while choice > 3 or choice < 1:
    #     choice = int(input("Enter valid input from 1, 2 , 3"))

    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    elif choice == 3:
        user_choice = "Scissor"
    else:
        print("Enter valid input from 1, 2 , 3")

    print(f'{username} has taken {user_choice} ')
    print("Now computers turn")

    computer = random.randint(1,3)

    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    elif computer == 3:
        comp_choice = "Scissor"
    else:
        print("Enter valid input from 1, 2 , 3")

    print(f'Computer choice is {comp_choice}')

    if ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        print("Paper wins")
        result = "Paper"

    elif ((user_choice == "Scissor" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissor")):
        print("Rock wins")
        result = "Rock"

    elif (user_choice == comp_choice):
        print("Its a tie")
        result = "Tie"

    else:
        print("Scissor wins")
        result = "Scissors"

    if result == comp_choice:
        print("Computer wins")
        roboscore +=1

    elif result == user_choice:
        print(f"{username} wins")
        user1score += 1

    else:
      #  result == "Tie":
        ties +=1

    print ("MATCH SCORES ARE ")
    print(f'{username} Score is {user1score} ')
    print(f'Computer Score is {roboscore} ')
    print(f'Number of Tie happened are {ties} ')

    repeat = input("Do you want to play again, Then press Y else press no?")
    if repeat == "no" or repeat == "NO":
        break

print ("**Game over**")
print(f"Thanks for playing {username} ")



