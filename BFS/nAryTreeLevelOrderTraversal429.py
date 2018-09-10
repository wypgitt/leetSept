# 429. N-ary Tree Level Order Traversal

'''
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

 


 
We should return its level order traversal:

 

 

[
     [1],
     [3,2,4],
     [5,6]
]
 

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.

'''



# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        stack = [root]
        
        if root is None:
            return []
        
        ans = []
        
        while stack:
            ans.append([node.val for node in stack])
            stack = [child for node in stack for child in node.children]
        return ans
    
