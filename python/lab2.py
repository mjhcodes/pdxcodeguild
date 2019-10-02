import random

# globals for while loop decisions
hearstory = True
repeat = True

# new line variable to add spacing where appropriate
nl = "\n"

# welcome message - only displays on 1st time through the program
print(f"{nl}Welcome to Mad Libs. Let's get wild!{nl}")

while repeat == True:

  def sillywords():
    """accepts two silly words, stores in a list, shuffles and returns"""
    words = input("Please enter two silly words (separated only by a blank space): ")
    sillyword_list = words.split()
    random.shuffle(sillyword_list)
    return sillyword_list

  # unpacks list into individual variables - raises error and quits if two words aren't rec'd
  try:
    sillyword1, sillyword2 = sillywords()
  except ValueError:
    print(f"{nl}Whoopsie! I said TWO words. Please try that again...{nl}")
    break
  
  # capitalizes both words, as they represent surnames in the story
  sillyword1 = sillyword1.capitalize()
  sillyword2 = sillyword2.capitalize()

  # input variables for the user to enter
  lastname = input("Please enter a last name: ").capitalize()
  illness = input("Please enter an illness: ")
  nounplural = input("Please enter a plural noun: ")
  adjective1 = input("Please enter an adjective: ")
  adjective2 = input("Please enter another adjective: ")
  place = input("Please enter a place: ").capitalize()
  number = input("Please enter a number: ")
  adjective3 = input("Please enter one more adjective: ").capitalize()

  # user option on whether or not to receive the output
  hearstory = input(f"{nl}Would you like to hear the story? (y or n) ").lower()
  if hearstory.startswith("n"):
    print(f"{nl}Odd choice, but I respect it. Goodbye!{nl}")
    break

  # prints final message back to the user - template borrowed from https://www.madtakes.com/
  print(f"{nl}Dear School Nurse:{nl}{nl}{sillyword1} {lastname} will not be attending school today. (S)he has come down with a case of {illness} and has horrible {nounplural} and a(n) {adjective1} fever.{nl}{nl}We have made an appointment with the {adjective2} Dr. {sillyword2}, who studied for many years in {place} and has {number} degrees in pediatrics. He will send you all the information you need. Thank you!{nl}{nl}Sincerely,{nl}{nl}Mrs. {adjective3}{nl}")

  # user option on whether or not to write another version of the Mad Lib
  repeat = input("Would you like to make another story? (y or n) ").lower()
  if repeat.startswith("n"):
    print(f"{nl}Thanks for playing!{nl}")
    break
  else:
    print(f"{nl}Okay, let's go again!{nl}")
    repeat = True

