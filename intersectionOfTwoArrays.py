'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        answer = []
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1:
                    answer.append(i)
        else:
            for i in nums1:
                if i in nums2:
                    answer.append(i)

        return(list(set(answer)))
        