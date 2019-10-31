# Practice 2 - Strings

# Problem #1

def double_letters(user_string):
  """accepts a string from the user and returns another string with every letter doubled"""
  doubled_string = ""
  for letter in user_string:
    doubled_string += letter * 2
  return doubled_string

# user_string = input("Enter some text: ")
# print(double_letters(user_string))


# ----------------------------------------------------------------

# Problem #2

def missing_char(user_string):
  """takes a string and returns a list of strings, each missing a different character"""
  string_list = []
  for letter in user_string:
    removed = user_string.replace(letter, "", 1)
    string_list.append(removed)
  return string_list

# print(missing_char("kitten"))


# ----------------------------------------------------------------

# Problem #3

def latest_letter(user_string):
  """returns the letter that appears the latest in the english alphabet"""
  sorted_string = sorted(user_string)
  return sorted_string[-1]

# print(latest_letter("pneumonoultramicroscopicsilicovolcanoconiosis"))


# ----------------------------------------------------------------

# Problem #4

def count_hi(hi_string):
  """returns the number of occurances of 'hi' in a given string."""
  return hi_string.count("hi")

# print(count_hi("hihi"))


# ----------------------------------------------------------------

# Problem #5

def cat_dog(user_string):
  """returns True if a given string contains the same number of 'cat' as it does 'dog'"""
  cats = user_string.count("cat")
  dogs = user_string.count("dog")
  if cats == dogs:
    return True
  else:
    return False

# print(cat_dog('catdog'))
# print(cat_dog('catcat'))
# print(cat_dog('catdogcatdog'))


# ----------------------------------------------------------------

# Problem #6

def count_letter(letter, word):
  """returns the number of letter occurances in a string"""
  return word.count(letter)

# print(count_letter('i', 'antidisestablishmentterianism'))
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))


# ----------------------------------------------------------------

# Problem #7

def lower_case(user_string):
  """converts input strings to lowercase without any surrounding whitespace"""
  return user_string.lower().strip()

# print(lower_case("SUPER!"))
# print(lower_case("        NANNANANANA BATMAN        "))