from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals: list[int] = []
        if head is None:
            return False
        current: ListNode = head
        next: Optional[ListNode] = head.next

        while next is not None:
            vals.append(current.val)
            current = next
            next = next.next
        vals.append(current.val)

        print(vals)

        for i in range(len(vals)):
            if vals[i] != vals[-(i + 1)]:
                return False

        return True
