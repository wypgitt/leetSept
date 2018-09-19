# 589. N-ary Tree Preorder Traversal
'''
Given an n-ary tree, return the preorder traversal of its nodes' values.

 
For example, given a 3-ary tree:



 
Return its preorder traversal as: [1,3,5,6,2,4].

 
Note: Recursive solution is trivial, could you do it iteratively?
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ans += [node.val]
                if node.children:                 
                    stack += [child for child in node.children[::-1]]
        return ans
        '''
        ans = []
        self.dfs(root, ans)
        return ans
    def dfs(self, node, ans):
        if node:
            ans.append(node.val)
            for child in node.children:
                self.dfs(child, ans)
        '''

