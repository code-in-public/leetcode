#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_1(self):
        sol = solution.Solution();
        input_words = ["a","b","ba","bca","bda","bdca"]
        expected = 4
        self.assertEqual(expected, sol.longestStrChain(input_words))

    def test_example_2(self):
        sol = solution.Solution();
        input_words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
        expected = 5
        self.assertEqual(expected, sol.longestStrChain(input_words))

    def test_example_3(self):
        sol = solution.Solution();
        input_words = ["abcd","dbqca"]
        expected = 1
        self.assertEqual(expected, sol.longestStrChain(input_words))

    def test_example_4(self):
        sol = solution.Solution();
        input_words = ["bc", "bca", "bcd", "bcae", "bced", "bcedf"]
        expected = 4
        self.assertEqual(expected, sol.longestStrChain(input_words))

if __name__ == '__main__':
    unittest.main()
