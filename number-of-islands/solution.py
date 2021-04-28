#!/usr/bin/env python3

class Solution:
    def getLandNeighbors(self, row_idx, col_idx, grid):
        """
        Returns at most 4 neighboring co-ordinates, which are land
        """
        neighbors = []
        row_max = len(grid)
        col_max = len(grid[0])

        directions = [
                [-1, 0],
                [1, 0],
                [0, 1],
                [0, - 1],
            ]

        for direction in directions:
            new_col_idx = col_idx+direction[1]
            new_row_idx = row_idx+direction[0]

            if (0 <= new_col_idx < col_max) and (0 <= new_row_idx < row_max):
                if grid[row_idx][col_idx] == '1':
                    neighbors.append([new_row_idx, new_col_idx])

        return neighbors

    def getGridWithoutIsland(self, row_idx, col_idx, grid):
        """
        Remove the island the contains the row and col provided
        """

        # Flip all coordinates == 1
        points_to_flip = [[row_idx, col_idx]]

        while points_to_flip:
            current_point = points_to_flip.pop()

            # Add other neightbors
            neighbors = self.getLandNeighbors(current_point[0], current_point[1], grid)

            points_to_flip.extend(neighbors)
            grid[current_point[0]][current_point[1]] = '0'

        return grid


    def numIslands(self, grid):
        islandCount = 0

        for row_idx, row in enumerate(grid):
            for col_idx, point in enumerate(row):
                # Continue
                if grid[row_idx][col_idx] == '1':
                    # Check if the current coordinate is land
                    # If it is, islandCount++
                    islandCount += 1

                    # Remove the island
                    grid = self.getGridWithoutIsland(row_idx, col_idx, grid)

        return islandCount
