# Lab 15 - Number to Phrase

def get_user_number():
  """prompts user for a number between 0 - 999; returns, if valid; otherwise, prints an error message and prompts again"""
  while True:
    user_number = int(input("\nEnter a number between 0 - 999: "))
    if user_number >= 0 and user_number <= 999:
      return user_number
    else:
      print("\nOut of range. Please enter a number between 0 - 999: ")
      continue

def get_hundreds_digit(user_number):
  """accepts user number and returns the digit in the hundreds position"""
  hundreds_digit = user_number // 100
  return hundreds_digit

def get_hundreds_message(hundreds_digit, ones_list):
  """accepts hundreds digit and ones list and gets the word in the respective index position; then adds word to message and returns response"""
  hundreds_word = ones_list[hundreds_digit]
  hundred_message = (f"{hundreds_word} hundred ")
  return hundred_message

def get_tens_digit(user_number):
  """accepts user number and returns the digit in the tens position"""
  if len(str(user_number)) > 2:
    num_as_string = str(user_number)
    num_sliced = num_as_string[1:]
    user_number = int(num_sliced)
  tens_digit = user_number // 10
  return tens_digit

def get_tens_word(tens_digit, tens_list):
  """accepts tens digit and tens list and returns the word in the respective index position"""
  tens_word = tens_list[tens_digit]
  return tens_word

def get_ones_digit(user_number):
  """accepts user number and returns the digit in the ones position"""
  ones_digit = user_number % 10
  return ones_digit

def get_ones_word(ones_digit, ones_list):
  """accepts ones digit and ones list and returns the word in the respective index position"""
  ones_word = ones_list[ones_digit]
  return ones_word

def get_teens_word(ones_digit, teens_list):
  """accepts ones digit and teens list and returns the word in the respective index position"""
  teens_word = teens_list[ones_digit]
  return teens_word

def get_result(user_number, hundreds_digit, hundreds_message, tens_digit, tens_word, ones_digit, ones_word, teens_word):
  """accepts all variables and returns the appropriate message based on the hundreds, tens and ones digits"""
  if hundreds_digit > 0 and tens_digit == 0 and ones_digit == 0:
    result = ""
  elif tens_digit == 0:
    result = (ones_word)
  elif tens_digit == 1 and ones_digit != 0:
    result = (teens_word)
  elif tens_digit > 0 and ones_digit == 0:
    result = (tens_word)
  elif tens_digit >= 2 and ones_digit != 0:
    result = (tens_word + "-" + ones_word)

  if hundreds_digit > 0:
    hundreds_result = (hundreds_message + result)
    return hundreds_result
  else:
    return result

def main():
  """prompts user for a number and prints the number written out as english words"""
  tens_list = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  teens_list = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  ones_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  user_number = get_user_number()
  hundreds_digit = get_hundreds_digit(user_number)
  hundreds_message = get_hundreds_message(hundreds_digit, ones_list)
  tens_digit = get_tens_digit(user_number)
  tens_word = get_tens_word(tens_digit, tens_list)
  ones_digit = get_ones_digit(user_number)
  ones_word = get_ones_word(ones_digit, ones_list)
  teens_word = get_teens_word(ones_digit, teens_list)
  result = get_result(user_number, hundreds_digit, hundreds_message, tens_digit, tens_word, ones_digit, ones_word, teens_word)
  print(f"\n{user_number} is written as {result}\n")

main()