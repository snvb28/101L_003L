########################################################################
##
## CS 101 Lab
## Program #13 (Assignment15_Grades program)
## Name: Steven Vu
## Email: snvb28@umsystem.edu
##
## PROBLEM: Creating programs to perform automated testing.
##
## ALGORITHM:
##      1. import unittest module, Grades program, and math module
##      2. create Grade_Test class
##      3. define test_total_returns_total_of_list method to test Grades.total function with given values
##      4. define test_total_returns_0 method to test Grades.total function with given value of 0
##      5. define test_average_one method to test Grades.average function with given values
##      6. define test_average_two method to test Grades.average function with given values
##      7. define test_average_returns_nan method to test Grades.average function that returns math.nan
##      8. define test_median_one method to test Grades.median function with given values
##      9. define test_median_two method to test Grades.median function with given values
##      10. define test_median_returns_ValueError method to test Grades.median function that raises ValueError
##      11. call unittest.main function
##
## ERROR HANDLING:
##          Raising ValueError in Grades.median function if there are no elements in the values list.
##
## OTHER COMMENTS:
##          No additional comments.
##
########################################################################

import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):

    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, 'The total function should return 33')

    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEqual(result, 0, 'The total function should return 0')

    def test_average_one(self):
        result = Grades.average([2, 5, 9])
        self.assertAlmostEqual(result, 5.3333, 4, 'The average function should return 5.3333')

    def test_average_two(self):
        result = Grades.average([2, 15, 22, 9])
        self.assertAlmostEqual(result, 12.0000, 4, 'The average function should return 12.0000')

    def test_average_returns_nan(self):
        result = Grades.average([])
        self.assertIs(result, math.nan, 'The average function should return nan')

    def test_median_one(self):
        result = Grades.median([2, 5, 1])
        self.assertEqual(result, 2, 'The median function should return 2')

    def test_median_two(self):
        result = Grades.median([5, 2, 1, 3])
        self.assertEqual(result, 2.5, 'The median function should return 2.5')

    def test_median_returns_ValueError(self):
        with self.assertRaises(ValueError):
            result = Grades.median([])
            

unittest.main()
