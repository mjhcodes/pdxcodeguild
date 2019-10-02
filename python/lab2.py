# globals for while loop decisions
hearstory = True
repeat = True

# new line variable to add spacing where appropriate
nl = "\n"

# welcome message - only displays on 1st time through the program
print(f"{nl}Welcome to Mad Libs. Let's get wild!{nl}")

while repeat == True:

  # input variables for the user to enter
  sillyword1 = input("Please enter a silly word: ").capitalize()
  lastname = input("Please enter a last name: ").capitalize()
  illness = input("Please enter an illness: ")
  nounplural = input("Please enter a plural noun: ")
  adjective1 = input("Please enter an adjective: ")
  adjective2 = input("Please enter another adjective: ")
  sillyword2 = input("Please enter another silly word: ").capitalize()
  place = input("Please enter a place: ").capitalize()
  number = input("Please enter a number: ")
  adjective3 = input("Please enter one more adjective: ").capitalize()

  # option to receive the output
  hearstory = input(f"{nl}Would you like to hear the story? (y or n) ").lower()
  if hearstory.startswith("n"):
    print(f"{nl}Odd choice, but I respect it. Goodbye!{nl}")
    break

  # prints final message back to the user
  print(f"{nl}Dear School Nurse:{nl}{nl}{sillyword1} {lastname} will not be attending school today. (S)he has come down with a case of {illness} and has horrible {nounplural} and a(n) {adjective1} fever.{nl}{nl}We have made an appointment with the {adjective2} Dr. {sillyword2}, who studied for many years in {place} and has {number} degrees in pediatrics. He will send you all the information you need. Thank you!{nl}{nl}Sincerely,{nl}{nl}Mrs. {adjective3}{nl}")

  # option to write another Mad Lib
  repeat = input("Would you like to make another story? (y or n) ").lower()
  if repeat.startswith("n"):
    print(f"{nl}Thanks for playing!{nl}")
    break
  else:
    print(f"{nl}Okay, let's go again!{nl}")
    repeat = True

