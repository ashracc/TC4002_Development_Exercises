# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354823
# Author: Juan Francisco Corral Stenner

"""
Given the math.factorial function,
Define a set of test cases that exercise the function (Remember Right BICEP)
"""
import unittest
import math


class TestFactorial(unittest.TestCase):
    def test_happy_paths(self):
        # Test factorial function when input >= 0
        self.assertEqual(math.factorial(1), 1)
        self.assertEqual(math.factorial(3), 6)
        self.assertEqual(math.factorial(6), 720)
        self.assertEqual(math.factorial(21), 51090942171709440000)
        self.assertNotEqual(math.factorial(5), 10)

    def test_edge_cases(self):
        self.assertRaises(OverflowError, math.factorial, 999999999999999999)

    def test_sad_paths(self):
        # Test factorial function when input <= 0
        self.assertEqual(math.factorial(0), 1)
        self.assertEqual(math.factorial(True), 1)

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(ValueError, math.factorial, -1)
        self.assertRaises(TypeError, math.factorial, "hello")
        self.assertRaises(TypeError, math.factorial, )
        self.assertRaises(TypeError, math.factorial, [1])
        self.assertRaises(ValueError,math.factorial, math.pi)
