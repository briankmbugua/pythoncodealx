"""You can use decorators with classes as well.Let's see how you use decorators with a Python class.There is no @ character innvolved.With the __call__ method the decorator is executed when an instance of the class is created"""

# EXAMPLE
"""This class keeps track of the number of times a function to query to an API has been run.Once it reaches the limit the decorator stops the function from executing"""

from typing import Any
import requests

class LimitQUery:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.limit = args[0]