#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):

    def test_neighbours_off_edge(self):
        sol = solution.Solution();

        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]

        neighbors = sol.getLandNeighbors(2, 1, grid)

        expected = [
            [1, 1],
            [3 ,1],
            [2, 2],
            [2, 0],
        ]

        self.assertEqual(neighbors, expected)

    def test_neighbours_on_edge(self):
        sol = solution.Solution();

        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]

        neighbors = sol.getLandNeighbors(0, 2, grid)

        expected = [
            [1, 2],
            [0, 3],
            [0, 1],
        ]

        self.assertEqual(neighbors, expected)

    def test_getGridWithoutIsland(self):
        sol = solution.Solution();

        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]

        col_idx = 0
        row_idx = 0

        new_grid = sol.getGridWithoutIsland(col_idx, row_idx, grid)

        expected_grid = [
            ["0","0","0","0","0"],
            ["0","0","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]

        self.assertEqual(grid, expected_grid)

    def test_example_1(self):
        sol = solution.Solution();

        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]

        expected = 1

        self.assertEqual(sol.numIslands(grid), expected)

    def test_example_2(self):
        sol = solution.Solution();

        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]

        expected = 3

        self.assertEqual(sol.numIslands(grid), expected)

if __name__ == '__main__':
    unittest.main()
