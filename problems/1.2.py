class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {nums[i] : i for i in range(len(nums))}
        for j in range(len(nums)):
            diff = target - nums[j]
            if (diff in hashmap) and (hashmap[diff] != j):
                return [j, hashmap[diff]]
