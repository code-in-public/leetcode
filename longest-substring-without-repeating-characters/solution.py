#!/usr/bin/env python3
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        seen = set()
        longest = 0
        start_idx = 0
        end_idx = 1
        seen.add(s[0])

        current_char = s[start_idx]
        seen.add(current_char)

        while end_idx < len(s):
            current_char = s[end_idx]
            if current_char in seen:
                # We have hit a duplicate
                print(s[start_idx:end_idx])
                while s[start_idx-1] != current_char:
                    #seen.remove(s[start_idx])
                    print("Moving start idx")
                    start_idx += 1
            else:
                seen.add(current_char)

            end_idx += 1

        return longest
