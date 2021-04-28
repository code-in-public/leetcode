#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def test_example_1(self):
        capacity = 2
        lruCache = solution.LRUCache(capacity)
        lruCache.put(1, 1)
        lruCache.put(2, 2)
        self.assertEqual(lruCache.get(1), 1)

        lruCache.put(3, 3)
        self.assertEqual(lruCache.get(2), -1)

        lruCache.put(4, 4)
        self.assertEqual(lruCache.get(1), -1)

        self.assertEqual(lruCache.get(3), 3)
        self.assertEqual(lruCache.get(4), 4)

if __name__ == '__main__':
    unittest.main()

"""
Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

"""
