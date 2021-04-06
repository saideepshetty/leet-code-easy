'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
Code By Saideep Shetty
'''
class Solution(object):
    def trailingZeroes(self, n):
        t = 0
        power = 1
        while n > 0:
            n = n // 5**power
            t += n
        return t
