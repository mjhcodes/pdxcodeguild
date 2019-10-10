# Lab 12 - Guess The Number

import random

def get_random_number():
  """generates a random number between 1 and 10"""
  comp_num = random.randint(1, 10)
  return comp_num

def compare_numbers(comp_num, user_num, count):
  """compares the two numbers and performs action based on result; if numbers do not match, increases count and returns incremented number"""
  if comp_num == user_num:
    print(f"\nCorrect! It only took you {count} guesses.\n")
    quit()
  elif count < 10:
    print("\nTry again!")
    count += 1
  else:
    print("\nNo more guesses. You lose!\n")
    count += 1
  return count

def main():
  """starts count at 1st guess, generates random number, compares to user number and repeats up to ten times, if number not guessed"""
  count = 1
  while count <= 10:
    comp_num = get_random_number()
    user_num = int(input("\nGuess the number (1-10): "))
    count = compare_numbers(comp_num, user_num, count)

main()