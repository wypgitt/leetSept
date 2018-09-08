#236. Lowest Ancestor Of A Binary Tree
'''

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Iterate from root and to the left and to the right
    # to check all nodes in the tree to see if they are both
    # in the same branch and then check the lowest ancestor
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        while root:
            if root == p or root == q:
                return root
            
            if self.common(p, q):
                return p
            if self.common(q, p):
                return q
            if self.common(root.left, p) and self.common(root.left, q):
                root = root.left
            if self.common(root.right, p) and self.common(root.right, q):
                root = root.right
            else:
                return root
        

    def common(self, root, child):
        if not root:
            return False
        if root:
            if root == child:
                return True
            return self.common(root.left, child) or self.common(root.right, child)
        
        return False
    
    # Recursion
    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None
        if root == q or root == p:
            return root
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)
        
        if left and right:
            return root
        if left:
            return left
        if right:
            return right