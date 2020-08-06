'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        output = list(s)
        storeVowels = []
        op = ''

        for i in s:
            if i == 'a' or i == 'e' or i == 'o' or i == 'u' or i == 'i' or i == 'A' or i == 'E' or i == 'O' or i == 'U' or i == 'I':
                storeVowels.append(i)

        for ind, val in enumerate(s):
            if val == 'a' or val == 'e' or val == 'o' or val == 'u' or val == 'i' or val == 'A' or val == 'E' or val == 'O' or val == 'U' or val == 'I':
                output[ind] = storeVowels.pop()

        op = op.join(output)
        return op