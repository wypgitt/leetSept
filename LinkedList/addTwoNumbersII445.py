# 445. Add Two Numbers II

'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None or l2 is None:
            return l1 if l1 else l2
        
        num1 = self.helper(l1)
        num2 = self.helper(l2)
        newNum = num1 + num2
        
        newHead = temp = ListNode(0)
        for ch in str(newNum):
            temp.next = ListNode(int(ch))
            temp = temp.next
        return newHead.next
        
    
    def helper(self, head):
        num, copy = 0, head
        while copy:
            num = num*10 + copy.val
            copy = copy.next
        return num
