from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_subarray = nums[0]
        max_subarray = nums[0]

        i = 1
        while i < len(nums):
            if current_subarray < 0:
                current_subarray = 0
            current_subarray += nums[i]
            max_subarray = max(max_subarray, current_subarray)
            i += 1

        return max_subarray
