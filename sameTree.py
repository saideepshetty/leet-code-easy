'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
Code By Saideep Shetty
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depthFirstSearch(self, root1, root2):
        if root1 and root2 and root1.val == root2.val:
            return self.depthFirstSearch(root1.left, root2.left) and self.depthFirstSearch(root2.right, root2.right)
        elif not root1 and not root2:
            return True
        else:
            return False
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.depthFirstSearch(p, q)
