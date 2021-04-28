#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_0(self):
        sol = solution.Solution();

        nums = [-2, 1]
        expected = 1

        self.assertEqual(expected, sol.maxSubArray(nums))

    def test_example_1(self):
        sol = solution.Solution();

        nums = [-2,1,-3,4,-1,2,1,-5,4]
        expected = 6

        self.assertEqual(expected, sol.maxSubArray(nums))

    def test_example_2(self):
        sol = solution.Solution();

        nums = [1]
        expected = 1

        self.assertEqual(expected, sol.maxSubArray(nums))

    def test_example_3(self):
        sol = solution.Solution();

        nums = [5,4,-1,7,8]
        expected = 23

        self.assertEqual(expected, sol.maxSubArray(nums))

if __name__ == '__main__':
    unittest.main()
