# mission: returns how many numbers are odd

arr = [1, 2, 3, 4, 5]

def odd_numbers(arr):
    count = 0   # this ensures it starts COUNTING
    for num in arr:
        if num % 2 != 0:   # the % is the modulo function which basically guves you the remainder of dividing two numbers
            count +=1   # increases the count
    return count   # so that it goes back into the function and python remembers it
    
    
print(odd_numbers(arr))     # since the function counts it, it ends up printing how many


# this mock codility problem took 19 mins with the help of chatgpt
