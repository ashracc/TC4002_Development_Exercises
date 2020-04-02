# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354823
# Author: Juan Francisco Corral Stenner

"""
Given the math.pow function,
Define a set of test cases that exercise the function (Remember Right BICEP)
"""
import unittest
import math


class TestPow(unittest.TestCase):
    def test_happy_paths(self):
        self.assertEqual(math.pow(2,2), 4)
        self.assertEqual(math.pow(3.4,2.5), 21.315586785261154)
        self.assertEqual(math.pow(2, 5), 2**5)

    def test_sad_paths(self):
        self.assertEqual(math.pow(-2, 3), -8)
        self.assertEqual(math.pow(2, -3), 0.125)
        self.assertEqual(math.pow(2, -4), 0.0625)

    def test_types(self):
        self.assertRaises(TypeError,math.pow, ("hi",2))

    def test_pow_vs_builtin(self):
        for x in range(23):             # After 23 lose presicion
            self.assertEqual(math.pow(5, x), 5**x)
        for x in range(210):            # After 210 lose presicion
            self.assertAlmostEqual(math.pow(5, x), 5**x)
