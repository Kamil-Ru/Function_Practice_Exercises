# COUNT PRIMES: 
# 
# Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# 
# 
# By convention, 0 and 1 are not prime.

def check_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False
                


def count_primes(num):
    count = 0
    for x in range(2, num//2):
        if check_prime(x) == True:
            count = count + 1
        else:
            continue
    return count


'''
    count = 0
    for x in range(num):
        if x == 0 or x == 1:
            continue
        else:
            for y in range(x):
                if y == 0 or y == 1:
                    continue
                elif x % y == 0:
                    count = count + 1
    return count
        
print(count_primes(100))
'''
print(check_prime(13))
print(check_prime(59))
print(count_primes(110))