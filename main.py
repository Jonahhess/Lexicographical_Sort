""" The credit for the solution goes to Chaim Fishman.
    Implementation by Jonah Hess.
    The fast digit count function was taken from the following:
    https://stackoverflow.com/questions/2189800/how-to-find-length-of-digits-in-an-integer
    but any implementation could work.

    The goal is to sort numbers lexicographically, as opposed to sorting by value.
    For example, 100 > 11 > 123, as we look at the order of appearance of the digits.
    The naive approach is to loop through each digit and sort them one at a time, but the runtime scales linearly with the 
    size of the longest number.

    A very clever approach is to notice that lexicographical ordering is how we sort remainders.
    Therefore, instead of looping over all digits, we can instead sort our numbers by treating them as remainders.

    Some edge cases may exist, as a by-product of floating-point imprecision.
"""

import time
import random

def num_as_remainder(i):
    return i / 10**len("%i" % i)

def main():
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    array.sort(key=num_as_remainder) # in place
    print(array)

def test():
    array = []
    average_time = 0
    for i in range(100):
        random.seed(i)
        for i in range(10000):
            array.append(random.randint(0,9999999))
        start = time.time()
        array.sort(key=num_as_remainder) # in place
        end = time.time()
        result = end-start
        average_time += result
        array = []
    print(result / 100)

main()