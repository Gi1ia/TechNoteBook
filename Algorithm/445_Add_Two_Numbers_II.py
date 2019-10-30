# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2 
        if not l2: return l1

        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        head, v = ListNode(0), 0
        while stack1 or stack2:
            if stack1 and stack2:
                v = stack1.pop() + stack2.pop() + head.val
            else:
                num = max(stack1, stack2)
                v = num.pop() + head.val
            
            # create the linked list from end
            node = ListNode(v//10)
            head.val = v % 10
            node.next = head
            head = node # head is always left most node

        if head.val == 0:
            head = head.next
        
        return head
