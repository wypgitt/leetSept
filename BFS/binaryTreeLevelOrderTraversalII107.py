# 107. Binary Tree Level Order Traversal II

'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        stack = []
        ans = []
        
        level = 0
        
        stack = [[root]]
        
        while stack:
            level = stack.pop(0)
            ans.append([node.val for node in level])  
            next_l = []
            for node in level:
                if node.left:
                    next_l.append(node.left)
                if node.right:
                    next_l.append(node.right)
            if len(next_l) > 0:
                stack.append(next_l)
        return ans[::-1]