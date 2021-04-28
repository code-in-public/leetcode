#!/usr/bin/env python3

import unittest
import solution

"""
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

class TestMethods(unittest.TestCase):
    def test_profitable(self):
        sol = solution.Solution();
        prices = [7,1,5,3,6,4]
        self.assertEqual(sol.maxProfit(prices), 5)

    def test_no_profit(self):
        sol = solution.Solution();
        prices = [7,6,4,3,1]
        self.assertEqual(sol.maxProfit(prices), 0)

if __name__ == '__main__':
    unittest.main()
