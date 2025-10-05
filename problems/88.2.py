from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1: int = 0
        idx2: int = 0

        if n == 0:
            return

        del nums1[-n:]
        while (idx1 < m) and (idx2 < n):
            if nums1[idx1] > nums2[idx2]:
                nums1.insert(idx1, nums2[idx2])
                m += 1
                idx2 += 1
            idx1 += 1
        if idx1 >= m:
            nums1.extend(nums2[idx2:])
