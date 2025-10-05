from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(
        self,
        head: Optional[ListNode],
        nums: list[int],
    ) -> int:
        if head is None:
            return 0
        current: ListNode = head
        next: Optional[ListNode] = head.next
        n_components: int = int(current.val in nums)
        in_component: bool = bool(current.val in nums)

        while next is not None:
            if in_component:
                if next.val not in nums:
                    in_component = False
            else:
                if next.val in nums:
                    in_component = True
                    n_components += 1
            current = next
            next = next.next

        return n_components
