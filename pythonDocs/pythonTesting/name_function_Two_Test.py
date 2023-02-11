#!/usr/bin/python3.9
from name_function_Two import get_formatted_name #import the function to be tested
import unittest #import unitest module

class Test(unittest.TestCase):#create an object that inherits from unittest.TestCase Class
    """Test for name_function_Two.py"""
    def test_first_las_name(self):#define a method to test the imported function
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('Janis', 'Joplin') #call the function to be test inside the test method
        self.assertEqual(formatted_name, 'Janis Joplin') #use assetEqual method of Test class inherited from unittest.TestCase test the expected result against what you are getting
                                                         #from the function you are testing


if __name__ == "__main__":
    unittest.main()

#This is how a failed unittest looks like
"""
 ./name_function_Two_Test.py
Brian Mbugua Kinyanjui
E
======================================================================
ERROR: test_first_las_name (__main__.Test)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/letbmk/Documents/pythonalx/pythonDocs/pythonTesting/./name_function_Two_Test.py", line 9, in test_first_las_name
    formatted_name = get_formatted_name('Janis', 'Joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.038s

FAILED (errors=1)
"""

