#!/usr/bin/env python3

class Solution(object):
    def getPoints(self, calories_sum, lower, upper):
        print(calories_sum)
        if calories_sum < lower:
            return -1
        elif calories_sum > upper:
            return 1

        return 0

    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """

        # Points total
        points_total = 0

        # Sliding window sum
        start_idx = 0
        end_idx = k - 1

        calories_sum = sum(calories[:end_idx+1])

        while end_idx < len(calories):
            # Get points for the windows sum
            # Add the points to the totals
            points_total += self.getPoints(calories_sum, lower, upper)

            # Move the sliding window
            # Remove the left most value
            calories_sum -= calories[start_idx]
            start_idx += 1

            end_idx += 1
            if (end_idx < len(calories)):
                calories_sum += calories[end_idx]

        return points_total
