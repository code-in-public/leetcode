#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def Xest_example_1(self):
        sol = solution.Solution();
        instructions = "GGLLGG"

        self.assertEqual(sol.isRobotBounded(instructions), True)

    def Xest_example_2(self):
        sol = solution.Solution();
        instructions = "GG"

        self.assertEqual(sol.isRobotBounded(instructions), False)

    def Xest_example_3(self):
        sol = solution.Solution();
        instructions = "GL"

        self.assertEqual(sol.isRobotBounded(instructions), True)

    def test_example_4(self):
        sol = solution.Solution();
        instructions = "GLRLLGLL"
        self.assertEqual(sol.isRobotBounded(instructions), True)

"""
Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.

Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

"""

if __name__ == '__main__':
    unittest.main()
