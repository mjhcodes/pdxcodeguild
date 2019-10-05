import random, string

def password_generator(n):
  """creates a random ten character password"""
  i = 0
  password = ""
  while i < n:
    password += random.choice(string.ascii_letters + string.digits)
    i += 1
  return password

def main():
  """accepts custom password length and prints randomly generated password accordingly"""
  length = int(input("Enter the desired password length: "))
  print(password_generator(length))

main()