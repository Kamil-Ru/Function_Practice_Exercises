# BLACKJACK: Given three integers between 1 and 11, 
# if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'


# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
import math

def blackjack (x,y,z):
    _sum = x + y + z
    if  _sum <= 21:
        return _sum
    elif _sum > 21 and x == 11 or y == 11 or z == 11:
        return _sum - 10
    elif _sum > 21:
        return 'BUST'


print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))