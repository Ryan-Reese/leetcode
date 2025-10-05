from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if head is None:
            return None

        current: ListNode = head
        left_end: Optional[ListNode] = None
        middle_start: Optional[ListNode] = None

        # if starting in reverse range
        if left == 1:
            middle_start = current
        # not starting in reverse range
        else:
            for _ in range(left - 2):
                if current.next is not None:
                    current = current.next
            left_end = current
            if current.next is not None:
                current = current.next
                middle_start = current

        for _ in range(right - left):
            if current.next is not None:
                current = current.next

        # save middle end
        middle_end: ListNode = current

        # save right start
        right_start: Optional[ListNode] = None
        if current.next is not None:
            right_start = current.next

        # create gaps
        if left_end is not None:
            left_end.next = None
        middle_end.next = None

        # reverse middle
        new_middle: Optional[ListNode] = self.reverseList(middle_start)

        # rejoin list
        if left_end is not None:
            left_end.next = new_middle
        if middle_start is not None:
            middle_start.next = right_start

        if left == 1:
            return middle_end
        else:
            return head

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
