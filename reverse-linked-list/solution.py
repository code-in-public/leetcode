#!/usr/bin/env python3

# Definition for singly-linked list.
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

class Solution(object):
    def reverseListIteratively(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        current = head

        while current:
            next = current.next
            current.setNext(previous)
            previous = current
            current = next

        head = current

        return previous

    def reverseListRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.getNext() == None:
            # Base case empty or single node
            return head
        else:
            # General case
            new_head = self.reverseListRecursive(head.getNext())

            # Rotate pointer from reversed list to head
            head.getNext().setNext(head)
            head.setNext(None)

            return new_head

    def reverseListStack(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return None

        stack = []

        # Populate the stack
        current = head
        while current:
            stack.append(current)
            current = current.getNext()
            stack[-1].setNext(None)

        # Remove each item from the stack
        head = stack.pop()
        current = head

        while stack:
            current.setNext(stack.pop())
            current = current.getNext()

        return head
