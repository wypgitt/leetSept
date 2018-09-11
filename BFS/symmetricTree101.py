# 101. Symmetric tree

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if left == right == None:
            return True
        if (left is None and right is not None) or (left is not None and right is None):
            return False
        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)   



    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        level = [root]
        while level:
            for i in range(len(level) // 2):
                if level[i] and level[~i]:
                    if level[i].val != level[~i].val: 
                        return False
                elif level[i] or level[~i]: 
                    return False
            new_level = []
            for node in level:
                if node: 
                    new_level.extend([node.left, node.right])
            level = new_level
        return True

