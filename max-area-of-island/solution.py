#!/usr/bin/env python3
#
class Solution(object):
    def getIslandArea(self, grid, row, col):
        if col < 0 or row < 0:
            return 0

        if row >= len(grid) or col >= len(grid[row]):
            return 0

        if grid[row][col] == 1:
            grid[row][col] = 0

            deltas = [(1,0), (-1,0), (0, 1), (0, -1)]
            return 1 + sum([self.getIslandArea(grid, row + delta[0], col + delta[1]) for delta in deltas])

        return 0


    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                max_area = max(max_area, self.getIslandArea(grid, row, col))

        return max_area
