"""
Given a tree, with below Node class. Player will obtain nodes in the tree that have shorter
distance to their nodes compared to other's nodes.
After player 1 occupied a node, design a strategy for player 2.
"""
import collections

class Node():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Occupy_Nodes():
    def play(self, player1):
        """
        player1 type: Node
        return: tuple(Node, count)
        """
        left_count, right_count, parent_count = 0, 0, 0
        if player1.left:
            left_count = self.count_nodes(player1.left, player1)
        if player1.right:
            right_count = self.count_nodes(player1.right, player1)
        if player1.parent:
            parent_count = self.count_nodes(player1.parent, player1)

        res = None
        if left_count > right_count:
            res = (player1.left, left_count)
        else:
            res = (player1.right, right_count)
        
        if parent_count > res[1]:
            res = (player1.parent, parent_count)
    
        return res


    def count_nodes(self, candidate, player1):      
        count = 0
        queue = collections.deque()
        queue.append(candidate)
        have_seen = set()

        while queue:
            current = queue.popleft()
            for next_node in [current.left, current.right, current.parent]:
                if next_node and next_node != player1 and next_node not in have_seen:
                    count += 1
                    have_seen.add(next_node)
                    queue.append(next_node)
        
        return count



