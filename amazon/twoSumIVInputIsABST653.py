# 653. Two Sum IV - Input is a BST

'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        dataset = set()
        return self.dfs(root, k, dataset)
    
    def dfs(self, root, k, dataset):
        if not root:
            return False
        else:
            if root.val in dataset:
                return True
            else:
                dataset.add(k - root.val)
        return self.dfs(root.left, k, dataset) or self.dfs(root.right, k, dataset)