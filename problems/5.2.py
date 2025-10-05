class Solution(object):
    def longestPalindrome(self, s: str) -> str:

        # dynamic programming table
        dp: list[list[bool]] = [[False for _ in range(len(s))]
                                for _ in range(len(s))]

        min: int = 0
        max: int = 0

        # base cases
        for i in range(len(s)):
            # palindromes of length 1
            dp[i][i] = True
        for i in range(len(s)-1):
            # palindromes of length 2
            if (s[i] == s[i+1]):
                dp[i][i+1] = True
                min, max = i, i+1

        # iterating over palindromes of other lengths
        for diff in range(2, len(s)):
            for start in range(0, len(s)-diff):
                if dp[(start)+1][(start+diff)-1]:
                    if (s[start] == s[start+diff]):
                        dp[start][start+diff] = True
                        min, max = start, start+diff

        return s[min:(max+1)]


