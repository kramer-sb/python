import random #so we can randomize the computer's choices

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Do you want rock, paper, or scissors?\n")

print("Computer choice:", computer_choice)

if computer_choice ==user_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "scissors":
    print ("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print ("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print ("You win!")
else: 
    print("You lose, computer wins :) ")

#this was my first randomized file, created with the Pythom 3 Fundamentals course in Pluralsight w Sarah Holderness
