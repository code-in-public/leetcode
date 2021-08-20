#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        sol = solution.Solution();
        self.assertEqual(sol.merge(intervals), expected)

    def test_example_2(self):
        intervals = [[1,4],[4,5]]
        expected = [[1,5]]
        sol = solution.Solution();
        self.assertEqual(sol.merge(intervals), expected)

    def test_example_3(self):
        intervals = [[1,4],[2,3]]
        expected = [[1,4]]
        sol = solution.Solution();
        self.assertEqual(sol.merge(intervals), expected)

    def test_example_4(self):
        intervals = [[1,4],[0,2],[3,5]]
        expected = [[0,5]]
        sol = solution.Solution();
        self.assertEqual(sol.merge(intervals), expected)

    def test_example_5(self):
        intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
        expected = [[1,3],[4,7]]
        sol = solution.Solution();
        self.assertEqual(sol.merge(intervals), expected)

if __name__ == '__main__':
    unittest.main()
