# Lab 11 - Simple Calculator

def get_sum(operator, num_one, num_two):
  """accepts two numbers and adds together to produce sum"""
  result = num_one + num_two
  return result

def get_difference(operator, num_one, num_two):
  """accepts two numbers and subtracts one from the other to produce difference"""
  result = num_one - num_two
  return result

def get_product(operator, num_one, num_two):
  """accepts two numbers and multiplies together to produce product"""
  result = num_one * num_two
  return result

def get_quotient(operator, num_one, num_two):
  """accepts two numbers and divides one by the other to produce quotient"""
  result = num_one / num_two
  return result

def run_operation(operator, num_one, num_two):
  """determines which function to run based on operator and returns result"""
  if operator == "+":
    result = get_sum(operator, num_one, num_two)
  elif operator == "-":
    result = get_difference(operator, num_one, num_two)
  elif operator == "*":
    result = get_product(operator, num_one, num_two)
  elif operator == "%" or operator == "/":
    result = get_quotient(operator, num_one, num_two)
  else:
    print(f"Error. {operator} is not a valid operation. Exiting...")
    quit()
  return result

def get_clean_result(result):
  """accepts result and converts to integer if no decimal places are found; otherwise, rounds to two decimal places"""
  if result % 1 == 0:
    clean_result = int(result)
  else:
    clean_result = "{0:.2f}".format(result)
  return clean_result

def main():
  """prompts user for operator and two numbers, runs specified operation and prints result"""
  operator = input("\nWhat is the operation you'd like to perform? (+, -, * or %): ")
  num_one = float(input("What is the first number? "))
  num_two = float(input("What is the second number? "))
  result = run_operation(operator, num_one, num_two)
  clean_result = get_clean_result(result)
  print(f"\nSolution = {clean_result}\n")

main()