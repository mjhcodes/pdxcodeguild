# Lab 9 - Unit Converter

def feet_to_meters(distance):
  """accepts n amount of feet and converts to meters"""
  meters = distance * .3048
  return meters

def miles_to_meters(distance):
  """accepts n amount of miles and converts to meters"""
  meters = distance * 1609.34
  return meters

def meters_to_meters(distance):
  """accepts n amount of meters and returns same amount"""
  meters = distance
  return meters

def kilometers_to_meters(distance):
  """accepts n amount of kilometers and converts to meters"""
  meters = distance * 1000
  return meters

def yards_to_meters(distance):
  """accepts n amount of yards and converts to meters"""
  meters = distance * .9144
  return meters

def inches_to_meters(distance):
  """accepts n amount of inches and converts to meters"""
  meters = distance * .0254
  return meters

def determine_conversion(distance, units):
  """determines conversion based on accepted unit type and converts distance accordingly"""
  if units.startswith("f"):
    converted_meters = feet_to_meters(distance)
  elif units.startswith("mi"):
    converted_meters = miles_to_meters(distance)
  elif units.startswith("me") or units == "m":
    converted_meters = meters_to_meters(distance)
  elif units.startswith("k"):
    converted_meters = kilometers_to_meters(distance)
  elif units.startswith("y"):
    converted_meters = yards_to_meters(distance)
  elif units.startswith("i"):
    converted_meters = inches_to_meters(distance)
  return converted_meters

def main():
  """asks user for distance and units, then converts to meters and prints result, rounded to two decimal places"""
  user_distance = float(input("What is the distance? "))
  user_units = input("What are the units? ").lower()
  converted_meters = determine_conversion(user_distance, user_units)
  print(f"{user_distance:.2f} {user_units} is {converted_meters:.2f} meters.")

main()