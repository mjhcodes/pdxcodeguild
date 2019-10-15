# Lab 19 - Blackjack Advice

def get_point_value(card):
  """accepts a card, then uses card as the key to obtain and return the value; if card not in dictionary, prints error message and quits"""
  point_values = {"K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "A": 1}
  try:
    point_value = point_values[card]
  except KeyError:
    print("\nNot a valid playing card. Please try again.\n")
    quit()
  else:
    return point_value

def get_advice(points):
  """accepts a point value and compares to conditions; returns respective advice message"""
  if points <= 16:
    return ("Hit")
  elif points < 21:
    return ("Stay")
  elif points == 21:
    return ("Blackjack!")
  elif points > 21:
    return ("Already Busted")

def main():
  """asks the user for three playing cards and returns advice message based on point total"""
  first_card = input("\nWhat's your first card? ").upper()
  current_total_point_value = get_point_value(first_card)
  second_card = input("What's your second card? ").upper()
  current_total_point_value += get_point_value(second_card)
  third_card = input("What's your third card? ").upper()
  current_total_point_value += get_point_value(third_card)
  advice = get_advice(current_total_point_value)
  print(f"\n{current_total_point_value} {advice}\n")

main()