# longest consecutive streak

# current streak, longest streak so far, number of that streak, 

# unfinished

A = [1, 1, 2, 2, 2, 3, 2, 2]
# output: (2, 3)



def solve(A):
    longest_streak = 0
    current_streak = 1
    current_number = None
    previous_number = A[0]
    best_number = A[0]
    
    for current_number in A[1:]:   # skips the first element
        if current_number == previous_number:
           current_streak += 1
        else:
            previous_number = current_number
        if longest_streak < current_streak:
            longest_streak = current_streak
            best_number = previous_number
                
    return best_number, longest_streak
        
consecutive_streak = solve(A)
print(consecutive_streak)
