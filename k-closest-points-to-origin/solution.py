#!/usr/bin/env python3

from math import sqrt, pow

class Solution:
    def distance(self, x1, y1):
        return sqrt(pow((x1 - 0),2) + pow((y1 - 0), 2))

    def handle_if_single(self, points):
        if len(points) == 1:
            return points[0][0], points[0][1]
        else:
            return points

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda point: sqrt(pow((point[0] - 0),2) + pow((point[1] - 0), 2)))

        return self.handle_if_single(points[:k])
