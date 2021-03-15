# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    if n <= 110 and n >= 90:
        return True
    elif n <= 210 and n >= 190:
        return True
    else:
        return False

# Test

print(almost_there(104))    # --> True?
print(almost_there(150))    # --> False?
print(almost_there(90))     # --> True?
print(almost_there(209))    # --> True?