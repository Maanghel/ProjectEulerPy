"""
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th
prime is 13.

What is the 10001st prime number?
"""

import math

def is_prime(number):
    """ check if a number is prime"""
    if number <= 1:
        return False
    for x in range(2, int(math.sqrt(number)) + 1):
        if number % x == 0:
            return False
    return True

def prime_number():
    """ find the 10001st prime number"""
    number = 1
    count = 0
    while count < 10001:
        number += 1
        if is_prime(number):
            count += 1
    return number

if __name__ == "__main__":
    print(prime_number())
