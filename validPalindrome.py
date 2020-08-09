'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
'''

class Solution(object):
    def isPalindrome(self, S):
        sl = []
        for i in S:
            if i.isalnum():
                sl.append(i.lower())
        if len(sl) == 0:
            return(True)

        for i in range(0, len(sl)):
            if sl[i] != sl[len(sl)-i-1]:
                return(False)
        
        return(True)
