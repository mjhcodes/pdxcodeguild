# Lab 17 - Palindrome & Anagram

# ----- PALINDROME -----

def check_palindrome(user_string):
  """accepts user string, compares to its reverse and returns True or False"""
  if user_string == user_string[::-1]:
    return True
  else:
    return False

def print_palindrome_result(user_string, is_palindrome):
  """prints a true of false statement depending on status of palindrome result"""
  if is_palindrome == True:
    print(f"\n'{user_string}' is a palindrome\n")
  else:
    print(f"\n'{user_string}' is not a palindrome\n")

def main_palindrome():
  user_string = input("\nEnter a word: ").lower()
  is_palindrome = check_palindrome(user_string)
  print_palindrome_result(user_string, is_palindrome)

# main_palindrome()

# ----- ANAGRAM -----

def strip_space(word_one, word_two):
  """removes all of the spaces from the two words"""
  stripped_one = word_one.replace(" ", "")
  stripped_two = word_two.replace(" ", "")
  return stripped_one, stripped_two

def sort_words(stripped_one, stripped_two):
  """sorts the letters of each word"""
  sorted_one = sorted(stripped_one)
  sorted_two = sorted(stripped_two)
  return sorted_one, sorted_two

def check_anagram(sorted_one, sorted_two):
  """accepts two strings, checks for equality and returns True or False"""
  if sorted_one == sorted_two:
    return True
  else:
    return False

def print_anagram_result(word_one, word_two, is_anagram):
  """prints a true of false statement depending on status of anagram result"""
  if is_anagram == True:
    print(f"\n'{word_one}' and '{word_two}' are anagrams\n")
  else:
    print(f"\n'{word_one}' and '{word_two}' are not anagrams\n")

def main_anagram():
  word_one = input("\nEnter the first word: ").lower()
  word_two = input("Enter the second word: ").lower()
  stripped_one, stripped_two = strip_space(word_one, word_two)
  sorted_one, sorted_two = sort_words(stripped_one, stripped_two)
  is_anagram = check_anagram(sorted_one, sorted_two)
  print_anagram_result(word_one, word_two, is_anagram)

main_anagram()