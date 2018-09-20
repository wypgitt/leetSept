# 25. Reverse Nodes in k-Group
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or k == 1:
            return head
        root = ListNode(None)
        root.next = head
        idx = 0
        pre, cur, nxt = root, head, None
        while cur:
            if idx == k - 1:
                idx = 0
                nxt = cur.next
                cur.next = None
                pre.next, end = self.reverse(pre.next)
                end.next = nxt
                
                pre = end
                cur = end.next
            else:
                cur = cur.next
                idx += 1
                
        return root.next

        
    def reverse(self, head):
        end = head
        pre = None
        cur = head
        nxt = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre, end
        

        

        '''
        l, node = 0, head
        while node:
            l += 1
            node = node.next
        if k <= 1 or l < k:
            return head
        node, cur = None, head
        for _ in range(k):
            nxt = cur.next
            cur.next = node
            node = cur 
            cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return node
        '''
