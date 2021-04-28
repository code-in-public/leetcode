#!/usr/bin/env python3

import unittest
import solution

class TestMethods(unittest.TestCase):
    def LinkedListFromArray(self, values):
        if len(values) > 0:
            headNode = solution.ListNode(values[0], None)
            tailPtr = headNode

            if len(values) > 1:
                for value in values[1:]:
                    tailPtr.setNext(solution.ListNode(value))
                    tailPtr = tailPtr.getNext()

            return headNode
        else:
            return None

    def printLinkedList(self, headNode):
        print(self.linkedListToArray(headNode))

    def linkedListToArray(self, headNode):
        result = []
        current = headNode

        while current:
            result.append(current.getValue())
            current = current.getNext()

        return result

    def checkLinkedListsAreEqual(self, headNodeA, headNodeB):
        valuesA = self.linkedListToArray(headNodeA)
        valuesB = self.linkedListToArray(headNodeB)

        return valuesA == valuesB

    def test_example_1(self):
        sol = solution.Solution();
        l1 = self.LinkedListFromArray([2, 4, 3])
        l2 = self.LinkedListFromArray([5, 6, 4])

        expected = [7, 0, 8]

        self.assertEqual(self.linkedListToArray(sol.addTwoNumbers(l1, l2)), expected)

    def test_example_steve7411(self):
        sol = solution.Solution();
        l1 = self.LinkedListFromArray([9])
        l2 = self.LinkedListFromArray([1])

        expected = [0, 1]

        self.assertEqual(self.linkedListToArray(sol.addTwoNumbers(l1, l2)), expected)

    def test_example_2(self):
        sol = solution.Solution();
        l1 = self.LinkedListFromArray([0])
        l2 = self.LinkedListFromArray([0])

        expected = [0]

        self.assertEqual(self.linkedListToArray(sol.addTwoNumbers(l1, l2)), expected)

    def test_example_2(self):
        sol = solution.Solution();
        l1 = self.LinkedListFromArray([9,9,9,9,9,9,9])
        l2 = self.LinkedListFromArray([9,9,9,9])

        expected = [8,9,9,9,0,0,0,1]

        self.assertEqual(self.linkedListToArray(sol.addTwoNumbers(l1, l2)), expected)

if __name__ == '__main__':
    unittest.main()
