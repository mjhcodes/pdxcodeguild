def qualify():
  """determines plus or minus grade"""
  remainder = student_grade % 10
  if remainder > 5:
    qualifier = "+"
  elif remainder < 5:
    qualifier = "-"
  else:
    qualifier = ""
  return qualifier

def grader(qualifier):
  """determines letter grade"""
  if student_grade >= 90:
    print("A" + qualifier)
  elif student_grade >= 80:
    print("B" + qualifier)
  elif student_grade >= 70:
    print("C" + qualifier)
  elif student_grade >= 60:
    print("D" + qualifier)
  else:
    print("F")

# main program loop
repeat = True
while repeat:
  student_grade = int(input("Enter a number representing the grade: "))
  qualifier = qualify()
  grader(qualifier)
  repeat = input("Would you like to enter another grade? (y or n) ").lower()
  if repeat.startswith("n"):
    repeat = False