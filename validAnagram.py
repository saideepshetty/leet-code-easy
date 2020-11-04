'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
Code By Saideep Shetty
'''
class Solution(object):
    def isAnagram(self, s, t):
        s_dict = {}
        t_dict = {}

        for i in s:
            s_dict[i] = s_dict.get(i, 0)+1

        for i in t:
            t_dict[i] = t_dict.get(i, 0)+1

        if s_dict == t_dict:
            return(True)
        else:
            return(False)
