#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_1(self):
        in_string = "abcabcbb"
        sol = solution.Solution();
        expected_output = 3
        self.assertEqual(expected_output, sol.lengthOfLongestSubstring(in_string))

    def test_example_2(self):
        in_string = "bbbbb"
        sol = solution.Solution();
        expected_output = 1
        self.assertEqual(expected_output, sol.lengthOfLongestSubstring(in_string))

    def test_example_3(self):
        in_string = "pwwkew"
        sol = solution.Solution();
        expected_output = 3
        self.assertEqual(expected_output, sol.lengthOfLongestSubstring(in_string))

    def test_example_4(self):
        in_string = ""
        sol = solution.Solution();
        expected_output = 0
        self.assertEqual(expected_output, sol.lengthOfLongestSubstring(in_string))

if __name__ == '__main__':
    unittest.main()
