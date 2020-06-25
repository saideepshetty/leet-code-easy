
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, int):
        int1= int
        if int<0:
            int = int*-1
        b = 0
        while int>0:
            a = int%10
            int = int//10
            b = b*10 + a
    
        x = (2 << 30) - 1 
        
        if int1<0:
            b = b*-1   
        if  b < (-1 * x) or b > x:
            return 0
        return b