#!/usr/bin/python3.9

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('Wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()

#First we import the function we want tested - get_formatted_name()
#We create a class called NameTestCase which will contain a series of unit tests for get_formatted_name()
#The class must inherit from the class unittest.TestCase so python knows how to run the tests
#The class contains a single method that tests one aspect of the get_formatted_name()
#We call the method test_first_last_name() we are verifying that names with only first name and second are formatted correctl
#Any method that starts with test_ will be run automatically when we run test_name_function.py
#Within this test method we call the function we want to test, in this example we call get_formatted_name() with the arguments 'janis' and 'joplin' and assing the result to formatted_name
#We then use one of unittest most useful features: an assert method.
#Assert method verifies that a result you received matches the result you expected to receive, we expect the value of formatted_name to be Janis Joplin, to check if this is true we use unittest's assertEqual() method and pass it formatted_name and 'Janis and Joplin' the line self.assertEqual(formatted_name, 'Janis Joplin')
#if this program is run as the main program we run unittest.main() which runs the test case

#output
"""
.
----------------------------------------------------------------------
Ran 1 test in 0.007s

OK
"""
#the . on the first line of the output tells us that a single test passed
#the next line is it ran one test and the time it took
#the final okay states that all unittest in the test case passed

