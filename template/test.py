#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_simple(self):
        sol = solution.Solution();
        self.assertEqual(sol.return_one(), 1)

if __name__ == '__main__':
    unittest.main()
