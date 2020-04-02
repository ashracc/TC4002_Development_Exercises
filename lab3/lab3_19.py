# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354823
# Author: Juan Francisco Corral Stenner

"""
Given the filecmp.cmp function,
Define a set of test cases that exercise the function (Remember Right BICEP)
"""
import filecmp
import unittest


class TestFilecmp(unittest.TestCase):
    def test_is_eq(self):
        self.assertEqual(filecmp.cmp('file1.txt', 'file2.txt'), True)
        self.assertTrue(filecmp.cmp('file1.txt', 'file2.txt'))

    def test_not_eq(self):
        self.assertFalse(filecmp.cmp('file1.txt', 'file3.txt'))

    def test_file_not_found(self):
        self.assertRaises(TypeError, filecmp.cmp, ('file1.txt', 'file4.txt'))
