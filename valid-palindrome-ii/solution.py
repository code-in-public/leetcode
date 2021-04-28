#!/usr/bin/env python3

class Solution:

    def validPalindromeHelper(self, seen, left_idx, right_idx):
        while (left_idx <= right_idx):
            if self.s[left_idx] == self.s[right_idx]:
                left_idx += 1
                right_idx -= 1
            else:
                if seen:
                    return False

                left_opt = self.validPalindromeHelper(True, left_idx, right_idx-1)
                right_opt = self.validPalindromeHelper(True, left_idx+1, right_idx)

                return left_opt or right_opt

        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_idx = 0
        right_idx = len(s) - 1
        self.s = s

        return self.validPalindromeHelper(False, left_idx, right_idx)
