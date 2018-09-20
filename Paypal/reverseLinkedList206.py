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

        '''
        return self.reverse(head)

    def reverse(self, head, pre = None):
        if not head:
            return pre
        node = head.next
        head.next = pre
        return self.reverse(node, head)
        '''

        '''
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre
        '''

        pre = None
        cur = head
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = pre
            pre = tmp
        return pre 
            
