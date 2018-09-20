# 82. Remove Duplicates from Sorted List II
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head
        
        while cur:
            nxt = cur.next
            while nxt and nxt.next and nxt.val == nxt.next.val:
                nxt = nxt.next
            if nxt != cur.next:
                cur.next = nxt.next
            else:
                cur = cur.next
        return dummy_head.next
        
        
        
        
        

        
        

