# globals for while loop decisions
hearstory = True
repeat = True

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

  nl = "\n" # new line variable to add spacing to final output

  # option to receive the output
  hearstory = input("Would you like to hear the story? (y or n) ")
  if hearstory.startswith("n"):
    break

  # prints final message back to the user
  print(f"{nl}Dear School Nurse:{nl}{nl}{sillyword1} {lastname} will not be attending school today. (S)he has come down with a case of {illness} and has horrible {nounplural} and a(n) {adjective1} fever.{nl}We have made an appointment with the {adjective2} Dr. {sillyword2}, who studied for many years in {place} and has {number} degrees in pediatrics. He will send you all the information you need. Thank you!{nl}{nl}Sincerely,{nl}{nl}Mrs. {adjective3}{nl}")

  # option to write another Mad Lib
  repeat = input("Would you like to make another story? (y or n) ")
  if repeat.startswith("n"):
    print(f"{nl}Thanks for playing!{nl}")
    break
  else:
    print(f"{nl}Okay, let's go again!{nl}")
    repeat = True

