# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True 
# has_33([1, 3, 1, 3]) → False 
# has_33([3, 1, 3]) → False


def has_33(nums):
    k = 0    
    for x in range(len(nums)):
        if k == 2:
            return True
        elif nums[x] == 3:
            k = k + 1
        elif nums[x] != 3:
            k = 0
        elif k == 0:
            return False
        else:
            continue
        
print(has_33([3, 3, 1]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(has_33([3, 3, 3]))
print(has_33([3, 1, 1, 3]))