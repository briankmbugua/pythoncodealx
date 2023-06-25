"""Python decorators allow you to change the behaviour of a function without modifying the function itself
BUILDING BLOCKS USED TO CREATE PYTHON DECORATORS
"""
# A FUNCTION IS AN OBJECT.
"""Because a function is an object a function can be assinged to a variable.The function can also be accessed from that variable"""


def my_function():
    print('I am a function')

# Assing the function to a variable without parenthesis. We don't want to execute the function

description = my_function

description()

# Function can be nested inside another funtion

# def outer_function():
#     def inner_function():
#         print('I came from the inner function')
#         # Executing the inner function inside the outer function
#     inner_function()

# outer_function()

# since a function can be nested inside another function it can also be returned


def outer_function():
    """Assing task to student"""

    task= 'Read Python book chapter 3.'
    def inner_function():
        print(task)
    return inner_function

homework = outer_function()

homework()


# A function can be passed to another function as an argument

def friendly_reminder(func):
    """reminder for husband"""

    func()
    print('Don\'t forgt to bring your wallet')


def action():
    print('I am going to the store to buy you something nice')

# calling the friendly_reminder function with the action function used as an argument.
friendly_reminder(action)
