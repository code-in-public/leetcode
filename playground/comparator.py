#!/usr/bin/env python3


#  You're passing the comparator as the `key` function. You should be
#  passing it as the `cmp`, wrapped in some kind of function that turns
#  it into a proper comparator.

mylist = [[1, 2], [1, 6], [1, 1]]
mylist.sort(key=lambda x: x[0] + x[1])
print(mylist)
