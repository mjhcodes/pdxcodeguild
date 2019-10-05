import random

def choice_selector():
  """accepts user choice and randomly selects computer choice"""
  user_choice = input("Select rock, paper or scissors: ").lower()
  computer_choice = random.choice(['rock', 'paper', 'scissors'])
  return user_choice, computer_choice

def print_result(user_choice, computer_choice):
  """compares user choice to computer choice and prints result"""
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

def main():
  """accepts choices, compares and prints result, then allows user to play again"""
  while True:
    user_choice, computer_choice = choice_selector()
    print_result(user_choice, computer_choice)
    repeat = input("Enter 'yes' to play again: ").lower()
    if repeat != "yes":
      break

main()