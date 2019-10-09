# Lab 9 - Unit Converter

# global table conversions
to_meter_table = {
  "feet": .3048,
  "miles": 1609.34,
  "meters": 1,
  "kilometers": 1000,
  "yards": .9144,
  "inches": .0254
}

from_meter_table = {
  "feet": 3.28084,
  "miles": 0.000621371,
  "meters": 1,
  "kilometers": 0.001,
  "yards": 1.09361,
  "inches": 39.3701
}

def translate_input_unit(input_unit):
  """checks user input and stores as written variable"""
  if input_unit.startswith("f"):
    input_unit = "feet"
  elif input_unit.startswith("mi"):
    input_unit = "miles"
  elif input_unit.startswith("me") or input_unit == "m":
    input_unit = "meters"
  elif input_unit.startswith("k"):
    input_unit = "kilometers"
  elif input_unit.startswith("y"):
    input_unit = "yards"
  elif input_unit.startswith("i"):
    input_unit = "inches"
  else:
    print("\nError. Requires an accepted unit of measurement (e.g. miles, kilometers, meters, yards, feet or inches). Exiting... \n")
    quit()
  return input_unit

def translate_output_unit(output_unit):
  """checks user input and stores as written variable"""
  if output_unit.startswith("f"):
    output_unit = "feet"
  elif output_unit.startswith("mi"):
    output_unit = "miles"
  elif output_unit.startswith("me") or output_unit == "m":
    output_unit = "meters"
  elif output_unit.startswith("k"):
    output_unit = "kilometers"
  elif output_unit.startswith("y"):
    output_unit = "yards"
  elif output_unit.startswith("i"):
    output_unit = "inches"
  else:
    print("\nError. Requires an accepted unit of measurement (e.g. miles, kilometers, meters, yards, feet or inches). Exiting... \n")
    quit()
  return output_unit

def main():
  user_distance = float(input("\nWhat is the distance? "))
  if user_distance % 1 == 0:
    user_distance = int(user_distance)
  user_input_units = input("What are the input units? ").lower()
  formal_input_units = translate_input_unit(user_input_units)
  user_output_units = input("What are the output units? ").lower()
  formal_output_units = translate_output_unit(user_output_units)
  converted_meters = user_distance * to_meter_table[formal_input_units]
  converted_output = converted_meters * from_meter_table[formal_output_units]
  if converted_output % 1 < .00001:
    converted_output = int(converted_output)
  else:
    converted_output = "{0:.4f}".format(converted_output)
  print(f"\n{user_distance} {formal_input_units} converts to {converted_output} {formal_output_units}.\n")

main()
