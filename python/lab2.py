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

# prints final message back to the user
print(f"{nl}Dear School Nurse:{nl}{nl}{sillyword1} {lastname} will not be attending school today. (S)he has come down with a case of {illness} and has horrible {nounplural} and a(n) {adjective1} fever.{nl}We have made an appointment with the {adjective2} Dr. {sillyword2}, who studied for many years in {place} and has {number} degrees in pediatrics. He will send you all the information you need. Thank you!{nl}{nl}Sincerely,{nl}{nl}Mrs. {adjective3}{nl}")