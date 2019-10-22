# Lab 25 - ATM

class ATM:
  def __init__(self, balance = 0, transactions = []):
    self.balance = balance
    self.transactions = transactions
  
  def check_balance(self):
    """returns the account balance"""
    return self.balance

  def deposit(self, amount):
    """deposits the given amount in the account"""
    self.balance += amount
    self.transactions.append(f'user deposited ${amount}')

  def check_withdrawal(self, amount):
    """returns true if the withdrawn amount won't put the account in the negative"""
    if self.balance >= amount:
      return True
  
  def withdraw(self, amount):
    """withdraws the amount from the account and returns it"""
    self.balance -= amount
    self.transactions.append(f'user withdrew ${amount}')
    return self.balance

  def print_transactions(self):
    """prints the list of transactions"""
    print(self.transactions)






