# Lab 14 - Pick 6

import random

def pick6():
  """generates a list of six random numbers"""
  ticket = []
  i = 1
  while i <= 6:
    ticket.append(random.randint(0, 99))
    i += 1
  return ticket

def buy_ticket(balance):
  """accepts current balance and subtracts by two, which is the price of the ticket"""
  balance -= 2
  return balance

def num_matches(winning, ticket):
  """accepts two tickets and compares their numbers in order to determine the amount of matches"""
  matches = 0
  for num in range(len(winning)):
    if winning[num] == ticket[num]:
      matches += 1
  return matches

def determine_winnings(matches, balance):
  """checks number of matches and adds corresponding amount to the balance"""
  if matches == 1:
    balance += 4
  elif matches == 2:
    balance += 7
  elif matches == 3:
    balance += 100
  elif matches == 4:
    balance += 50000
  elif matches == 5:
    balance += 1000000
  elif matches == 6:
    balance += 25000000
  return balance

def main():
  """generates the winning ticket, sets the balance at zero; cycles through 100,000 purchased tickets, checks number of matches, updates balance based on winnings and returns final balance once complete"""
  winning_ticket = pick6()
  balance = 0
  count = 1
  while count <= 100000:
    user_ticket = pick6()
    balance = buy_ticket(balance)
    matches = num_matches(winning_ticket, user_ticket)
    balance = determine_winnings(matches, balance)
    count += 1
  print(f"${balance}")

main()