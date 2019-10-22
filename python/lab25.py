# Lab 25 - ATM

class ATM:
  def __init__(self, balance = 0, transactions = []):
    self.balance = balance
    self.transactions = transactions
  
  def check_balance(self):
    """returns the account balance"""
    return "Current balance: ${:.2f}".format(self.balance)

  def deposit(self, amount):
    """deposits the given amount in the account and adds transaction to list"""
    self.balance += amount
    self.transactions.append("user deposited ${:.2f}".format(amount))

  def check_withdrawal(self, amount):
    """returns true if the withdrawn amount won't put the account in the negative"""
    if self.balance >= amount:
      return True
  
  def withdraw(self, amount):
    """withdraws the amount from the account and returns it; also, adds transaction to list"""
    self.balance -= amount
    self.transactions.append("user withdrew ${:.2f}".format(amount))
    return self.balance

  def print_transactions(self):
    """prints the list of transactions"""
    print(self.transactions)


def main():
  atm = ATM()
  while True:
    user_action = input("\nWhat would you like to do (deposit, withdraw, check balance, history)? ").lower()

    if user_action.startswith("d"):
      user_amount = float(input("How much would you like to deposit? "))
      atm.deposit(user_amount)
    elif user_action.startswith("w"):
      user_amount = float(input("How much would you like to withdrawal? "))
      is_approved = atm.check_withdrawal(user_amount)
      if is_approved == True:
        atm.withdraw(user_amount)
      else:
        print("Unable to complete request. Insufficient funds.")
    elif user_action.startswith("c"):
      print(atm.check_balance())
    elif user_action.startswith("h"):
      atm.print_transactions()
    else:
      print("Valid transaction type not received... please try again.")

    again = input("\nWould you like to perform another transaction? (y or n) ").lower()
    if again.startswith("n"):
      print("\nTransaction(s) complete. Please visit again soon.\n")
      quit()


main()