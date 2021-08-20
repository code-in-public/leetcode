#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_is_prime_valid(self):
        """
        Valid primes are 2, 3, 5, 7.
        """
        sol = solution.Solution();
        self.assertTrue(sol.isPrime(2))
        self.assertTrue(sol.isPrime(3))
        self.assertTrue(sol.isPrime(7))
        #self.assertTrue(sol.isPrime(863))

    def test_is_prime_invalid(self):
        """
        Valid primes are 2, 3, 5, 7.
        """
        sol = solution.Solution();
        self.assertFalse(sol.isPrime(1))
        self.assertFalse(sol.isPrime(4))
        self.assertFalse(sol.isPrime(6))
        #self.assertFalse(sol.isPrime(864))

    def test_example_1(self):
        """
        Example 1:

        Input: n = 10
        Output: 4
        Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
        """
        sol = solution.Solution();
        n = 10
        self.assertEqual(4, sol.countPrimes(n))

    def test_example_2(self):
        """
        Example 2:

        Input: n = 0
        Output: 0
        """
        sol = solution.Solution();
        n = 0
        self.assertEqual(0, sol.countPrimes(n))

    def test_example_3(self):
        """
        Example 3:

        Input: n = 1
        Output: 0
        """
        sol = solution.Solution();
        n = 1
        self.assertEqual(0, sol.countPrimes(n))

if __name__ == '__main__':
    unittest.main()
