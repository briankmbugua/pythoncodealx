#!/usr/bin/python3.9
#There are other cases where the excat output may not be predictable, but should still be testable

class MyClass:
    pass

def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass())
    [<doctest_unpredictable.MyClass object at 0x10055a2d0>]
    """
    return [obj]

#when the test includes values that are likely to change in unpredictable ways, and where the actual value is not important to the test results, use the ELLIPSIS option to tell doctest to ignore portions of the verification value
print("EXAMPLE 2 WITH #doctest: +ELLIPSIS")

class MyClass:
    pass

def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<doctest_unpredictable.MyClass object at 0x...>]
    """
    return [obj]

#The "#doctest: +ELLIPSIS" comment after the call to unpredictable() tells doctest to turn on the ELLIPSIS option for the test. The ... replaces the memory address in the object id so that the portion of the expected value is ignored

