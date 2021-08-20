#!/usr/bin/env python3

class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        Followers
            x_Coding
            choushou52
            savagecities
        """
        self.children = {}
        self.terminal = False
        self.value = 0

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        current = self

        for c in key:
            if c not in current.children:
                current.children[c] = MapSum()

            current = current.children[c]

        current.terminal = True
        current.value = val

    def getTrieTotals(self, head):
        totals = 0
        if head:
            if head.terminal:
                totals += head.value

            for child in head.children:
                totals += self.getTrieTotals(head.children[child])

        return totals

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sub_tree = self

        for c in prefix:
            if c in sub_tree.children:
                sub_tree = sub_tree.children[c]
            else:
                return 0

        return self.getTrieTotals(sub_tree)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
