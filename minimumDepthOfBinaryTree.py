'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
Code By Saideep Shetty
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        count = 0
        miniTree = []
        miniTree.append(root)
        
        while miniTree:
            treeLength = len(miniTree)
            for i in range(treeLength):
                firstNode = miniTree.pop(0)
                
                if firstNode.left is None and firstNode.right is None:
                    miniTree = []
                    break
                if firstNode.left is not(None):
                    miniTree.append(firstNode.left)
                if firstNode.right is not(None):
                    miniTree.append(firstNode.right)
                
            count += 1
        return count 

