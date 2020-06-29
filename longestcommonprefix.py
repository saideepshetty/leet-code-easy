'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
class Solution(object):
    def longestCommonPrefix(self, input_array):
        op = ""
        if len(input_array) is 0:
            return("")
        compare_string = min(input_array, key = len)
        for i in range(len(compare_string)):
            if all([x.startswith(compare_string[:i + 1]) for x in input_array]):
                op = compare_string[:i+1]
            else:
                break

        return(op)