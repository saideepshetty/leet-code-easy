'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
class Solution:
    def isPalindrome(self, x):
        if x>=0:
            s = str(x)
            alist = list(s)
            alen = len(alist)
            flag = 0

            for i in range(0, alen//2):
                    if alist[i] == alist[alen-i-1]:
                        flag = 0
                    else:
                        flag = 1
                        break

            if flag == 0:
                return True
            else:
                return False
        else:
            return False