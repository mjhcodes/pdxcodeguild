# Practice 3 - Lists

import random

# Problem #1

def random_element(fruits):
  """pick a random element of a list and return it."""
  random_index = random.randint(0, len(fruits))
  return fruits[random_index - 1]

# fruits = ['apples', 'bananas', 'pears']
# print(random_element(fruits))


# ----------------------------------------------------------------

# Problem #2

def list_compiler():
  """asks users for a list of numbers, which they enter, until they say 'done'. Then prints out the list."""
  user_list = []
  while True:
    try:
      user_input = int(input("Enter a number (or 'done'): "))
      user_list.append(user_input)
    except:
      return user_list

# print(list_compiler())


# ----------------------------------------------------------------

# Problem #3

def eveneven(user_list):
  """accepts a list of numbers, and returns True if there is an even number of even numbers."""
  removed_list = [n for n in user_list if n % 2 == 0]
  if len(removed_list) % 2 == 0:
    return True
  else:
    return False

# print(eveneven([5, 6, 2]))
# print(eveneven([5, 5, 2]))


# ----------------------------------------------------------------

# Problem #4

