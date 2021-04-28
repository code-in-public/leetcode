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

    def test_linked_list(self):
        sol = solution.Solution();

        node_values = [1,2,420,3,4,5]
        head = self.LinkedListFromArray(node_values)

        self.printLinkedList(head)

    def test_linked_list_are_equal(self):
        sol = solution.Solution();

        node_values_a = [1, 3, 6]
        headA = self.LinkedListFromArray(node_values_a)

        node_values_b = [1, 3, 6]
        headA = self.LinkedListFromArray(node_values_b)

        self.assertEqual(node_values_a, node_values_b)

    def test_linked_list_are_not_equal(self):
        sol = solution.Solution();

        node_values_a = [1, 3, 6]
        headA = self.LinkedListFromArray(node_values_a)

        node_values_b = [1, 3, 7]
        headA = self.LinkedListFromArray(node_values_b)

        self.assertNotEqual(node_values_a, node_values_b)

    """
    Iterative Tests
    """

    def test_long_lists(self):
        """
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]
        """
        sol = solution.Solution();

        node_values = [1,2,3,4,5]
        head = self.LinkedListFromArray(node_values)

        expected_values = [5, 4, 3, 2, 1]

        reversed_linked_list = sol.reverseListIteratively(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

    def test_single_item_lists(self):
        """
        Input: head = [1]
        Output: [1]
        """
        sol = solution.Solution();

        node_values = [1]
        head = self.LinkedListFromArray(node_values)

        expected_values = [1]

        reversed_linked_list = sol.reverseListIteratively(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

    def test_short_lists(self):
        """
        Input: head = [1, 2]
        Output: [2, 1]
        """
        sol = solution.Solution();

        node_values = [1, 2]
        head = self.LinkedListFromArray(node_values)

        expected_values = [2, 1]

        reversed_linked_list = sol.reverseListIteratively(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

    def test_empty_lists(self):
        """
        Input: head = []
        Output: []
        """
        sol = solution.Solution();

        node_values = []
        head = self.LinkedListFromArray(node_values)

        expected_values = []

        reversed_linked_list = sol.reverseListIteratively(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

    """
    Recursive Tests
    """

    def test_long_lists_recurse(self):
        """
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]
        """
        sol = solution.Solution();

        node_values = [1,2,3,4,5]
        head = self.LinkedListFromArray(node_values)

        expected_values = [5, 4, 3, 2, 1]

        reversed_linked_list = sol.reverseListRecursive(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

    def test_single_item_lists_recurse(self):
        """
        Input: head = [1]
        Output: [1]
        """
        sol = solution.Solution();

        node_values = [1]
        head = self.LinkedListFromArray(node_values)

        expected_values = [1]

        reversed_linked_list = sol.reverseListRecursive(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

    def test_short_lists_recurse(self):
        """
        Input: head = [1, 2]
        Output: [2, 1]
        """
        sol = solution.Solution();

        node_values = [1, 2]
        head = self.LinkedListFromArray(node_values)

        expected_values = [2, 1]

        reversed_linked_list = sol.reverseListRecursive(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

    def test_empty_lists_recurse(self):
        """
        Input: head = []
        Output: []
        """

        sol = solution.Solution();

        node_values = []
        head = self.LinkedListFromArray(node_values)

        expected_values = []

        reversed_linked_list = sol.reverseListRecursive(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

    """
    Stack Tests
    """

    def test_long_lists_recurse(self):
        """
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]
        """
        sol = solution.Solution();

        node_values = [1,2,3,4,5]
        head = self.LinkedListFromArray(node_values)

        expected_values = [5, 4, 3, 2, 1]

        reversed_linked_list = sol.reverseListStack(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

    def test_single_item_lists_recurse(self):
        """
        Input: head = [1]
        Output: [1]
        """
        sol = solution.Solution();

        node_values = [1]
        head = self.LinkedListFromArray(node_values)

        expected_values = [1]

        reversed_linked_list = sol.reverseListStack(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

    def test_short_lists_recurse(self):
        """
        Input: head = [1, 2]
        Output: [2, 1]
        """
        sol = solution.Solution();

        node_values = [1, 2]
        head = self.LinkedListFromArray(node_values)

        expected_values = [2, 1]

        reversed_linked_list = sol.reverseListStack(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

    def test_empty_lists_recurse(self):
        """
        Input: head = []
        Output: []
        """

        sol = solution.Solution();

        node_values = []
        head = self.LinkedListFromArray(node_values)

        expected_values = []

        reversed_linked_list = sol.reverseListStack(head)

        self.assertEqual(self.linkedListToArray(reversed_linked_list), expected_values)

if __name__ == '__main__':
    unittest.main()
