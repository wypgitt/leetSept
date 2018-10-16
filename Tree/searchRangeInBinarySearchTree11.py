# 11. Search Range in Binary Search Tree
'''
Description
Given a binary search tree and a range [k1, k2], return all elements in the given range.

Have you met this question in a real interview?  
Example
If k1 = 10 and k2 = 22, then your function should return [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12
Related Problems
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        ans = []
        if root is None:
            return ans
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                if queue[index].val >= k1 and queue[index].val <= k2:
                    ans.append(queue[index].val)
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            
            index += 1 
        return sorted(ans)
