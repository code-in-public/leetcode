#!/usr/bin/env python3

class Position(object):
    def __init__(self, x, y, current_direction):
        self.x = x
        self.y = y
        self.current_direction = current_direction

    def turn_right(self):
        if self.current_direction == 'N':
            self.current_direction = 'E'
        elif self.current_direction == 'E':
            self.current_direction = 'S'
        elif self.current_direction == 'S':
            self.current_direction = 'W'
        else:
            self.current_direction = 'N'

    def turn_left(self):
        if self.current_direction == 'N':
            self.current_direction = 'W'
        elif self.current_direction == 'W':
            self.current_direction = 'S'
        elif self.current_direction == 'S':
            self.current_direction = 'E'
        else:
            self.current_direction = 'N'

    def go(self):
        if self.current_direction == 'N':
            self.y += 1
        elif self.current_direction == 'E':
            self.x += 1
        elif self.current_direction == 'S':
            self.y -= 1
        elif self.current_direction == 'W':
            self.x -= 1

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        position = Position(0, 0, 'N')

        print(position.x, position.y, position.current_direction)

        # Apply the movements
        for instruction in instructions:
            if instruction == 'R':
                position.turn_right()
            elif instruction == 'L':
                position.turn_left()
            else:
                position.go()
            print(position.x, position.y, position.current_direction)

        # Check location and direction
        # If back at the origin, is it bounded
        if position.x == 0 and position.y == 0:
            return True

        # If not back at the origin and pointing not North
        # Then bounded
        if position.current_direction == 'N':
            return False

        return True
