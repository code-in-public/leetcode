#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_1(self):
        words = ["hello","leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        sol = solution.Solution();
        self.assertEqual(sol.isAlienSorted(words, order), True)

    def test_example_2(self):
        words = ["word","world","row"]
        order = "worldabcefghijkmnpqstuvxyz"
        sol = solution.Solution();
        self.assertEqual(sol.isAlienSorted(words, order), False)

    def test_example_3(self):
        words = ["apple","app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        sol = solution.Solution();
        self.assertEqual(sol.isAlienSorted(words, order), False)

if __name__ == '__main__':
    unittest.main()
