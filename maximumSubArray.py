'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Code By Saideep Shetty
'''

class Solution(object):
    def maxSubArray(self, nums):
        max_so_far = -999999999999
        max_end = 0
                
        for i in range(0, len(nums)):
            max_end = max_end + nums[i]
            if max_so_far < max_end:
                max_so_far = max_end
            if max_end < 0:
                max_end = 0
        
        return (max_so_far)
