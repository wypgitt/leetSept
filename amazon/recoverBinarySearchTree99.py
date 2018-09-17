# 99 Recover Binary Search Tree

'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.order = []
        self.prev = None
        self.inorder(root)
        if len(self.order) == 2:
            self.swap(self.order[0][0], self.order[1][1])
        else:
            self.swap(self.order[0][0], self.order[0][1])   
        return 

    def inorder(self, root):
        if root is None:
            return 
        self.inorder(root.left)
        if self.prev and self.prev.val > root.val:
            self.order.append((self.prev, root))
        self.prev = root
        self.inorder(root.right)
        return
        
    def swap(self, a, b):
        a.val, b.val = b.val, a.val
        return
        
