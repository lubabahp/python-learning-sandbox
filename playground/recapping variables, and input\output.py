# i made this file on the 21st of september, just uploaded it now tho!

# recapping variables, and input/output



# variables and data types:

a = "Good Morning World!"
b = 10 
c = "20"
d = 30.5
print(type(c)) # output: str
print(type(b)) # output: int

print(type(int(c))) # turns a string variable into an integer, if it can. only works if the string is an integer
print(int(c)) # output: 20

print(type(a)) # output: str

print(type(str(b))) # output: str

int()
str()
float()

x = 10
y = "20"
z = int(y) + x
print(z)  # 30
print(type(z))  # <class 'int'>


# input/output

favourite_character = input("Your favourite character? ")
print(f"{favourite_character.title().strip()} is cool!\nYou have great taste!") # f strings allow to print the user's input
# .upper() will make the user's input all uppercase. .lower() will make it all lowercase, and so on. i put .strip() and .title() so that  it will always start with a capital letter and remove any spaces the user may have typed, in the output. 
# \n is for newline, basically a line break. 

print(f"{favourite_character.title().strip()} is a great choice!\tHonestly, they're awesome!")

print("Name\tAge\nAlice\t25\nBob\t30")
# \t is tab space. inserts a horizontal space. useful for neatening stuff up. 


# touching up on how .lower() works again

choice = input("Pick yes or no: ").lower() # this ensures it will print what it says if the user types yes, but is case insensitive. so doesn't matter if its "YES" or "yEs" etc.   
if choice == "yes":
    print("You said yes!")
else:
    print("You said no!")
