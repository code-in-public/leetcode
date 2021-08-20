#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def containsNode(self, root, target):
        result = False

        if root == None:
            result = False
        elif root.value == target.value:
            result = True
        elif self.containsNode(root.left, target):
            result = True
        elif self.containsNode(root.right, target):
            result = True

        return result

    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None

        # Check the root node first
        if root.val == p.val:
            # Check that q exists in one of the subtrees
            if self.containsNode(root.left, q) or self.containsNode(root.right, q):
                return root

        # Check the root node first
        if root.val == q.val:
            # Check that p exists in one of the subtrees
            if self.containsNode(root.left, p) or self.containsNode(root.right, p):
                return root

        # Check down the left and right subtrees
        if self.containsNode(root.left, p) and self.containsNode(root.right, q):
            return root

        if self.containsNode(root.left, q) and self.containsNode(root.right, p):
            return root

        # Recurse
        left_ancestor = self.lowestCommonAncestor(root.left, p, q)
        if left_ancestor:
            return left_ancestor

        right_ancestor = self.lowestCommonAncestor(root.right, p, q)
        if right_ancestor:
            return right_ancestor
