#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_1(self):
        sol = solution.Solution()
        input_string = 'a1c1e1'
        expected_output_string = 'abcdef'
        self.assertEqual(expected_output_string, sol.replaceDigits(input_string))

    def test_example_1(self):
        sol = solution.Solution()
        input_string = 'a1b2c3d4e'
        expected_output_string = 'abbdcfdhe'
        self.assertEqual(expected_output_string, sol.replaceDigits(input_string))

    def test_shift_1(self):
        """
        shift('a', 5) = 'f'
        """
        sol = solution.Solution()
        input_char = 'a'
        input_index = 5
        expected_output = 'f'
        self.assertEqual(expected_output, sol.shift(input_char, input_index))

if __name__ == '__main__':
    unittest.main()
