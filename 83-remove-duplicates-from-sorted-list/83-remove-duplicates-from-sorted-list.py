# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p_1 = head
        while p_1:
            while p_1.next and p_1.val == p_1.next.val:
                p_1.next = p_1.next.next
            p_1 = p_1.next
        return head
        