'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
Code By Saideep Shetty
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        sd = {}
        for index, data in enumerate(t):
            if t[index] not in sd:
                if s[index] not in sd.values():
                    sd[data] = s[index]
                else:
                    return(False)
            else:
                if sd[data] != s[index]:
                    return(False)
        return(True)
