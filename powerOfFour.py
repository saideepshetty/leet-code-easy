'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
Code By Saideep Shetty
'''
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 4 or num == 1: 
            return True
        elif num % 2 == 1:
            return False
        else:
            while num > 4 :
                den = num % 4
                num = num / 4
            if num == 4 and den == 0:
                return True
            else:
                return False
