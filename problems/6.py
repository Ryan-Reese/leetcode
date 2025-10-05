class Solution:
    def convert(self, s: str, numRows: int) -> str:

        final_rows = []
        i = 0
        while i < len(s):
            for j in range(0, numRows, 1):
                final_rows.append(j)
                i += 1
            for j in range(numRows - 2, 0, -1):
                final_rows.append(j)
                i += 1

        answer = ""

        for row in range(numRows):
            for i in range(len(s)):
                if final_rows[i] == row:
                    answer += s[i]

        return answer
