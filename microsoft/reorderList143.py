# 143. Reorder List
'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        run = slow.next
        slow.next = None
        
        l1 = None
        while run:
            runN = run.next
            run.next = l1
            l1 = run
            run = runN
        l0 = head
        while l1:
            l0n = l0.next
            l1n = l1.next
            
            l0.next = l1
            l1.next = l0n
            
            l0 = l0n
            l1 = l1n

        
        
        
        
        


