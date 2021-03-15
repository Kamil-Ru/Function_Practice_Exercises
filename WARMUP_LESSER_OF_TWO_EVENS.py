# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(x,y):

    if x % 2 == 0 and y % 2 == 0 and x <= y: 
        return x
    elif x % 2 == 0 and y % 2 == 0 and y < x:
        return y
    elif x > y:
        return x
    elif y > x:
        return y

# Test:
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(40,20))
print(lesser_of_two_evens(15,133))
print(lesser_of_two_evens(333,333))
print(lesser_of_two_evens(10,10))