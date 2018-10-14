# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import collections
import heapq

class Solution:
    def mergeKLists_heap(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        dummy = ListNode(0)
        cursor = dummy
        heap = []
        
        for index, head_node in enumerate(lists):
            if not head_node:
                continue
            # item is (node.val, node row in lists, node.next) 
            # So that if two nodes have same value, we compare their index in lists.
            item = (head_node.val, index, head_node)
            heapq.heappush(heap, item)

        while heap:
            current = heapq.heappop(heap)
            if current and current[2].next:
                # item is (node.val, node row in lists, node.next)
                item = (current[2].next.val, current[1], current[2].next)
                heapq.heappush(heap, item)
            cursor.next = current[2]
            cursor = cursor.next
        
        return dummy.next
    
    def mergeKLists_divided_conquer(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return lists

        N = len(lists)
        interval = 1
        while interval < N:
            for i in range(0, N, interval * 2):
                lists[i] = self.merge_two(lists[i], lists[i + interval])

            interval *= 2
        
        return lists[0]

    def merge_two(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(0)
        cursor = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cursor.next = l1
                l1 = l1.next
                cursor = cursor.next
            else:
                cursor.next = l2
                l2 = l2.next
                cursor = cursor.next
        
        if l1:
            cursor.next = l1
        elif l2:
            cursor.next = l2

        return dummy.next

        