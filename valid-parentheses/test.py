#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_simple_valid(self):
        """
        Example 1:

        Input: s = "()"
        Output: true
        """
        sol = solution.Solution();
        s = "()"
        self.assertEqual(sol.isValid(s), True)

    def test_complex_valid(self):
        """
        Example 2:

        Input: s = "()[]{}"
        Output: true
        """
        sol = solution.Solution();
        s = "()[]{}"
        self.assertEqual(sol.isValid(s), True)

    def test_simple_invalid(self):
        """
        Example 3:

        Input: s = "(]"
        Output: false
        """
        sol = solution.Solution();
        s = "(]"
        self.assertEqual(sol.isValid(s), False)

    def test_simple_invalid_intersection(self):
        """
        Example 4:

        Input: s = "([)]"
        Output: false
        """
        sol = solution.Solution();
        s = "([)]"
        self.assertEqual(sol.isValid(s), False)

    def test_complix_valid_nested(self):
        """
        Example 5:

        Input: s = "{[]}"
        Output: true
        """
        sol = solution.Solution();
        s = "()[]{}"
        self.assertEqual(sol.isValid(s), True)

if __name__ == '__main__':
    unittest.main()
