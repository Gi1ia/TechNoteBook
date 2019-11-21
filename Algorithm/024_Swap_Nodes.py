# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy.next, dummy

        while fast and fast.next:
            fast = fast.next # Find the second in pair
            slow.next.next = fast.next # Fist point to rest of linked list
            fast.next = slow.next
            slow.next = fast # Reconnect first part to the pair

            slow = slow.next.next
            fast = fast.next.next
        
        return dummy.next