# Lab 14 - Pick 6

import random

def pick6():
  """generates a list of six random numbers"""
  ticket = []
  for num in range(6):
    ticket.append(random.randint(0, 99))
  return ticket

def buy_ticket(balance, expenses):
  """simulates ticket purchase: subtracts $2 from balance and adds $2 to expenses"""
  balance -= 2
  expenses += 2
  return balance, expenses

def num_matches(winning, ticket):
  """accepts two tickets and compares their numbers in order to determine the amount of matches"""
  matches = 0
  for num in range(len(winning)):
    if winning[num] == ticket[num]:
      matches += 1
  return matches

def determine_winnings(balance, earnings, matches):
  """checks number of matches and adds corresponding amount to both the balance and earnings"""
  if matches == 1:
    balance += 4
    earnings += 4
  elif matches == 2:
    balance += 7
    earnings += 7
  elif matches == 3:
    balance += 100
    earnings += 100
  elif matches == 4:
    balance += 50000
    earnings += 50000
  elif matches == 5:
    balance += 1000000
    earnings += 1000000
  elif matches == 6:
    balance += 25000000
    earnings += 25000000
  return balance, earnings

def get_roi(earnings, expenses):
  """accepts total earnings and expenses, then runs the calculation to determine the return on investment"""
  roi = (earnings - expenses) / expenses
  return roi

def main():
  """lottery simulator based on 100,000 purchased tickets; returns final balance, earnings, expenses and ROI"""
  winning_ticket = pick6()
  balance = 0
  earnings = 0
  expenses = 0
  tickets = 100000
  count = 1
  while count <= tickets:
    user_ticket = pick6()
    balance, expenses = buy_ticket(balance, expenses)
    matches = num_matches(winning_ticket, user_ticket)
    balance, earnings = determine_winnings(balance, earnings, matches)
    count += 1
  roi = get_roi(earnings, expenses)
  print(f"\nFinal Balance: ${balance}\nEarnings: ${earnings}\nExpenses: ${expenses}\nROI: {roi}\n")

main()