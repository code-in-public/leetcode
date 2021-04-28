#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_0(self):
        in_string = "1"

        sol = solution.Solution();
        self.assertEqual(sol.numDecodings(in_string), 1)

    def test_example_1(self):
        in_string = "12"

        sol = solution.Solution();
        self.assertEqual(sol.numDecodings(in_string), 2)

    def test_example_2(self):
        in_string = "226"

        sol = solution.Solution();
        self.assertEqual(sol.numDecodings(in_string), 3)

    def test_example_3(self):
        in_string = "0"

        sol = solution.Solution();
        self.assertEqual(sol.numDecodings(in_string), 0)

    def test_example_4(self):
        in_string = "06"

        sol = solution.Solution();
        self.assertEqual(sol.numDecodings(in_string), 0)

if __name__ == '__main__':
    unittest.main()
