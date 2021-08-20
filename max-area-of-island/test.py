#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_0(self):
        sol = solution.Solution();
        island = [[0, 0]]
        expected = 0
        self.assertEqual(expected, sol.maxAreaOfIsland(island))

    def test_example_1(self):
        sol = solution.Solution();
        island = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]

        expected = 6
        self.assertEqual(expected, sol.maxAreaOfIsland(island))
if __name__ == '__main__':
    unittest.main()
