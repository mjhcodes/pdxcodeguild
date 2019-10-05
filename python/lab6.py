import random, string

def password_generator():
  """creates a ten character password"""
  i = 0
  password = ""
  while i < 10:
    password += random.choice(string.ascii_letters + string.digits)
    i += 1
  return password

print(password_generator())