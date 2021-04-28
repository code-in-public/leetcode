#!/usr/bin/env python3

class Solution:
    def maxSubArray(self, nums):
        moving_total = nums[0]
        max_moving_total = moving_total

        for num in nums[1:]:
            # if value + moving_total > 0, add to moving total
            if moving_total < 0:
                moving_total = num
            else:
                moving_total += num

            max_moving_total = max(max_moving_total, moving_total)

        return max_moving_total
