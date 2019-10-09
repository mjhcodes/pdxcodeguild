# Lab 10 - Average Numbers

def sum_nums(nums):
  """accepts list of numbers and returns sum"""
  sum_total = 0
  for num in nums:
    sum_total += num
  return sum_total

def get_length(nums):
  """accepts list of numbers and returns length"""
  list_length = len(nums)
  return list_length

def average_nums(sum_total, list_length):
  """accepts sum total and list length; returns average with four decimal points"""
  num_average = sum_total / list_length
  num_average = "{0:.4f}".format(num_average)
  return num_average

def main(nums):
  sum_total = sum_nums(nums)
  list_length = get_length(nums)
  num_average = average_nums(sum_total, list_length)
  print(num_average)

main([5, 0, 8, 3, 4, 1, 6])