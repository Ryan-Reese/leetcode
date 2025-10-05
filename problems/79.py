from typing import Tuple, List


class Solution:

    def backtrack(self, curr_pos: Tuple[int, int], suffix: str):
        if suffix == "":
            return True
        if (curr_pos[0] < 0) or (curr_pos[0] >= self.ROWS):
            return False
        if (curr_pos[1] < 0) or (curr_pos[1] >= self.COLS):
            return False
        if self.visited[curr_pos[0]][curr_pos[1]] == 1:
            return False
        if self.board[curr_pos[0]][curr_pos[1]] == suffix[0]:
            self.visited[curr_pos[0]][curr_pos[1]] = 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if self.backtrack((curr_pos[0] + dx, curr_pos[1] + dy), suffix[1:]):
                    return True
            self.visited[curr_pos[0]][curr_pos[1]] = 0
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:

        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board
        self.visited = [[0 for i in range(self.COLS)] for j in range(self.ROWS)]

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.backtrack((i, j), word):
                    return True

        return False
