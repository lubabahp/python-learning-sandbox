arr = [1, 2, 3, 4, 5, 6]
# Output: 12 (because 2 + 4 + 6 = 12)

def even_numbers_sum(arr):
    total = 0   # we need to establish this if we want a total of the numbers. in the same way we establish count = 0 if we wanna coung how many they are. 
    for num in arr:
        if num % 2 == 0:
            total += num   # means "total = total + whatever num is"
    return total
            
print(even_numbers_sum(arr))         

# took around 10 minutes to solve, i knew the logic but asked chatgpt at the end for syntax correction!
