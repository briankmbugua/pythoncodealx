# How to Add Arguments to Decorators in python

"""To add arguments to decorators add *args and **kwargs to the inner function"""


def my_decorator_func(func):

    def wrapper_func(*args, **kwargs):
        # Do something before the function
        func(*args, **kwargs)
        # Do something after the function
    
    return wrapper_func

@my_decorator_func
def my_func(my_arg):
    """Example docstring for function"""

    pass

"""Decorators hide the function they are decorating.If i check __name__ or __doc__ method we get an unexpected result"""


print(my_func.__name__)
print(my_func.__doc__)

"""To fix the above problem use functools,Functools wraps will updte the decorator with the decorated function attribute."""

from functools import wraps

def my_decorater_func(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func


