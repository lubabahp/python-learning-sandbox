# if else statements experiments exercises, and user input.

name = input("What's your name? ")  # ask user for their name. input is always a string

if name == "Lubabah":
    print("Hey genius Lubabah!")
else:
    print("Hello there, " + name + "!")

age = input("How old are you?")

if age == 18:
  print("cool!")
else:
  print("nice.")


number = input("Enter your favorite number: ")
number = int(number)  # converting string to integer

if number > 10: # ">" acts like "more than or equal to"
    print("that's a big number!")
else:
    print("that's a small number!")


age = input("What is your age?")
age = int(number) # again, converting string to integer

if age > 18:
  print("adulthood core!")
else:
  print("you are too young!")


answer = input("Do you like Python?").lower()  # converts input to lowercase
# so "answer" is a variable. a variable can have user input.

if answer == "yes":
    print("same!")
else:
    print("hmm, maybe give it a chance!")


favourite_colour = input("what is your favourite colour?")   # python thinks "favourite colour" is two words, so use the underscore.

if favourite_colour == "red":
  print("that's bold!")
elif favourite_colour == "blue": # use elif, not another if. 
  print("that's calming!")
elif favourite_colour == "turquoise":
  print("me too!")
else:
  print("nice.")

months = input("how many months until your birthday?")
months = float(months) # convert months to a floating point number

if months < 1: # must remember to put the colon
    print("that's REALLY close, damn!")
    
elif 1 <= months <= 3: # months are now between 1 and 3
    # must use elif instead of else, because "else" cannot take a condition, it is simply for anything not covered by "if" and "elif" statements. 
    print("that's close, damn!")

else:
    print("ok :)")


