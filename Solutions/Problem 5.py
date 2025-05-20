"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
withou any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers 
from 1 to 20?
"""

import math

def smallest_number() -> int:
    """returns the smallest positive number that is evenly divisible by all of the numbers
    from 1 to 20 """
    lcm = 1
    for i in range(1, 21):
        lcm = math.lcm(lcm, i)
    return lcm

#########################   Main    ################################

if __name__ == "__main__":
    print(smallest_number())
