# 637. Average of Levels in Binary Tree
'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        queue = [root]
        while queue:
            ans.append(sum(map(lambda x: x.val, queue))/len(queue))
            queue = [kid for node in queue for kid in (node.left, node.right) if kid]
        return ans
        
        
        '''
        ans = []
        stack = [[root]]
        while stack:
            nodes = stack.pop()
            ans.append(sum(node.val for node in nodes)/len(nodes))
            next_l = []
            for node in nodes:
                if node.left:
                    next_l.append(node.left)
                if node.right:
                    next_l.append(node.right)
            if len(next_l):
                stack.append(next_l)
        return ans
        '''


