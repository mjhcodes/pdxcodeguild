# Lab 22 - Compute Automated Readability Index

import string

def open_text():
  """opens the text file and returns its contents"""
  filename = 'lab22_gettysburg_address.txt'
  with open(filename, 'r') as gettysburg:
    return filename, gettysburg.read()

def get_characters(contents):
  """accepts text contents and returns the number of characters in the text"""
  characters = 0
  for char in contents:
    if char in string.ascii_letters:
      characters += 1
  return characters

def get_words(contents):
  """accepts text contents and returns the number of words in the text"""
  clean_contents = contents.replace("-", " ")
  word_list = clean_contents.split()
  words = len(word_list)
  return words

def get_sentences(contents):
  """accepts text contents and returns the number of sentences in the text"""
  sentences = 0
  for char in contents:
    if char in [".", "!", "?"]:
      sentences += 1
  return sentences

def get_ari(characters, words, sentences):
  """accepts the number of characters, words and sentences and plugs them into the formula to compute the automated readability index (ARI); if the result is a decimal, rounds up"""
  float_ari = (4.71 * (characters / words)) + (0.5 * (words / sentences)) - 21.43
  if float_ari // 1 != 0:
    float_ari += 1
  ari = int(float_ari)
  return ari

def get_grade_and_ages(ari):
  """accepts ARI and returns the ages and grade level based on ARI scale"""
  ari_scale = {
    1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages': '6-7', 'grade_level': '1st Grade'},
    3: {'ages': '7-8', 'grade_level': '2nd Grade'},
    4: {'ages': '8-9', 'grade_level': '3rd Grade'},
    5: {'ages': '9-10', 'grade_level': '4th Grade'},
    6: {'ages': '10-11', 'grade_level': '5th Grade'},
    7: {'ages': '11-12', 'grade_level': '6th Grade'},
    8: {'ages': '12-13', 'grade_level': '7th Grade'},
    9: {'ages': '13-14', 'grade_level': '8th Grade'},
    10: {'ages': '14-15', 'grade_level': '9th Grade'},
    11: {'ages': '15-16', 'grade_level': '10th Grade'},
    12: {'ages': '16-17', 'grade_level': '11th Grade'},
    13: {'ages': '17-18', 'grade_level': '12th Grade'},
    14: {'ages': '18-22', 'grade_level': 'College'}
  }

  if ari > 14:
    grade = ari_scale[14]['grade_level']
    ages = ari_scale[14]['ages']
  elif ari in ari_scale:
    grade = ari_scale[ari]['grade_level']
    ages = ari_scale[ari]['ages']
  return grade, ages

def print_output(filename, ari, grade, ages):
  """accepts multiple parameters and prints output based on specification"""
  print("\n" + ("-" * 56) + "\n")
  print(f"The ARI for {filename} is {ari}\nThis corresponds to a {grade} level of difficulty\nthat is suitable for an average person {ages} years old.")
  print("\n" + ("-" * 56) + "\n")

def main():
  filename, contents = open_text()
  characters = get_characters(contents)
  words = get_words(contents)
  sentences = get_sentences(contents)
  ari = get_ari(characters, words, sentences)
  grade, ages = get_grade_and_ages(ari)
  print_output(filename, ari, grade, ages)

main()