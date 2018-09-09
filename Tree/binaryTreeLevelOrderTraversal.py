# 102. Binary Tree Level Order Traversal

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        stack = [root]
        while stack:
            size = len(stack)
            level = []
            for _ in range(size):
                pop = stack.pop(0)
                level.append(pop.val)
                if pop.left is not None:
                    stack.append(pop.left)
                if pop.right is not None:
                    stack.append(pop.right)
            ans.append(level)
        return ans
# Iterative, BFS, Time Complexity: O(n^2), Space complexity: O(n)


    def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        stack = [root]
        
        while stack:
            level = []
            for l in stack:
                level.append(l.val)
            ans.append(level)
            
            stack2 = []
            for l in stack:
                if l.left is not None:
                    stack2.append(l.left)
                if l.right is not None:
                    stack2.append(l.right)
            stack = stack2
        return ans
        
        