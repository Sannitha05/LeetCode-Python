# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_set = set()
        currentA = headA
        while currentA:
            nodes_set.add(currentA)
            currentA = currentA.next
            currentB = headB
        while currentB:
            if currentB in nodes_set:
                return currentB  
            currentB = currentB.next
        return None  
        