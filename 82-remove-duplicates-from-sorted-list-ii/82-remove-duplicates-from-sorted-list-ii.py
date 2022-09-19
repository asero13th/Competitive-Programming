# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode()
        node = tmp
        p1 = head
        p2 = head
        
        while p1:
            p2 = p1
            l = 0
            val = p1.val
            while p2.next and p2.val == p2.next.val:
                p2 = p2.next
                l += 1
            p1.next = p2.next
            if l == 0:
                node.next = ListNode(val)
                node = node.next
            p1 = p1.next          
        return tmp.next
                