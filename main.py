import random

user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissors"]

while True:
     user_input = input("Type Rock-Paper-Scissors or Q to quit: ").lower()
     if user_input == "q":
          break

     if user_input not in ["rock", "paper", "scissors"]:
          print("Not a valid option! Try again!")
          continue

     random_number = random.randint(0, 2)
     computer_choice = options[random_number]
     print("Computer picked", computer_choice + ".")

     if user_input == "rock" and computer_choice == "scissors":
          print("You won!")
          user_wins += 1
     
     elif user_input == "scissors" and computer_choice == "paper":
          print("You won!")
          user_wins += 1
     
     elif user_input == "paper" and computer_choice == "rock":
          print("You won!")
          user_wins += 1

     elif str(user_input) == str(computer_choice):
          print("You both chose", user_input + "!")

     else:
          print("You lose!")
          comp_wins += 1

print("You won", str(user_wins) + " times!")
print("The computer won", str(comp_wins) + " times!")
print("Goodbye!")