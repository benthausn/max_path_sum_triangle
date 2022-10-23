#!/usr/bin/env python

""" Unittests for Max_path_sum_triangle.py"""
__author__ = "Michaela Benthaus"


import unittest
import max_path_sum_triangle as triangle
import os

test_array = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

class TestTriangle(unittest.TestCase):
    def test_input_file(self):
        self.assertTrue(os.path.exists(triangle.INPUT_FILE))

    def test_max_sum(self):   # test for small test triangle, sum = only first value, otherwise loop needed!
        max_path_sum = triangle.max_sum(test_array)
        assert max_path_sum == [[3], [7, 4], [10, 13, 15]]


if __name__ == '__main__':
    unittest.main()
