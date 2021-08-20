#!/usr/bin/env python3

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = height[:]
        right_max = height[:]

        # Get the max depth for each index
        max_depths = []

        # trapped water
        trapped_water = 0

        # Populate left max
        for idx in range(1, len(left_max)):
            left_max[idx] = max(left_max[idx],left_max[idx-1])

        # Populate right max
        for idx in range(len(right_max)-2, -1, -1):
            right_max[idx] = max(right_max[idx],right_max[idx+1])

        # Populate max depth
        for idx in range(len(height)):
            trapped_water += min(left_max[idx], right_max[idx]) - height[idx]

        return trapped_water
