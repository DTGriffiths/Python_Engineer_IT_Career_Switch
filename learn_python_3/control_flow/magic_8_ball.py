# Import random
import random

# Create variables: names, question, answer
name = ''
question = ''
answer = ''

# Create variable: random_number = randint(0, 11)
random_number = random.randint(0, 11)
#print(random_number)

# If/elif random_number and print answer
if random_number == 0:
  answer = "100%"
elif random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "100%"
elif random_number == 11:
  answer = "Magic"
else:
  anser = "Error"

# If/else question == '', print statement
# Nest if/elst name == '', print statement
if question == '':
  print("Please ask a question for the fabric of reality.")
else:
  if name == '':
    print(question)
  else:
    print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer: {answer}")
