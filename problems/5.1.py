class Solution(object):
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(start: int, subLen: int) -> bool:
            for i in range(int(subLen/2)):
                if not (s[start+i] == s[start+subLen-(i+1)]):
                    return False
            return True

        for subLen in range(len(s), 0, -1):
            for start in range(0, len(s)-subLen+1):
                if isPalindrome(start, subLen):
                    return s[start:(start+subLen)]

        return ""
