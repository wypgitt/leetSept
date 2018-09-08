#654. Maximum Binary Tree

'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        dummy = TreeNode(None)
        self.dfs(dummy, nums)
        return dummy
    def dfs(self, root, nums):
        if not nums:
            return
        i = nums.index(max(nums))
        root.val = nums[i]
        if nums[:i]:
            root.left = TreeNode(None)
            self.dfs(root.left, nums[:i])
        if nums[i+1:]:
            root.right = TreeNode(None)
            self.dfs(root.right, nums[i + 1:])
            