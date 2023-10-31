"""
Task - 1
Pick your solution to one of the exercises in this module.
Design tests for this solution and write tests using unittest library.
"""

import unittest
import random
from testing_task import make_operation


class CalcTest(unittest.TestCase):
    """Tests for make_operation function that return the sum or product
    of all the numbers in the arbitrary parameter.

    For example:
    the call make_operation('+', 7, 7, 2) should return 16
    the call make_operation('-', 5, 5, -10, -20) should return 30
    the call make_operation('*', 7, 6) should return 42"""

    def setUp(self):
        # Prepare environment
        self.count_args = random.randint(2, 6)
        self.args = [random.randint(-100, 100) for _ in range(self.count_args)]

    def test_case(self):
        """Test case"""
        self.assertEqual(make_operation('+', 7, 7, 2), 16)
        self.assertEqual(make_operation('-', 5, 5, -10, -20), 30)
        self.assertEqual(make_operation('*', 7, 6), 42)

    def test_case_sum(self):
        """Test case sum"""
        arguments = self.args[2:] if self.count_args > 2 else [0]
        result = sum(self.args)
        self.assertEqual(make_operation('+', self.args[0], self.args[1], *arguments), result)

    def test_case_dev(self):
        """Test case dev"""
        arguments = self.args[2:] if self.count_args > 2 else [0]
        result = 0
        for index,  element in enumerate(self.args):
            if index == 0:
                result = element
            else:
                result -= element
        self.assertEqual(make_operation('-', self.args[0], self.args[1], *arguments), result)

    def test_case_multiply(self):
        """Test case multiply"""
        arguments = self.args[2:] if self.count_args > 2 else [1]
        print(self.args)
        result = 1
        for element in self.args:
            result *= element
        print(result)
        self.assertEqual(make_operation('*', self.args[0], self.args[1], *arguments), result)


if __name__ == "__main__":
    unittest.main()
