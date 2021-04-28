#!/usr/bin/env python3

class Solution(object):
    def decode(self, seen, s):
        if s:
            if s[0] == '0':
                #invalid encoding
                return 0

            if int(s[0]) > 0:
                # First digit is valid
                self.decode(seen + [s[0]], s[1:])

            if len(s) >= 2 and int(s[:2]) <= 26:
                # First 2 digits are valid
                self.decode(seen + [s[:2]], s[2:])

        else:
            # Base case, valid path
            print('Reached the end!')
            print(seen)
            self.numWays += 1

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.numWays = 0
        self.decode([], s)

        return self.numWays
