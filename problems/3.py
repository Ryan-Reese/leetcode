class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLen: int = 0
        subLen: int = 0
        i: int = 0

        while (i < len(s)):
            if s[i] not in s[(i-subLen):i]:
                subLen += 1
                maxLen = max(maxLen, subLen)
                i += 1
            else:
                subLen -= 1

        return maxLen
