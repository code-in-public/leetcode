#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def xest_example_1(self):
        sol = solution.Solution();

        numCourses = 2
        prerequisites = [[1,0]]
        self.assertEqual(True, sol.canFinish(numCourses, prerequisites))

    def test_example_2(self):
        sol = solution.Solution();

        numCourses = 2
        prerequisites = [[1,0], [0, 1]]
        self.assertEqual(False, sol.canFinish(numCourses, prerequisites))

    def xest_example_3(self):
        sol = solution.Solution();

        numCourses = 5
        prerequisites = [[1,4],[2,4],[3,1],[3,2]]
        self.assertEqual(True, sol.canFinish(numCourses, prerequisites))

    def test_example_4(self):
        sol = solution.Solution();
        numCourses = 3
        prerequisites = [[0,1],[0,2],[1,2]]
        self.assertEqual(True, sol.canFinish(numCourses, prerequisites))

    def xest_example_5(self):
        sol = solution.Solution();
        numCourses = 7
        prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
        self.assertEqual(True, sol.canFinish(numCourses, prerequisites))

if __name__ == '__main__':
    unittest.main()
