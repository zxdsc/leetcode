"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        p = head
        nodeMap = {}
        while p:
            nodeMap[p] = Node(p.val, None, None)
            p = p.next
        
        res = Node(0, None, None)
        res.next = nodeMap[head]
        resPointer = res.next
        p = head
        while p:
            resPointer.next = nodeMap[p.next] if p.next else None
            resPointer.random = nodeMap[p.random] if p.random else None
            resPointer = resPointer.next
            p = p.next
        
        return res.next