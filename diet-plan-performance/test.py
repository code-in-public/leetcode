#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_calories_sum_example_1(self):
        sol = solution.Solution();
        calories = [1,2,3,4,5]
        k = 1
        lower = 3
        upper = 3
        expected_points = 0
        self.assertEqual(expected_points ,sol.dietPlanPerformance(calories, k, lower, upper))

    def test_calories_sum_example_2(self):
        sol = solution.Solution();
        calories = [3, 2]
        k = 2
        lower = 0
        upper = 1
        expected_points = 1
        self.assertEqual(expected_points ,sol.dietPlanPerformance(calories, k, lower, upper))

    def test_calories_sum_example_3(self):
        sol = solution.Solution();
        calories = [6, 5, 0, 0]
        k = 2
        lower = 1
        upper = 5
        expected_points = 0
        self.assertEqual(expected_points ,sol.dietPlanPerformance(calories, k, lower, upper))

if __name__ == '__main__':
    unittest.main()
