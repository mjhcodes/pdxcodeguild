# Lab 25 - ATM

class ATM:
  def __init__(self, balance = 0):
    self.balance = balance
  
  def check_balance(self):
    """returns the account balance"""
    return self.balance

  def deposit(self, amount):
    """deposits the given amount in the account"""
    self.balance += amount

  def check_withdrawal(self, amount):
    """returns true if the withdrawn amount won't put the account in the negative"""
    if self.balance >= amount:
      return True
  
  def withdraw(self, amount):
    """withdraws the amount from the account and returns it"""
    self.balance -= amount
    return self.balance
