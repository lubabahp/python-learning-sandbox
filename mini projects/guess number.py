# unfinished

def guess_number():
    import random 
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    users_guess = input("Guess a number from 1-20: ")
    random_number = random.choice(numbers)


    while True:
      if users_guess.strip() == str(random_number):
        print("Correct!")
        play_again = input("Do you want to play again?")
        if play_again.lower().strip() == "Yes":
          users_guess = input("Okay! Guess a number from 1-20: ")
        else:
          break
      else:
        second_guess = input("Try again: ")
        if second_guess.strip() == str(random_number):
                      
guess_number()            
        
