# fruits basket, made on 27-07-2025 on my phone (so i ended up not uploading it to github earlier)

python:
def fruits_basket():
    import random
    fruits = ["apple", "banana", "orange", "mango", "cherry", "jackfruit", "grape", "pear"]
    
    user_pick = input("pick a fruit from the basket. ").lower().strip()
    # .strip() essentially strips whitespace from the beginning and end of the string
    if user_pick == "apple":
        print("nice choice!")
    elif user_pick == "banana":
        print("sweet!")
    elif user_pick == "orange":
        print("cool")
    else:
        fruit = random.choice(fruits)
        if fruit[0].lower() in ["a", "e", "i", "o", "u"]:
            # essentially asking, "is the first letter of the fruit inside this list?"
            print("sure, you can have an", fruit)
        else:
            print("sure, you can have a", fruit)
fruits_basket()
