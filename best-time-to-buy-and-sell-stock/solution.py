#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices):
        max_profit = 0

        best_buy_price = prices[0]

        for price in prices[1:]:
            # Chech the profit if we sell on this day
            profit = price - best_buy_price
            max_profit = max(max_profit, profit)

            # Update the best buy price
            best_buy_price = min(best_buy_price, price)

        return max_profit
