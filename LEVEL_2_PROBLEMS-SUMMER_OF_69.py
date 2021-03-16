# SUMMER OF '69: Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 9 
# (every 6 will be followed by at least one 9). Return 0 for no numbers.


# summer_69([1, 3, 5]) --> 9 
# summer_69([4, 5, 6, 7, 8, 9]) --> 9 
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer_69(_list):
    a = 0
    stop = 0
    for x in _list:
        if x < 6 and stop == 0:
            a = a + x
        elif x == 6:
            stop = 1
        elif x == 9:
            stop = 0
        elif x > 9 and stop == 0:
            a = a + x      
        else:
            continue
    return a

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
print(summer_69([1, 4, 6, 1, 1, 1, 1, 9, 10]))
print(summer_69([1, 4, 6, 1, 1, 1, 1, 9, 10, 6, 1000, 10000, 9]))
