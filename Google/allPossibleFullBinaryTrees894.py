# 894. All Possible Full Binary Trees
'''
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

 

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

 

Note:

1 <= N <= 20
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def allPossibleFBT(self, n):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        memo = {}
        if n == 0:
            return None
        if n == 1:
            return [TreeNode(0)]
        if n in memo:
            return memo[n]
        
        trees = []
        for i in range(1, n - 1):
            lefts, rights = self.allPossibleFBT(i), self.allPossibleFBT(n - i - 1)
            for left in lefts:
                for right in rights:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    trees.append(root)
        memo[n] = trees
        return trees
                
        
        
        
        
        
        
        
        
        

