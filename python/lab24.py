# Lab 24 - Rain Data

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

def main():
  data = open_file()
  dates = get_dates(data)
  daily_totals = get_daily_totals(data)
  merged_data = get_merged_data(dates, daily_totals)
  print(merged_data)

main()