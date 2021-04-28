#!/usr/bin/env python3

class Solution:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
    """
    valid_pairs = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
    }

    def isValid(self, s):
        stack = []

        for bracket in s:
            if (self.isOpeningBracket(bracket)):
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False

                last_opening_bracket = stack.pop()
                if not self.isValidClosingBracket(last_opening_bracket, bracket):
                    return False

        if len(stack) > 0:
            return False

        return True

    def isOpeningBracket(self, bracket):
        return bracket in self.valid_pairs

    def isValidClosingBracket(self, last_opening_bracket, closing_bracket):
        return self.valid_pairs[last_opening_bracket] == closing_bracket

     # Solution Ideas:
     # Use a stack:
     #  When an open bracket hit, push onto the stack
     #  When a close bracket is hit:
     #    Check that the current open bracket is the same type
     #    Pop the open
     #
     #  Valid example
     #  current = ,s = "()[]{}" stack : EMPTY
     #  current = (, s = ")[]{}" stack : ( // Push on open bracket
     #  current = ), s = "[]{}" stack : // Pop matching bracket from stack
     #  current = [, s = "]{}" stack : [ // Push on open bracket
     #  current = ], s = "{}" stack : // Pop matching bracket from stack
     #  current = {, s = "}" stack : { // Push on open bracket
     #  current = }, s = "" stack : // Pop matching bracket from stack
     #  Check if the stack is empty
     #
     #  Invalid example
     #  current = ,s = "([)]" stack : EMPTY
     #  current = (, s = "[)]" stack = (
     #  current = [, s = ")]" stack = ([
     #  current = ), s = "]", stack = ([

     # Notes:
     #    Work on identifying edge cases, for example starting with a closing brace causes a pop from an empty stack
