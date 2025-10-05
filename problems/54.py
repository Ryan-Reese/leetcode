class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # recursive approach
        x_len: int = len(matrix[0])
        y_len: int = len(matrix)
        x_pos: int = -1
        y_pos: int = 0

        output: list[int] = []

        # get outermost numbers
        # RIGHTWARDS
        while x_pos < x_len - 1:
            x_pos += 1
            output.append(matrix[y_pos][x_pos])
        # DOWNWARDS
        while y_pos < y_len - 1:
            y_pos += 1
            output.append(matrix[y_pos][x_pos])
        # LEFTWARDS
        if y_len >= 2:
            while x_pos > 0:
                x_pos -= 1
                output.append(matrix[y_pos][x_pos])
        # UPWARDS
        if x_len >= 2:
            while y_pos > 1:
                y_pos -= 1
                output.append(matrix[y_pos][x_pos])

        if (x_len > 2) and (y_len > 2):
            return output + self.spiralOrder(
                [
                    [matrix[y][x] for x in range(1, x_len - 1)]
                    for y in range(1, y_len - 1)
                ]
            )
        else:
            return output


if __name__ == "__main__":
    inputs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(inputs))
