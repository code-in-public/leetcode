#!/usr/bin/env python3
class Solution(object):

    def shift(self, char, idx):
        print(char)
        print(idx)
        return chr(ord(char) + idx)

    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx = 0
        result = ''
        while idx < len(s):
            if idx % 2 == 0:
                result += s[idx]
            else:
                result += self.shift(s[idx-1],int(s[idx]))

            idx += 1

        return result
