from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = 0, 0

        for i in range(m + n):
            if ptr2 >= n:  # all nums2 has been appended to nums1
                return
            if (i - ptr2) == m:  # end of num1 has been reached
                nums1.insert(ptr1, nums2[ptr2])
                nums1.pop()
                ptr1 += 1
                ptr2 += 1
            else:
                if nums1[ptr1] <= nums2[ptr2]:
                    ptr1 += 1
                else:
                    nums1.insert(ptr1, nums2[ptr2])
                    nums1.pop()
                    ptr1 += 1
                    ptr2 += 1
