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
  """asks user for numerical input, determines number of quarters, dimes, nickels and pennies based on input and prints the result"""
  starting_pennies = int(input("\nPlease enter the total number of pennies you wish to convert: "))
  quarters, leftover_pennies = get_quarters(starting_pennies)
  dimes, leftover_pennies = get_dimes(leftover_pennies)
  nickels, leftover_pennies = get_nickels(leftover_pennies)
  print(f"\nYou have {quarters} quarter(s), {dimes} dime(s), {nickels} nickel(s) and {leftover_pennies} pennies\n")

main()