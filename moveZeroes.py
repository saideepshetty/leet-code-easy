'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations
Code By Saideep Shetty
'''
class Solution:
    def moveZeroes(self, input):
        zero_pointer = 0
        for position, data in enumerate(input):
            if data != 0:
                input[position], input[zero_pointer] = input[zero_pointer], input[position]
                zero_pointer += 1
