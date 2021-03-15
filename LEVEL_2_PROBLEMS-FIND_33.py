# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True has_33([1, 3, 1, 3]) → False has_33([3, 1, 3]) → False


def has_33(nums):
    for x in range(len(nums)):
        if nums[x] == 3 and nums[x+1] == 3 or nums[x] == 3 and nums[x-1]:
            return True
            
        else:
            continue
    return False
    
    
 # WRONG !!!!!!!
    