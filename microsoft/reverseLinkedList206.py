# 206. Reverse Linked List
'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        pre = None
        while head:
            curr = head
            head = head.next
            curr.next = pre
            pre = curr
        return pre



# recursive:
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head)
        
    def reverse(self, node, prev = None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.reverse(n, node)
