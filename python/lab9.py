# Lab 9 - Unit Converter

def feet_to_meters(feet):
  """accepts n amount of feet and converts to meters"""
  meters = feet * .3048
  return meters

def main():
  """asks user for distance in feet, converts to meters and prints result"""
  user_feet = float(input("What is the distance in feet? "))
  converted_meters = feet_to_meters(user_feet)
  print(f"{user_feet:.2f} feet is {converted_meters:.4f} meters.")

main()