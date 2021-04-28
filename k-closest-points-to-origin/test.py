#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_1(self):
        sol = solution.Solution();

        points = [[1,3],[-2,2]]
        k = 1

        kClosestPts = sol.kClosest(points, k)

        print(kClosestPts)

        self.assertEqual(kClosestPts, (-2,2))

    def test_example_2(self):
        sol = solution.Solution();

        points = [[3,3],[5,-1],[-2,4]]
        k = 2

        kClosestPts = sol.kClosest(points, k)

        print(kClosestPts)

        self.assertEqual(set(kClosestPts), set([[-2, 4], [3, 3]]))

if __name__ == '__main__':
    unittest.main()
