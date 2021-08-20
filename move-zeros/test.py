#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example(self):
        """
        nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]
        """
        sol = solution.Solution();
        nums = [0,1,0,3,12]
        expected = [1,3,12,0,0]
        self.assertEqual(expected, sol.moveZeros(nums))

if __name__ == '__main__':
    unittest.main()
