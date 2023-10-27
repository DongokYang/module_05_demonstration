"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: ACE Faculty
Date: 2023-10-25
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""
 
import unittest
from unittest.mock import patch
from src.functions import greet_name_age, grade_outcome
 
class TestGreetName(unittest.TestCase):
    def test_greet_name_with_all_parameters(self):
        # Arrange
        name = "Joe"
        age = 25
        expected = "Hello Joe, you are 25 years old!"
        # Act
        actual = greet_name_age(name, age)
        # Assert
        self.assertEqual(expected, actual)
    def test_grade_outcome_a_plus(self):
        # Arrange
        grade = 91
        expected = "A+"
        # Act
        actual = grade_outcome(grade)
        # Assert
        self.assertEqual(expected, actual)
    def test_grade_outcome_pass(self):
        # Arrange
        grade = 76
        low_edge = 50
        high_edge = 90
        expected = "Pass"
        # Act
        # actual = grade_outcome(grade)
        # Act and Assert including edge cases
        self.assertEqual(expected, grade_outcome(grade))
        self.assertEqual(expected, grade_outcome(low_edge))
        self.assertEqual(expected, grade_outcome(high_edge))
    def test_grade_outcome_fail(self):
        # Arrange
        grade = 40
        high_edge = 49
        negative = -1
        expected = "Fail"
 
        # Act and Assert including edge cases
        self.assertEqual(expected, grade_outcome(grade))
        self.assertEqual(expected, grade_outcome(high_edge))
        self.assertEqual(expected, grade_outcome(negative))        
