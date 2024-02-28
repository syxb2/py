#!/usr/bin/env python3


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = 0
        b = 0
        for i in s:
            a += ord(i)
        for i in t:
            b += ord(i)
        c = b - a
        return chr(c)


a = Solution
s = "asd"
t = "asdf"
print(a.findTheDifference(a, s, t))
