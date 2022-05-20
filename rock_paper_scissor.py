from random import randint

print("Welcome!")
print("R is rock, p is paper, s is scissor ! ! !")
print()

user_wins = 0
computer_wins = 0


option = ["r", "p", "s"]

while True:
    user_choice = input("Type 'r' for rock, 'p' for paper, 's' for scissor or q to QUIT: ")

    if user_choice == "q":
        break

    if user_choice in option:
    
        computer_choice = randint(0,2)   
        computer = option[computer_choice]

        print(f"Computer choice was {computer}. ")


        if user_choice == "r" and computer == "scissor":
            print("You Win !")
            user_wins += 1
            
        elif user_choice == "p" and computer == "rock":
            print("You Win !")
            user_wins += 1

        elif user_choice == "s" and computer == "paper":
            print("You Win !")
            user_wins += 1

        elif user_choice == computer:
            print("TIE !")
        
        else:
            print("You Lose !")
            computer_wins += 1

print(f"You won {user_wins} times! ")
print(f"The computer win {computer_wins} times")
print("Goodbye")