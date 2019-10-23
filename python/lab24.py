# Lab 24 - Rain Data

import datetime
import matplotlib.pyplot as plt

def open_file():
  """opens the file and returns its contents as a list separated by each row"""
  with open('lab24_ankeny_rain.txt', 'r') as data:
    return data.read().split("\n")

def get_dates(data):
  """accepts data and returns a list of just the dates"""
  dates = []
  for row in data:
    row_as_list = row.split(" ")
    for value in row_as_list:
      if len(value) == 11:
        dates.append(value)
  return dates

def get_daily_totals(data):
  """accepts data and returns a list of the first integer located in each row, i.e. the daily total for each date"""
  daily_totals = []
  for row in data:
    row_as_list = row.split(" ")
    for value in row_as_list:
      if value == "-":
        value = 0
      try:
        num = int(value)
        daily_totals.append(num)
        break
      except:
        pass
  return daily_totals

def get_merged_data(dates, daily_totals):
  """accepts two lists and zips together to return as a list of tuples"""
  merged_data = list(zip(dates, daily_totals))
  return merged_data

def calculate_mean(daily_totals):
  """calculates the mean of the data by dividing the total sum by the length of the list"""
  sum_total = sum(daily_totals)
  return sum_total / len(daily_totals)

def calculate_variance(mean, daily_totals):
  """calculates the variance by accepting the mean; then, for each number, subtracts the mean and squares the result; finally, returns the average of those squared differences"""
  sq_diffs = [((num - mean) ** 2) for num in daily_totals]
  sum_sq_diff = sum(sq_diffs)
  return sum_sq_diff / len(sq_diffs)

def get_max_rain_date(merged_data):
  """iterates through the tuples of merged rain data and returns the date with the highest rain total"""
  rain_totals = [date[1] for date in merged_data]
  max_rain_total = max(rain_totals)
  max_rain_date = [date[0] for date in merged_data if date[1] == max_rain_total]
  return max_rain_date[0]

def print_results(mean, variance, max_rain_date):
  """accepts results and prints each back to the user"""
  print(f"\nThe mean of the data is {mean}.")
  print(f"The variance of the data is {variance}.")
  print(f"The date which had the most rain was {max_rain_date}.\n")

def plot_results(dates, daily_totals):
  """creates an x, y graph with the dates along the x-axis and the daily totals along the y-axis"""
  plt.plot(dates, daily_totals)
  plt.ylabel("Daily Totals")
  plt.xlabel("Dates")
  plt.show()

def main():
  data = open_file()
  dates = get_dates(data)
  daily_totals = get_daily_totals(data)
  merged_data = get_merged_data(dates, daily_totals)
  mean = calculate_mean(daily_totals)
  variance = calculate_variance(mean, daily_totals)
  max_rain_date = get_max_rain_date(merged_data)
  print_results(mean, variance, max_rain_date)
  plot_results(dates, daily_totals)

main()
