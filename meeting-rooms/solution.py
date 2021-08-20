#!/usr/bin/env python3

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """

        start_times = sorted([entry[0] for entry in intervals])
        end_times = sorted([entry[1] for entry in intervals])

        num_meetings = 0
        min_rooms = 0

        while start_times and end_times:
            if start_times[0] < end_times[0]:
                num_meetings += 1

                min_rooms = max(num_meetings, min_rooms)

                start_times.pop(0)
            else:
                num_meetings -= 1
                end_times.pop(0)

        return min_rooms
