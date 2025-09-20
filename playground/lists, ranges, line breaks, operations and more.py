# lists, ranges, line breaks, operations and more

print("Hello\nWorld") # \n is for line breaks


name = input("what's your full name? ")
print(f"Hello {name.title()}") 

# .title() capitalises the first letters of each word in the string variable.
# f is "formatted string literal" and putting it before a string means you can directly embed variables and expressions inside strings using curly braces {}

words = name.split() # .split() chops a string into a list. you can split on commas, dashes, whatever
print(words)


# recapping lists (a container that can hold multiple items)
fruits = ["apple", "orange", "cherry"]
print(fruits[0]) # prints apple
print(str(fruits[1][0])) # the first [] will determine which iten from the list of fruits, and the second [] determines which letter from that item printed.

print(fruits.pop()) # .pop() print and removes last item in list if not specfied
print(fruits.pop(0)) # since i specified it print the first item and removes
# .append() to add things at the end of the 

fruits.append("date")
print(fruits) # since we removed the first and last item in the original one , output will be ['orange', 'date']

x = "lubabah"
print(str(x[0]))


y = "hello"
y = "world"
# reassigning a variable, means that y is now "world" and no longer "hello"


for i in range(7):
    print(i, i*3, i-9, i/2, i+3)

    # basic operations, and ranges. prints all numbers from 0 up until there is as many numbers specfifed in the range (since python starts at 0, here where i said 7, it will end the loop at 6) 
