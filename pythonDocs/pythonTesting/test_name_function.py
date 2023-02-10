#!/usr/bin/python3.9

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()

#First we import the function we want tested - get_formatted_name()
#We create a class called NameTestCase which will contain a series of unit tests for get_formatted_name()
#The class must