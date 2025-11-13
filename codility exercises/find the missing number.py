# unfinished

nums = [1, 2, 4, 5, 6]  # 3 is missing
# N is the total number of numbers in the sequence. 
N = len(nums) + 1

def find_missing(nums, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = nums
    N = expected_sum - actual_sum
    return N
    
print(find_missing(nums, N))
