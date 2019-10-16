# Lab 21 - Count Words

def open_text():
  """opens the text file and returns its contents"""
  with open('lab21_the_origin_of_species.txt', 'r') as origin:
    return origin.read()

def make_lowercase(contents):
  """accepts text contents and converts to all lowercase"""
  return contents.lower()

def main():
  contents = open_text()
  lowercase_contents = make_lowercase(contents)
  print(lowercase_contents)

main()