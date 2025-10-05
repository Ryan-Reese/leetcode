from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # break array apart
        arrays: list[list[int]] = [[n] for n in nums]

        # merge arrays back
        while len(arrays) != 1:
            n_arrays: int = len(arrays)
            merged_arrays: list[list[int]] = [arrays[-1]] if (n_arrays % 2) == 1 else []

            for i in range(0, n_arrays - 1, 2):
                merged_arrays.append(
                    self.mergeLists(
                        arrays[i],
                        arrays[i + 1],
                    ),
                )

            arrays = merged_arrays
        return arrays.pop()

    def mergeLists(self, arr1: list[int], arr2: list[int]) -> list[int]:
        # merging two (nonempty) sorted lists in-place
        idx1: int = 0
        idx2: int = 0
        len1: int = len(arr1)
        len2: int = len(arr2)

        while (idx1 < len1) and (idx2 < len2):
            if arr1[idx1] > arr2[idx2]:
                arr1.insert(idx1, arr2[idx2])
                len1 += 1
                idx2 += 1
            idx1 += 1
        if idx1 >= len1:
            arr1.extend(arr2[idx2:])
        return arr1
