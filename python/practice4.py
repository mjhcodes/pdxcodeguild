# Practice 4 - Dictionaries

# Problem #1

def combine(x, y):
  """accepts two lists and combines them into a dictionary"""
  return dict(zip(x, y))

fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

# print(combine(fruits, prices))


# ----------------------------------------------------------------

# Problem #2

def average(d):
  """accepts a dictionary, iterates through it and calculates the average price of an item"""
  value_list = [num for num in d.values()]
  sum_of_values = sum(value_list)
  return sum_of_values / len(value_list)

combined = combine(fruits, prices)

# print(average(combined))


# ----------------------------------------------------------------

