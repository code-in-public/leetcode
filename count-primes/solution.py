#!/usr/bin/env python3

import math

class Solution:
    def __init__(self):
        #self.max_candidate = 5 * (10**3)
        self.max_candidate = 15
        self.seive = [0]*self.max_candidate
        self.populateTheSeive()

    def populateTheSeive(self):
        for step in range(2, self.max_candidate):
            # Mark each multiple of step on the seive
            for candidate in range(step*step, self.max_candidate, step):
                self.seive[candidate] += 1

    def isPrime(self, n):
        """
        Checks the count of the seive
        """
        if n >=2 and self.seive[n] == 0:
            return True
        else:
            return False

    def countPrimes(self, n):

        count = 0
        for num in range(1, n):
            if self.isPrime(num):
                count += 1

        return count
