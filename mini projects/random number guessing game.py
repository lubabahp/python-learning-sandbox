def random_number_guessing_game(): 
  # everything that belongs to the function is indented 4 spaces

    import random
    
    play_again = "yes"
    while play_again in ["yes", "yeah", "yh", "y", "yep", "yuh", "yup", "yus"]:
      # must be put in quotation marks otherwise python will think they are variables and not words/string.
       user_guess = int(input("Pick a number from 1 to 10: ")) 
        # colon and space added for UI.

       number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
       random_number = random.choice(number_list)

       # what the user guesses, the list of numbers, and the random number itself picked, must all be separate variables. if you don't make a separate variable for the number and just use random.choice() twice, this will pick the random number two different times/separately each time you type it.
       # random.choice() is how python picks a random variable from a list

       if int(user_guess) == random_number: 
        # we use "if int(number)" not "if input" or "if number" as we want the variable we assigned, not the function itself. 
        print("You guessed correct.")
       else:
        print("Wrong. The random number was", random_number)

       play_again = input("Do you want to play again? ").lower()
random_number_guessing_game()

# that neatly encompasses one function!
