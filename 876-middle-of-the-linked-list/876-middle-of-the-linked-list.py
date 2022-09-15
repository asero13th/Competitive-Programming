# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = node = head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        idx = (count // 2)

        node = head
        count = 0
        while node:
            if count == idx:
                return node
            else:
                node = node.next
                count += 1
        return None
        