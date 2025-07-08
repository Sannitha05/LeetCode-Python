# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next

        mid_pos = cnt // 2
        current = head
        for _ in range(mid_pos):
            current = current.next

        return current
