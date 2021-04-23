'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Code By Saideep Shetty
'''
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        splitString = str.split()
        setString = set(splitString)
        setPattern = set(pattern)

        if len(pattern) != len(splitString):
            return False
        elif len(setString) != len(setPattern):
            return False
        else:
            from collections import defaultdict
            d = defaultdict(list)
            for index, value in enumerate(pattern):
                d[value].append(splitString[index])

            for i in d:
                if len(set(d[i])) > 1:
                    return False
                else:
                    return True
