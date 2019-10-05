import random

def printPrediction():
  """randomly selects a prediction from the list of options"""
  predictions = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
  print(f"\n{random.choice(predictions)}\n")

# welcome message - displayed once
print("\nWelcome to Magic 8 Ball!")

def main():
  """prompts user for question, displays prediction, then asks whether to repeat or not"""
  while True:
    input("\nWhat is your question? ")
    printPrediction()
    repeat = input("Would you like to ask another question? (Enter 'done' to exit) ").lower()
    if repeat == "done":
      print("\nIt is written...\n")
      break

main()