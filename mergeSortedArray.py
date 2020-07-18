'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        n = len(nums2)
        for i in range(0,n):
            del nums1[-1]
        #nums1 = [i for i in nums1 if i is not 0]
        for i in nums2:
            nums1.append(i)
        nums1.sort(