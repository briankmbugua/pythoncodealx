#!/usr/bin/python3.9
#A variety of Assert Methods
"""you can only use these methods in a class that inherits from unitest.TestCase
assertEqual(a,b) Verify that a == b
assertNotEqual(a,b) verify that a != b
asserTrue(x) verify that x is True
assertFalse(x) verify that x is False
assertIn(item, list) verify that an item is in list
"""

class AnonymousSurvey:
    """Store a question, and prepare to store responses."""
    def __init__(self, question):
        """Store a question and prepare to store responses"""
        self.question = question
        self.responses = []
    def show_question(self):
        """Show the survey question"""
        print(self.question)
    def store_response(self, new_response):
        """store a single response to the survey"""
        self.responses.append(new_response)
    def show_results(self):
        """Show all responses that have been stored"""
        print("Survey results")
        for response in self.responses:
            print(f" - {response}")
