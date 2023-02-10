#!/usr/bin/python3.9

def add(*nums):
    """
    function to enter variable number of arguments and return their total
    """
    total = 0
    for num in nums:
        total = total + num
    print(total)

add(1,2,3)