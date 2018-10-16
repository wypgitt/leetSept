# 426. Convert Binary Search Tree to Sorted Doubly Linked List
'''
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:

 


 
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

 


 
Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

 


Seen this question in a real interview before?  

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.ans = []
        self.dfs(root)
        if not self.ans:
            return None
        for i in range(len(self.ans)):
            self.ans[0].left = self.ans[-1]
            self.ans[-1].right = self.ans[0]
            if 0 < i < len(self.ans):
                self.ans[i].left = self.ans[i - 1]
                self.ans[i - 1].right = self.ans[i]
                
        return self.ans[0]
        
        
    def dfs(self, root):
        if not root:
            return 
        self.dfs(root.left)
        self.ans.append(root)
        self.dfs(root.right)
