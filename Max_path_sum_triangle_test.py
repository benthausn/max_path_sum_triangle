#!/usr/bin/env python

""" Unittests for Max_path_sum_triangle.py"""
__author__ = "Michaela Benthaus"


import unittest
import Max_path_sum_triangle as triangle
#from Max_path_sum_triangle import maxSum
import os

test_array = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

class TestTriangle(unittest.TestCase):
    def test_input_file(self):
        self.assertTrue(os.path.exists(triangle.INPUT_FILE))

    def test_maxSum(self):   # test for small test triangle
        self.assertEqual(triangle.maxSum(test_array), 23)


if __name__ == '__main__':
    unittest.main()
