# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        dummy = jump = ListNode(0)
        l = r = head
        dummy.next = head
        
        while True:
            count = 0
            while r and count < k:
                r = r.next 
                count += 1
            if count == k:
                # start reverse
                cur, pre = l, r
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                # connect two linked list together
                jump.next = pre
                jump = l
                l = r
            else:
                return dummy.next
        
        
    