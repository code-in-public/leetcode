#!/usr/bin/env python3

import unittest
import solution

"""
Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""

class TestMethods(unittest.TestCase):
    def test_example_1(self):
        sol = solution.Solution();
        self.assertEqual(sol.validPalindrome("aba"), True)

    def test_example_2(self):
        sol = solution.Solution();
        self.assertEqual(sol.validPalindrome("abca"), True)

    def test_example_3(self):
        sol = solution.Solution();
        self.assertEqual(sol.validPalindrome("abccba"), True)

    def test_example_4(self):
        sol = solution.Solution();
        self.assertEqual(sol.validPalindrome("axcba"), False)

    def test_example_5(self):
        sol = solution.Solution();
        self.assertEqual(sol.validPalindrome("eedede"), True)

if __name__ == '__main__':
    unittest.main()
