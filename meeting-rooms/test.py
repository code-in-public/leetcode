#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_simple_false(self):
        sol = solution.Solution();
        intervals = [[0,30],[5,10],[15,20]]
        self.assertFalse(sol.canAttendMeetings(intervals))

    def test_simple_true(self):
        sol = solution.Solution();
        intervals = [[7,10],[2,4]]
        self.assertTrue(sol.canAttendMeetings(intervals))

    def test_complex(self):
        sol = solution.Solution();
        intervals = [[8,11],[17,20],[17,20]]
        self.assertFalse(sol.canAttendMeetings(intervals))

if __name__ == '__main__':
    unittest.main()
