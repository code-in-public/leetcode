#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_0_0(self):
        sol = solution.Solution();

        # Given
        s = "abcde"
        word = 'c'

        # When
        result = sol.isSubseq(s, word)

        # Then
        self.assertTrue(result)

    def test_example_0_fail(self):
        sol = solution.Solution();

        # Given
        s = "abcde"
        word = 'bb'

        # When
        result = sol.isSubseq(s, word)

        # Then
        self.assertFalse(result)

    def test_example_0_1(self):
        sol = solution.Solution();

        # Given
        s = "abcde"
        word = 'x'

        # When
        result = sol.isSubseq(s, word)

        # Then
        self.assertFalse(result)

    def test_example_0_2(self):
        sol = solution.Solution();

        # Given
        s = "abc"
        word = 'abd'

        # When
        result = sol.isSubseq(s, word)

        # Then
        self.assertFalse(result)

    def test_example_1(self):
        sol = solution.Solution();
        # Given
        s = "abcde"
        words = ["a","bb","acd","ace"]

        # When
        result = sol.numMatchingSubseq(s, words)

        # Then
        expected = 3
        self.assertEqual(expected, result)

    def test_example_2(self):
        sol = solution.Solution();

        # Given
        s = "dsahjpjauf"
        words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

        # When
        result = sol.numMatchingSubseq(s, words)

        # Then
        expected = 2
        self.assertEqual(expected, result)

    def test_example_3(self):
        sol = solution.Solution();
        # Given
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        words = ['ab', 'ab']

        # When
        result = sol.numMatchingSubseq(s, words)

        # Then
        expected = 2
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
