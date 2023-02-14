#!/usr/bin/python3.9
import unittest #import unittest module
from survey import AnonymousSurvey #import the class you want tested

class TestAnonymousSurvey(unittest.TestCase):#A test class inheritting from unittest.TestCase
    """Tests for class AnonymousSurvey"""
    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        question = "What language did you learn first"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual resppnses are stored properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'spanish', 'mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)
if __name__ == '__main__':
    unittest.main()

#output
"""
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""

#output after adding the second test
"""
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
"""

