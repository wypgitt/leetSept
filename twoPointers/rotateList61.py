# 61. Rotate List
'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return None
        dummy = ListNode(None)
        dummy.next = head
        slow = fast = dummy
        
        n = 0
        while fast.next:
            fast = fast.next
            n += 1
        i = n - k%n
        while i > 0:
            slow = slow.next
            i -= 1
            
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        
        return dummy.next
        
        
        
        '''
        n, pre, current = 0, None, head
        while current:
            pre, current = current, current.next
            n += 1
        if not n or not k%n:
            return head
        tail = head
        for _ in range(n - k%n - 1):
            tail = tail.next
        nxt, tail.next, pre.next = tail.next, None, head
        return nxt
        
        '''
        
        
        

        
        
        
        
        

