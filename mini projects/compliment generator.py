def compliment_generator():
  import random
  name = input("What's your name? ")
  yes = ["yes", "y", "yeah", "yeah", "yea", "yh", "sure", "mhm", "yhh", "yhhh", "please", "pleasee", "yes please", "pls"]
  while True:
      compliments = [f"You're amazing, {name}!", f"You're so smart, {name}!", f"You're beautiful, {name}. So, so beautiful.", f"You are pretty cool, {name}!"]
      compliment = random.choice(compliments)
      print(compliment)
      question = input("Do you want to hear more? ")
      question_clean = question.lower().strip()
      if question_clean in yes:
        print(compliment)
      else:
        break  
compliment_generator()  
