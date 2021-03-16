# COUNT PRIMES: 
# 
# Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# 
# 
# By convention, 0 and 1 are not prime.


def count_primes(num):
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

