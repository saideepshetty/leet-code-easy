'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
Code By Saideep Shetty
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict
        d = defaultdict(int)

        for ind, val in enumerate(nums):
            if val in d:
                if ind - d[val] <= k:
                    return True
            d[val] = ind
        
        return False
