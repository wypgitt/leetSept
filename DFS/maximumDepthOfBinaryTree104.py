# 104. Maximum Depth of Binary Tree
'''

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    depth = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.helper(root, 1)
        return self.depth

    def helper(self, node, curDepth):
        if not node:
            return 
        if curDepth > self.depth:
            self.depth = curDepth
        self.helper(node.left, curDepth + 1)
        self.helper(node.right, curDepth + 1)
        
        
        

        #return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0