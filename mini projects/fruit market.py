"""
Fruit Market!
- 
"""

def fruit_market():
  fruits = ("apple", "banana", "cherry", "orange", "melon") 
  # tuple for fruits.

  user_wallet = float(input("How much money do you have? "))
  if user_wallet < 3:
    print("You don't have enough, you can't buy anything")
    exit()
  # must be a floating point number.

  print("Available fruits: ", fruits)
  user_purchase = input("What do you want to buy? ")

  if user_purchase in fruits:
    print("okay. here are the prices: ")
  else:
    print("Sorry, we don't have that available.")  
    exit()
fruit_market()    
