# exploring .lower() string method, defining functions, while loops/breaks

answer = input("what is life?")

# "=" is used for assignment, such as assigning a value to a variable.
# "==" is used for comparison, for checking the equality of two values. 

if answer == "amazing":
  print("sure")
elif answer == "sweet":
  print("cool")
elif answer == "great":
  print("yeah.")
else:
  print("nice")



def chatbot_with_loop(): 
  
  # def = definition, used to define a function. in this case, it's the chatbot. 

    print("Hello! I'm your chatbot. What's your name?")
    name = input()
    
    while True:  # a while loop is used to repeat a section of code an unknown number of times until a specific condition is met.
        print(f"Hey {name}, how are you feeling today?")
        mood = input()

        if "happy" in mood.lower():  # lower() is used to make sure the comparison works even if the user types "HAPPY" or "Happy"
            print("Yay! Keep smiling 😄")
        elif "sad" in mood.lower():
            print("I'm sorry to hear that 😔. Want to talk about it?")
        elif "exit" in mood.lower():
            print("Okay, goodbye! Take care!")
            break # allows you to exit the loop as the condition here is met. 
        else:
            print("Got it! Hope you have a good day!")

chatbot_with_loop()



text = "Hello, WORLD!"
lowercase_text = text.lower() # .lower() converts any string to all lowercase letters. 
print(lowercase_text)



# loops
# This prints numbers 0 to 4, since python always begins by counting from 0.
for i in range(5): 
  # "i" is just a commonly used variable name. 
    print(i)


    import random 

responses = ["That's awesome!", "I'm glad you're happy!", "Oh no, that's sad."]
# lists are enclosed by square brackets. each value is separated by a comma. 

print(random.choice(responses))  # picks a random response



