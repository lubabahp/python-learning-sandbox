# finding max number in a list

arr = [2, 8, 1, 4, 5]
# Output: 8

def find_max(arr):
    max_num = arr[0]   # python counts lists the same way it does w strings and square brackets
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

print(find_max(arr))


# took 8 mins with the help of AI
       

# Variable initialization
# Looping through a list
# Conditional logic (if)
# Comparison operators (>)
# Returning values from functions
      

