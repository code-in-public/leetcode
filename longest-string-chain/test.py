#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_simple(self):
        sol = solution.Solution();
        expected = 1
        self.assertEqual(expected, sol.return_one())

if __name__ == '__main__':
    unittest.main()
