# Practice 1 - Fundamentals

# Problem #1

def is_even(num):
  """accepts number and returns True, if the number is even; else, False"""
  if num % 2 == 0:
    return True
  else:
    return False

# print(is_even(5))
# print(is_even(6))


# ----------------------------------------------------------------

# Problem #2

def opposite(a, b):
  """accepts two numbers and checks if one is positive and the other is negative; if so, returns True; else, returns False"""
  if (a < 0 and b >= 0) or (a >= 0 and b < 0):
    return True
  else:
    return False

# print(opposite(10, -1))
# print(opposite(2, 3))
# print(opposite(-1, -1))


# ----------------------------------------------------------------

# Problem #3

def near_100(num):
  """accepts a number and returns True, if the number is less than 10 from 100; else, returns False"""
  num = abs(100 - num)
  if num < 10:
    return True
  else:
    return False

# print(near_100(50))
# print(near_100(99))
# print(near_100(105))


# ----------------------------------------------------------------

# Problem #4

def maximum_of_three(a, b, c):
  """accepts three numbers and returns the maximum"""
  max_num = max(a, b, c)
  return max_num

# print(maximum_of_three(5, 6, 2))
# print(maximum_of_three(-4, 3, 10))


# ----------------------------------------------------------------

# Problem #5

def print_powers_of_2():
  """prints out the powers of 2 from 2^0 to 2^20"""
  i = 0
  while i <= 20:
    if i == 20:
      print(2 ** i, end="\n")
      break
    print(2 ** i, end=", ")
    i += 1

# print_powers_of_2()