'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
Code By Saideep Shetty
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, node):
        if node is None:
            return 0
        else:
            return max(self.maxDepth(node.left), self.maxDepth(node.right)) + 1
        
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        if (abs(leftHeight - rightHeight) <= 1) and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True: 
            return True
   
        return False
