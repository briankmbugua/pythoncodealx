#!/usr/bin/python3.9
# In python we can pass a variable number of arguments to a function using special symbols.
#There are two special symbols
#1 *args(Non Keyword Arguments)
#2 **kwargs(Keyword Arguments)

#In the function we should use an * asterisk before the parameter parameter names to pass variable length arguments

# *args

def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n
    print(f"sum: ,{sum}")

adder(1,2,3,4,5)

# **kwargs
# Allows us to pass the variable length of keyword arguments to the function
# we use double asterisk ** before the paramater, The arguments are passed as a dictionary

def intro(**data):
    print("\nDta type of argument:", type(data))

    for key, value in data.items():
        print(f"{key} is {value}")

intro(Firstname="Sita", lastname="sharma", Age=22, phone=123456789)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)