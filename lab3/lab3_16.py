"""
Given the math.ceil function,
- Define a set of unit test cases that exercise the function (Remember Right BICEP)
"""
import unittest
import math


class TestCeil(unittest.TestCase):
    def test_happy_paths(self):
        # Test ceil function when input >= 0
        self.assertAlmostEqual(math.ceil(1), 1.0)
        self.assertAlmostEqual(math.ceil(1.6), 2.0)
        self.assertAlmostEqual(math.ceil(1.4), 2.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(math.ceil(math.pi), 4.0)
        self.assertAlmostEqual(math.ceil(999999999999999999),999999999999999999.0)

    def test_sad_paths(self):
        # Test ceil function when input <= 0
        self.assertAlmostEqual(math.ceil(0), 0)
        self.assertAlmostEqual(math.ceil(-2.3), -2.0)
        self.assertAlmostEqual(math.ceil(True), 1.0)

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, math.ceil, 3+5j)
        self.assertRaises(TypeError, math.ceil, "hello")
        self.assertRaises(TypeError, math.ceil, )
        self.assertRaises(TypeError, math.ceil, [1])
