# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354823
# Author: Juan Francisco Corral Stenner

"""
Given the math.factorial function,
Define a set of test cases that exercise the function (Remember Right BICEP)
"""
import unittest
import lab3_17
import math


class TestFactorial(unittest.TestCase):
    def test_happy_paths(self):
        # Test factorial function when input >= 0
        self.assertEqual(lab3_17.my_factorial(1), 1)
        self.assertEqual(lab3_17.my_factorial(3), 6)
        self.assertEqual(lab3_17.my_factorial(6), 720)
        self.assertEqual(lab3_17.my_factorial(21), 51090942171709440000)
        self.assertNotEqual(lab3_17.my_factorial(5), 10)

    def test_edge_cases(self):
        self.assertRaises(OverflowError, lab3_17.my_factorial, 999999999999999999)

    def test_sad_paths(self):
        # Test factorial function when input <= 0
        self.assertEqual(lab3_17.my_factorial(0), 1)
        self.assertEqual(lab3_17.my_factorial(True), 1)

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(ValueError, lab3_17.my_factorial, -1)
        self.assertRaises(TypeError, lab3_17.my_factorial, "hello")
        self.assertRaises(TypeError, lab3_17.my_factorial, )
        self.assertRaises(TypeError, lab3_17.my_factorial, [1])
        self.assertRaises(ValueError,lab3_17.my_factorial, math.pi)
