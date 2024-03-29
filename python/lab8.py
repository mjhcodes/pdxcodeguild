# Lab 8 - Make Change

def get_quarters(pennies):
  """accepts n amount of pennies, determines number of quarters, determines remaining pennies and returns both"""
  quarters = pennies // 25
  leftover_pennies = pennies - (quarters * 25)
  return quarters, leftover_pennies

def get_dimes(pennies):
  """accepts n amount of pennies, determines number of dimes, determines remaining pennies and returns both"""
  dimes = pennies // 10
  leftover_pennies = pennies - (dimes * 10)
  return dimes, leftover_pennies

def get_nickels(pennies):
  """accepts n amount of pennies, determines number of nickels, determines remaining pennies and returns both"""
  nickels = pennies // 5
  leftover_pennies = pennies - (nickels * 5)
  return nickels, leftover_pennies

def main():
  """asks user for dollar amount, converts to pennies, determines number of quarters, dimes, nickels and pennies based on input and prints the result"""
  user_dollar_amount = float(input("\nPlease enter the dollar amount which you wish to convert: $"))
  starting_pennies = user_dollar_amount * 100
  quarters, leftover_pennies = get_quarters(starting_pennies)
  dimes, leftover_pennies = get_dimes(leftover_pennies)
  nickels, leftover_pennies = get_nickels(leftover_pennies)
  print(f"\nYou have {int(quarters)} quarter(s), {int(dimes)} dime(s), {int(nickels)} nickel(s) and {int(leftover_pennies)} pennies\n")

main()