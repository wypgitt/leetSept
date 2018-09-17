#109. Convert Sorted List to Binary Search Tree

'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        temp = slow.next
        slow.next = None
        node = TreeNode(temp.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(temp.next)
        return node
        
        
        
    
        '''
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        return self.convert([head], 0, l-1)
    
    def convert(self, head, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(head, start, mid-1)
        root = TreeNode(head[0].val)
        root.left = l
        head[0] = head[0].next 
        root.right = self.convert(head, mid+1, end)
        return root
        '''
