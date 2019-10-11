# Lab 13 - ROT Cipher

import string

def rot_cipher():
  """accepts a string from the user, cycles through string and gathers index position based on the tuple of the alphabet. Moves indices either up or down by 13, then adds encoded letter to string and returns encoded string once completed"""
  word = input("Enter a string to be encoded: ").lower()
  alphabet = tuple(string.ascii_lowercase)
  rot_string = ""
  for char in word:
    i = alphabet.index(char)
    if i < 13:
      rot_string += alphabet[i + 13]
    else:
      rot_string += alphabet[i - 13]
  print(rot_string)

rot_cipher()
