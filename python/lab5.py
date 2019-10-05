import random

# lists of potential eyes, noses and mouths
eyes = [":", ";", "*", "8", "X"]
noses = [">", "^", "-", "=", "*"]
mouths = [")", "(", "]", "X", "O"]

def emoticon_builder():
  """builds five randomly generated emoticons"""
  i = 0
  while i < 5:
    print(f"{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}")
    i += 1

emoticon_builder()
