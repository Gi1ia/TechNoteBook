# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        first = head
        last = head

        while last != None:
            next_node = last.next
            if next_node is None:
                break
            
            last.next = next_node.next
            next_node.next = first
            first = next_node

        return first

    
    def reverseList_iterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
            
        # This will be the Null pointer that the last node point to
        # The last point after reversed is the head
        newNext = None
        
        while head:
            temp = head.next
            head.next = newNext
            newNext = head
            head = temp
        
        return newNext
        