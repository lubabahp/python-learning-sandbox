# find which numbers are duplicated in the list

arr = [2, 2, 2, 1, 4, 4, 5, 6]
# Output: 2 and 4

def dupe(arr):
    nums = set()   # empty set. sets don't allow dupes so it's perfect. list is [] and dict is {}
    duplicates = set()   # puts all dupes we find in here. also a set and not a list so that if something has more than two duplicates it's not printed twice in the dupes list 
    for num in arr:
        if num in nums:
            duplicates.add(num)   # if we've seen it before it's a dupe
        else:
            nums.add(num)   # .add() is for sets, .append() is for list
    return duplicates
            
            
dupli = dupe(arr)
for num in dupli:
    print(num)
    
# started off with finding THE duplicate in a list
# eventually broke the code to see what would happen if there was more than one dupe, as well as if each number in the dupe was more than two
# u basically gotta put ur dupes in a set and return that set and later call the function to show you the dupes 
