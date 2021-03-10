'''
You are given a string s representing an attendance record for a student. The record only contains the following three characters:
'A': Absent.
'L': Late.
'P': Present.
A student could be rewarded if his attendance record does not contain more than one 'A' (absent) or more than two consecutive 'L' (late).

Return true if the student could be rewarded according to his attendance record, and false otherwise.

 

Example 1:

Input: s = "PPALLP"
Output: true
Example 2:

Input: s = "PPALLL"
Output: false
 

Constraints:

1 <= s.length <= 1000
s[i] is either 'A', 'L', or 'P'.

Code By Saideep Shetty
'''
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = s.count('A')
        if absent > 1:
            return False
        for i in range(len(s)-2):
            if s[i] == s[i+1] == s[i+2] == 'L':
                return False
        return True