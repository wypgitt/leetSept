# 111. Minimum Depth of Binary Tree

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
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [[root]]     
        ans = []
        res = 0
        while stack:
            level = stack.pop(0)
            res += 1
            new_level = []
            for node in level:
                if node.left == node.right==None:
                    ans.append(res)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if len(new_level)> 0:
                stack.append(new_level)
        return min(ans)