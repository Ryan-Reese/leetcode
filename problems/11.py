from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # init pointers (two pointer approach for O(n))
        left_idx, right_idx = 0, len(height) - 1
        # init heights
        left_height, right_height = height[left_idx], height[right_idx]
        # init area
        area = min(left_height, right_height) * (right_idx - left_idx)

        while left_idx < right_idx:
            if left_height < right_height:
                left_idx += 1
                if height[left_idx] > left_height:
                    left_height = height[left_idx]
                    area = max(
                        area, min(left_height, right_height) * (right_idx - left_idx)
                    )
            else:
                right_idx -= 1
                if height[right_idx] > right_height:
                    right_height = height[right_idx]
                    area = max(
                        area, min(left_height, right_height) * (right_idx - left_idx)
                    )

        return area
