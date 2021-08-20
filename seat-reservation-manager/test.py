#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_simple(self):
        capacity = 5
        sm = solution.SeatManager(capacity);
        self.assertEqual(1, sm.reserve())
        self.assertEqual(2, sm.reserve())
        sm.unreserve(2); # // Unreserve seat 2, so now the available seats are [2,3,4,5].
        self.assertEqual(2, sm.reserve())
        self.assertEqual(3, sm.reserve())
        self.assertEqual(4, sm.reserve())
        self.assertEqual(5, sm.reserve())
        sm.unreserve(5); # // Unreserve seat 5, so now the available seats are [5].

if __name__ == '__main__':
    unittest.main()
