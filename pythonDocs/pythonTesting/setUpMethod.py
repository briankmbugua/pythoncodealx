#!/usr/bin/python3.9
"""in test_survey.py we created an instance of AnonymousSurvwy in each test method and we created new responses in each method
unittest.TestCase class has a setUp() method that allows you to create these objects once and then use them in each of your test methods
When you include a setUp() method in a TestCase class, python runs the setUp() method before running each method starting with test_Any objects created in the setUp() method are the available in each test you write"""

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods
        """
        question = "what language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()

"""
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
"""
