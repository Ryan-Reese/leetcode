from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        previous: Optional[ListNode] = None
        current: ListNode = head
        next: Optional[ListNode] = head.next

        while next is not None:
            current.next = previous
            previous = current
            current = next
            next = next.next
        current.next = previous

        return current
