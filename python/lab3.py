def getQualifier(remainder):
  """determines plus or minus grade"""
  if remainder > 5:
    qualifier = "+"
  elif remainder < 5:
    qualifier = "-"
  else:
    qualifier = ""
  return qualifier

def getGrade(percentage):
  """determines letter grade"""
  if percentage >= 90:
    grade = "A"
  elif percentage >= 80:
    grade = "B"
  elif percentage >= 70:
    grade = "C"
  elif percentage >= 60:
    grade = "D"
  else:
    grade = "F"
  return grade

def printGrade(grade, qualifier):
  """prints letter grade with qualifier, if applicable"""
  if grade == "F":
    print(f"Student Grade: {grade}")
  else:
    print(f"Student Grade: {grade}{qualifier}")

def main():
  """main program loop"""
  while True:
    percentage = int(input("Enter the grade percentage: "))
    qualifier = getQualifier(percentage % 10)
    grade = getGrade(percentage)
    printGrade(grade, qualifier)
    repeat = input("Would you like to enter another grade? (y or n) ").lower()
    if repeat.startswith("n"):
      break

main()