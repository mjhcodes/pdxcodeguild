import random

user_choice = input("Select rock, paper or scissors: ").lower()
computer_choice = random.choice(['rock', 'paper', 'scissors'])

if user_choice == computer_choice:
  print(f"{user_choice} vs. {computer_choice} - You Tied!")
elif user_choice == "rock" and computer_choice == "scissors":
  print(f"{user_choice} vs. {computer_choice} - You Win!")
elif user_choice == "scissors" and computer_choice == "paper":
  print(f"{user_choice} vs. {computer_choice} - You Win!")
elif user_choice == "paper" and computer_choice == "rock":
  print(f"{user_choice} vs. {computer_choice} - You Win!")
else:
  print(f"{user_choice} vs. {computer_choice} - You Lose!")