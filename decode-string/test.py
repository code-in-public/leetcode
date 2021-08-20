#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_0(self):
        sol = solution.Solution();
        input_string = "bc"
        expected = "bc"
        self.assertEqual(expected, sol.decodeString(input_string))

    def test_example_1(self):
        sol = solution.Solution();
        input_string = "3[a]2[bc]"
        expected = "aaabcbc"
        self.assertEqual(expected, sol.decodeString(input_string))

    def test_example_2(self):
        sol = solution.Solution();
        input_string = "3[a2[c]]"
        expected = "accaccacc"
        self.assertEqual(expected, sol.decodeString(input_string))

    def test_example_3(self):
        sol = solution.Solution();
        input_string = "2[abc]3[cd]ef"
        expected = "abcabccdcdcdef"
        self.assertEqual(expected, sol.decodeString(input_string))

    def test_example_4(self):
        sol = solution.Solution();
        input_string = "abc3[cd]xyz"
        expected = "abccdcdcdxyz"
        self.assertEqual(expected, sol.decodeString(input_string))

        #"100[leetcode]"
    def test_example_5(self):
        sol = solution.Solution();
        input_string = "100[leetcode]"
        expected = 100*"leetcode"
        self.assertEqual(expected, sol.decodeString(input_string))

if __name__ == '__main__':
    unittest.main()
