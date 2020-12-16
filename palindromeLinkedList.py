'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
Code By Saideep Shetty
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return(True)
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        
        length = len(temp)
        for i in range(length/2):
            if temp[i] != temp[length-i-1]:
                return(False)
        return(True)
