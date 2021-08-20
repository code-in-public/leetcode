#!/usr/bin/env python3

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # Sort the intervals based on start time
        intervals.sort(key=lambda x:x[0])

        merged_intervals = [intervals.pop(0)]
        end_time = merged_intervals[-1][1]

        while intervals:
            # Check if the new interval overlaps
            new_interval = intervals.pop(0)

            if end_time >= new_interval[0]:
                # Update the end time
                merged_intervals[-1][1] = max(end_time, new_interval[1])
            else:
                merged_intervals.append(new_interval)

            end_time = merged_intervals[-1][1]


        # Add each new interval and merge it
        return merged_intervals
