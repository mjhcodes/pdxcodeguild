# Lab 20 - Credit Card Validation

def get_list_of_ints(credit_card_string):
  """accepts a credit card number as a string and returns it as a list of integers"""
  return [int(num) for num in credit_card_string]

def get_check_digit(list_of_ints):
  """accepts a list of integers, removes the last digit and returns both the last digit and the newly shortened list of integers"""
  check_digit = list_of_ints.pop()
  return check_digit, list_of_ints

def get_reversed_list(shortened_list):
  """accepts a list of integers and returns a reversed version"""
  return shortened_list[::-1]

def get_alternately_doubled_list(reversed_list):
  """accepts a list of integers and returns a version with every other number doubled"""
  for i, num in enumerate(reversed_list):
    if i % 2 == 0:
      reversed_list[i] = num * 2
  return reversed_list

def get_subtracted_list(alternately_doubled_list):
  """accepts a list of integers and checks if any of the numbers are greater than nine; if so, subtracts nine, then returns the amended list"""
  for i, num in enumerate(alternately_doubled_list):
    if num > 9:
      alternately_doubled_list[i] = num - 9
  return alternately_doubled_list

def get_sum_of_list(subtracted_list):
  """accepts a list of integers and returns its sum"""
  return sum(subtracted_list)

def get_second_digit(sum_of_list):
  """accepts an integer and returns the second digit"""
  sum_as_string = str(sum_of_list)
  return int(sum_as_string[1])

def compare_digits(check_digit, second_digit):
  """accepts two numbers and returns True message, if they match; otherwise, False message"""
  if check_digit == second_digit:
    return "\nValid!\n"
  else:
    return "\nNot Valid.\n"

def main():
  credit_card_string = input("\nPlease enter the credit card number: ")
  list_of_ints = get_list_of_ints(credit_card_string)
  check_digit, shortened_list = get_check_digit(list_of_ints)
  reversed_list = get_reversed_list(shortened_list)
  alternately_doubled_list = get_alternately_doubled_list(reversed_list)
  subtracted_list = get_subtracted_list(alternately_doubled_list)
  sum_of_list = get_sum_of_list(subtracted_list)
  second_digit = get_second_digit(sum_of_list)
  response = compare_digits(check_digit, second_digit)
  print(response)

main()