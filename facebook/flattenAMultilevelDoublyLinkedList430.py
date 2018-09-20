# 430. Flatten a Multilevel Doubly Linked List
'''
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
Explanation for the above example:

Given the following multilevel doubly linked list:



We should return the following flattened doubly linked list:


'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        #1.iterate through the old list. 
        #2.if a node has a child, and its next pointer isn't null, use a stack to put the current nodes next node on top, and revise the node's child property to None. change the current node to the node's child, iterate. 
        #3.if a node does not have a child, but is a child aka stack is non-empty and its next pointer is NULL, pop the stack and let it be the next node. the node's previous pointer will be the current node. 
        #4.else, move the current node along adn repeat 2-3. 
        #5. return the list. 
        cur, nodeStack = head, []
        if cur is None: return None
        while cur:
            if cur.child:
                if cur.next:
                    nodeStack.append(cur.next)
                cur.next = cur.child
                cur.child.prev = cur 
                cur.child = None
            if not cur.next and len(nodeStack):
                temp = nodeStack.pop()
                temp.prev = cur 
                cur.next = temp
            cur = cur.next 
        return head 
        
        '''
        if not head:
            return
        
        dummy = Node(0,None,head,None)     
        stack = []
        stack.append(head)
        prev = dummy
        
        while stack:
            root = stack.pop()

            root.prev = prev
            prev.next = root
            
            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root        
            
        
        dummy.next.prev = None
        return dummy.next
        '''
