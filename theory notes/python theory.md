Python Basics Notes
Variables and Data Types

Variables store data values. No need to declare type explicitly.

Common types: int, float, str, bool, list, dict, tuple, set.

age = 18           # int
price = 19.99      # float
name = "Alice"     # str
is_student = True  # bool

Control Flow
If Statements

Execute code blocks conditionally.

if age >= 18:
    print("Adult")
else:
    print("Minor")

Loops

Repeat code blocks.

for loops iterate over sequences.

while loops run while a condition is true.

for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1

Functions

Reusable blocks of code defined with def.

def greet(name):
    print(f"Hello, {name}!")

greet("Bob")
