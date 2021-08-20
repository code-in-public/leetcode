#!/usr/bin/env python3


class Thing(object):
    def __init__(self, value):
        self.value = value

def changeThing(thing):
    thing.value = 'NewValue'

def changeList(inList):
    #inList = [1, 2, 3]
    inList[0] = 1
    inList[1] = 2
    inList[2] = 3

originalList = [4, 5, 6]

print(originalList)
# Expect 4, 5, 6

changeList(originalList)

print(originalList)
# Expect 4, 5, 6

oldThing = Thing('OldValue')
print(oldThing.value)
changeThing(oldThing)
print(oldThing.value)
