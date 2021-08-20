#!/usr/bin/env python3

from collections import defaultdict
import heapq
class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.min_heap = []
        heapq.heapify(self.min_heap)

        for seat_idx in range(1, n+1):
            heapq.heappush(self.min_heap, seat_idx)

    def reserve(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.min_heap)

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.min_heap, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
