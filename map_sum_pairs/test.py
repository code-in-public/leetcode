#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_1(self):
        obj = solution.MapSum();

        key = 'apple'
        val = 3
        obj.insert(key, val)

        prefix = 'ap'
        expected = 3
        self.assertEqual(expected, obj.sum(prefix))

    def test_example_2(self):
        obj = solution.MapSum();

        key = 'apple'
        val = 3
        obj.insert(key, val)

        prefix = 'ap'
        expected = 3
        self.assertEqual(expected, obj.sum(prefix))

        key = 'app'
        val = 2
        obj.insert(key, val)

        prefix = 'ap'
        expected = 5
        self.assertEqual(expected, obj.sum(prefix))

if __name__ == '__main__':
    unittest.main()
