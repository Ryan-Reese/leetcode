from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_idx, right_idx = 0, len(nums) - 1

        while left_idx <= right_idx:

            midpoint = (left_idx + right_idx) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                right_idx = midpoint - 1
            else:
                left_idx = midpoint + 1

        return -1
