#!/usr/bin/env python3

l = ['one', 'two', 'three', 'one']

print(l)

seen = set()
for idx in range(len(l)):
    if l[idx] in seen:
        l[idx] = 'anything'
    seen.add(l[idx])

print(l)
