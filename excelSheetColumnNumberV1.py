'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''
class Solution:
    def titleToNumber(self, s):
        input_data = list(s)
        input_data.reverse()
        alphabet = ['0']
        for i in range(0, 26):
            alphabet.append(chr(65+i))
        total = 0
        for index, letter in enumerate(input_data):
                if letter in alphabet:
                    total += (alphabet.index(letter) * (26 ** (index)))
        return total