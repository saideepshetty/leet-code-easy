'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
Code By Saideep Shetty
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        total = 0
        while total > 9 or total == 0:
            num = str(num)
            for i in num:
                total += int(i)
            if total > 9:
                num = total
                total = 0
        return total
