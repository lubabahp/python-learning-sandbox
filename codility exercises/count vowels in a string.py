# count vowels in a string


string = "I love dr stone"
vowels = ["a", "e", "i", "o", "u"]

# expected output: 5

def string_vowels(string):
    count = 0   # it's starting the count of vowels. 
    for char in string:
        if char.lower() in vowels:   # must put .lower() otherwise it would have not counted "I" in "I love dr stone"
            count += 1
        else:
            count += 0
    return count
    
print(string_vowels(string))
        
# took around 10 mins with some help of GPT
