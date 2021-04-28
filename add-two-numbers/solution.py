#!/usr/bin/env python3

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getValue(self):
        return self.val

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def print(self):
        print(self.getValue())
        if self.getNext():
            print(self.getNext().print())

class Solution:
    def getValueOrDefault(self, node, default):
        if node:
            return node.getValue()
        else:
            return default

    def getNextOrNone(self, node):
        if node:
            return node.getNext()
        else:
            return None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sol_list = None

        solution_head = ListNode(0)
        solution_tail = solution_head
        carry = 0

        while (l1 or l2 or carry):
            l1_value = self.getValueOrDefault(l1, 0)
            l2_value = self.getValueOrDefault(l2, 0)

            new_value = l1_value + l2_value + carry

            # Check if requires carry
            if new_value >= 10:
                carry = 1
                new_value -= 10
            else:
                carry = 0

            new_node = ListNode(new_value)
            solution_tail.setNext(new_node)
            solution_tail = solution_tail.getNext()

            l1 = self.getNextOrNone(l1)
            l2 = self.getNextOrNone(l2)

        return solution_head.getNext()
