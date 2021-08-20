#!/usr/bin/env python3

import unittest
import solution

"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""

class TestMethods(unittest.TestCase):
    def test_example_1(self):
        sol = solution.Solution();
        heights = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(sol.trap(heights), 6)

    def test_example_2(self):
        sol = solution.Solution();
        heights = [4,2,0,3,2,5]
        self.assertEqual(sol.trap(heights), 9)

if __name__ == '__main__':
    unittest.main()
