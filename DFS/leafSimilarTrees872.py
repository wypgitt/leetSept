# 872. Leaf-Similar Trees

'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def dfs(root):
            if not root:
                return []
            
            if root.left is None and root.right is None:
                return [root.val]
            return dfs(root.left) + dfs(root.right)
        return dfs(root1) == dfs(root2)


    def leafSimilar2(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def bfs(root):
            visited = [root]
            ans = []
            while visited:
                node = visited.pop()
                if node.left:
                    visited.append(node.left)
                if node.right:
                    visited.append(node.right)
                if not node.left and not node.right:
                    ans.insert(0, node.val)
            return ans
        return bfs(root1) == bfs(root2)
                    