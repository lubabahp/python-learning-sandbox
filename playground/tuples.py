# tuples:
# elements always have a defined order.
# immutable: cannot be changed after creation.
# allow duplicate elements: can contain repeated values.
# can contain mixed data types: (1, "apple", True, 3.14)

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
dr_stone_characters = ("senku", "chrome", "suika", "kohaku", "gen")

# You can also create a tuple without parentheses (not recommended for clarity)
another_tuple = 4, 5, 6

# Single-element tuple (COMMA IS REQUIRED)
single_element = (7,)



# accessing tuples
my_tuple = (10, 20, 30)
print(my_tuple[1])  # Output: 20
print(dr_stone_characters[3]) # output: kohaku

# tuple unpacking: assigning individual elements of a tuple to separate variables, all in one line. 
x, y, z = my_tuple 
scientist, browser, melon, gorilla, mentalist = dr_stone_characters
print(y)  # Output: 20
print(melon) # output: suika




# slicing tuples
# follows this pattern: [start:stop:step]
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)

## Basic slice from index 1 to 3 (not including 4)
print(my_tuple[1:4])  # Output: (20, 30, 40)

## Slice from the start to index 2 (not including 3)
print(my_tuple[:3])   # Output: (10, 20, 30)

## Slice from index 2 to the end
print(my_tuple[2:])   # Output: (30, 40, 50)

## Slice from index -3 to the end
print(my_tuple[-3:])  # Output: (30, 40, 50)
### -1 refers to the last element, -2 to the second last and so on.

## Slice with step (skip every 2nd element)
print(my_tuple[::2])  # Output: (10, 30, 50)
print(my_tuple[::3]) # skip every third element
# output: (10, 40)

print(my_tuple[::-1]) # output: (50, 40, 30, 20, 10)
# since its negative and its one, it will just print the exact tuple list but backwards.

print(dr_stone_characters[-3:3]) # output: i assume this doesn't work
# starting with the negative means python thinks its right to left slicing. 


# looping through a tuple
for item in my_tuple:
    print(item) # this will just print each iten in the tuple, line by line. just like range()


# membership test
print(20 in my_tuple)  # Output: True


# immutability:
# "my_tuple[0] = 100" will raise TypeError

# print(my_typle.append())
# append is for adding stuff to a list, so this will result in NameError as tuples are immutable.
