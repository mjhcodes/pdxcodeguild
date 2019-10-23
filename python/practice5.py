# Practice 5 - Comprehensions

# Problem #1

def get_powers_of_two():
  """generates a list of the first 10 powers of two"""
  return [(2 ** i) for i in range(10)]

# print(get_powers_of_two())


# ----------------------------------------------------------------

# Problem #2

def get_first_ten_evens():
  """generates a list of the first ten even numbers"""
  return [num for num in range(2, 22, 2)]

# print(get_first_ten_evens())


# ----------------------------------------------------------------

# Problem #3

def swap_keys_and_values():
  """swaps the keys and values of a given dictionary"""
  test_dict = {'a': 1, 'b': 2}
  return {v: k for k, v in test_dict.items()}

# print(swap_keys_and_values())


# ----------------------------------------------------------------

# Problem #4

import string

def get_letters_and_codes():
  """generates a dictionary with each letter of the alphabet and its corresponding ASCII code"""
  return {k: ord(k) for k in string.ascii_lowercase}

# print(get_letters_and_codes())