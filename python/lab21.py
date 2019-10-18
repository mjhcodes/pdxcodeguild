# Lab 21 - Count Words

import string

def open_text():
  """opens the text file and returns its contents"""
  with open('lab21_the_origin_of_species.txt', 'r') as origin:
    return origin.read()

def make_lowercase(contents):
  """accepts text contents and converts to all lowercase"""
  return contents.lower()

def strip_punctuation(lowercase_contents):
  """accepts text contents and removes all of the punctuation characters"""
  return lowercase_contents.translate(str.maketrans('', '', string.punctuation))

def convert_to_list(stripped_contents):
  """accepts text contents and splits into a list words"""
  return stripped_contents.split()

def convert_to_dict(list_of_words):
  """accepts a list of words and converts to a dictionary with the words as keys and the number of appearances as the value"""
  word_dict = {}
  for word in list_of_words:
    if word not in word_dict.keys():
      word_dict[word] = 1
    word_dict[word] += 1
  return word_dict

def print_top_ten(word_dict):
  """accepts a dictionary of words and their respective count and prints the top ten most frequent occurences with stopwords removed"""
  stopwords = ['of', 'and', 'the', 'in', 'to', 'a', 'that', 'as', 'have', 'be', 'is', 'on', 'by', 'which', 'or', 'are', 'it', 'with', 'for', 'from', 'we', 'this', 'been', 'not', 'but', 'their', 'i', 'at', 'has', 'they', 'will', 'an', 'all', 'same', 'other', 'some', 'more', 'so', 'would', 'may', 'each', 'these', 'many', 'any', 'can', 'if', 'when', 'its', 'than', 'most', 'no', 'one', 'two', 'between', 'thus', 'very', 'there']
  words = list(word_dict.items())
  words.sort(key=lambda tup: tup[1], reverse=True)
  filtered_words = [word for word in words if word[0] not in stopwords]
  for i in range(min(10, len(filtered_words))):
    print(filtered_words[i])

def main():
  contents = open_text()
  lowercase_contents = make_lowercase(contents)
  stripped_contents = strip_punctuation(lowercase_contents)
  list_of_words = convert_to_list(stripped_contents)
  word_dict = convert_to_dict(list_of_words)
  print_top_ten(word_dict)

main()