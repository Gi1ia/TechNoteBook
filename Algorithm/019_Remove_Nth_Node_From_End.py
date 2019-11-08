"""Remove n-th node from end of the list.
Return head node
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        slow = head
        fast = head

        for i in range(n):
            fast = fast.next
            
        if fast == None:
            # In this case, the node we need to delete is the first node.
            head = slow.next
        else:
            # find out the node we want to delete (slow.next)
            while fast.next != None:
                fast = fast.next
                slow = slow.next
            
            slow.next = slow.next.next

        return head
    
    def remove_Nth_From_End_With_Dummy(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        for i in range(n + 1):
            fast = fast.next

        while fast != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next