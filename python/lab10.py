# Lab 10 - Average Numbers

def get_nums():
  """prompts user for numbers and returns complete list of numbers when finished"""
  num_list = []
  while True:
    new_num = input("Enter a number or type 'done': ")
    try:
      new_num = float(new_num)
      num_list.append(new_num)
    except:
      break
  return num_list

def sum_nums(num_list):
  """accepts list of numbers and returns sum"""
  sum_total = 0
  for num in num_list:
    sum_total += num
  return sum_total

def get_length(num_list):
  """accepts list of numbers and returns length"""
  list_length = len(num_list)
  return list_length

def average_nums(sum_total, list_length):
  """accepts sum total and list length; returns average with four decimal points"""
  num_average = sum_total / list_length
  num_average = "{0:.4f}".format(num_average)
  return num_average

def main():
  """gathers numbers from user, sums total, determines length, calculates average and prints result"""
  num_list = get_nums()
  sum_total = sum_nums(num_list)
  list_length = get_length(num_list)
  num_average = average_nums(sum_total, list_length)
  print(f'\nAverage: {num_average}\n')

main()