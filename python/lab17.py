# Lab 17 - Palindrome & Anagram

def check_palindrome(user_string):
  """accepts user string, compares to its reverse and returns True or False"""
  if user_string == user_string[::-1]:
    return True
  else:
    return False

def print_result(user_string, is_palindrome):
  """prints a true of false statement depending on status of palindrome result"""
  if is_palindrome == True:
    print(f"\n'{user_string}' is a palindrome\n")
  else:
    print(f"\n'{user_string}' is not a palindrome\n")

def main():
  user_string = input("\nEnter a word: ").lower()
  is_palindrome = check_palindrome(user_string)
  print_result(user_string, is_palindrome)

main()