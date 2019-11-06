# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        firstLoop = head
        secondLoop = head
        visited = {}
        
        while firstLoop:
            copyNode = Node(firstLoop.val, None, None)
            visited[firstLoop] = copyNode
            firstLoop = firstLoop.next
        
        while secondLoop:
            visited[secondLoop].next = visited.get(secondLoop.next)
            visited[secondLoop].random = visited.get(secondLoop.random)
            secondLoop = secondLoop.next
        
        return visited.get(head)

class PythonicSolution:
# @param head, a RandomListNode
# @return a RandomListNode
    def copyRandomList(self, head):
        # idea here is, default dict will generate entity with lambda
        dic = collections.defaultdict(lambda: RandomListNode(0))
        dic[None] = None
        n = head
        while n:
            dic[n].label = n.label
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]