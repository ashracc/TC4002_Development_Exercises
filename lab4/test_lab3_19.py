# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354823
# Author: Juan Francisco Corral Stenner

"""
Given the filecmp.cmp function,
Define a set of test cases that exercise the function (Remember Right BICEP)
"""
import lab3_19
import unittest
import os


class TestFilecmp(unittest.TestCase):
    def test_is_eq(self):
        f1 = os.path.basename(__file__)
        self.assertEqual(lab3_19.my_cmp(f1, 'test_lab3_19.py'), True)
        self.assertTrue(lab3_19.my_cmp(f1, 'test_lab3_19.py'))

    def test_not_eq(self):
        f1 = os.path.basename(__file__)
        with open('myfile.txt', 'w') as fp:
            pass
        f2 = 'myfile.txt'
        self.assertFalse(lab3_19.my_cmp(f1, f2))

    def test_file_not_found(self):
        self.assertRaises(TypeError, lab3_19.my_cmp, ('file1.txt', 'file4.txt'))
