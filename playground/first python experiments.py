x = 10
print(x)
# kinda self explanatory. we assigned x as the variable equal to 10, and we asked the computer to print it (show it on screen)
# starting with a "#" as i'm doing right now is how you make comments, which explain code and make it more readable.
# more blatantly, putting a "#"" at the start of ANYTHING will make python ignore the code.

y = "lubabah"
# quotation marks are always needed for string (lettered) variables. doesn't matter if it's "" or '' they do the same thing. 
print(y)

z = 'i love coding'
print(z[2])
# the "2" in the square  brackets actually means it will print the 3rd character (characters include spaces) in the string of text, because the first character is considered the "0th". 
# and as you can see, single and double quotes do the same thing. 
print(z[0])
# see, it printed "i".

a = " "
print(a)
# i was just wondering how to make a line break, i guess that is it. 

Z = "coding is awesome, and string variables are case sensitive"
print(Z)
# what is says above. variable "Z" is completely different to "z".
print(len(Z))
# "len()" tells you the length (how many characters) are in a string variable.

print(type(Z))
# "type" tells you the data type the variable is. data types include:
# str (string - for text)
print(type(x))
# int (integer)
b = 10.1
print(type(b))
# float (floating point number - basically any decimal)
# *int and float are both numerical data types, and can be both positive and negative.

# list, tuple, range (sequence data types)

# casting is when you specify the data type of a variable. for example, if you want a number to be considered string instead of numeric:
c = str(7)
print(c)
print(type(c))

# boolean: this is the entire spine of logic computers rely on. 
# the only possible outcomes are true (1) and false (0). 
# bool() tells you whether a variable is true or false.

# generally, everything is considered True *except* for:
# - 0 (zero)
# - None
# - empty strings ("" or '')
# - empty containers ([], {}, ())
# - False (obviously)

print(bool(c))  # c = str(7) from before, which is a non-empty string — so it's True.

d = 0
e = "false"     # even though it *says* "false", it's still a string. non-empty = True.
f = "none"      # same with this — just characters, not the special value None.

print(bool(d))  # False, because 0 is literally False in bool logic
print(bool(e))  # True, because it's a string (non-empty)
print(bool(f))  # True again — spelling "none" means nothing to Python
# (i just realised u don't need to start a new line to add comments)

g = None
h = []
i = {}

print(bool(g))  # None is False
print(bool(h))  # empty list is False
print(bool(i))  # empty dictionary is False


jk = "variable made with two letters"
print(jk)
