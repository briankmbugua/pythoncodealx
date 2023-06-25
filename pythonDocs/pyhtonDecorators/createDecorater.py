"""To create decorator function in python, create an outer function that takes a function as an argument.There is also an inner function that wraps around the decorated function"""
# syntax of basic python decorator
def my_decorator_func(func):
    
    def wrapper_func():
        # Do something before the function
        func()
        # Do something after the funtion
    return wrapper_func

"""To use a decorator, you attach it to a function like you see in the code below, We use a decorater by placing the name of the decorator directly above the function we want to use it on.You prefix the decorator function with an @ symbol"""

@my_decorator_func
def my_func():
    pass

# EXAMPLE
# logs the date and time a function was executed
from datetime import datetime

def log_datetime(func):
    """log the date and time of a function"""
    print("outside wrapper")

    def wrapper():
        print(f"Function : {func.__name__}\nRun on: {datetime.today().strftime('%y-%m-%d %H:%M:%S')}")
        print(f"{'-'*30}")
        func()
    return wrapper

@log_datetime
def daily_backup():

    print('Daily backup job has finished')

daily_backup()



