from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []
        for i in range(len(intervals) - 1):
            if intervals[i][1] < intervals[i + 1][0]:
                merged_intervals.append(intervals[i])
            else:
                intervals[i + 1][0] = intervals[i][0]
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
        merged_intervals.append(intervals[-1])
        return merged_intervals
