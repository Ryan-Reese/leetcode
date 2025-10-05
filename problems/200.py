from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.n_islands = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if self.visited[i][j] == 1:
                    continue
                if grid[i][j] == "1":
                    self.n_islands += 1
                    self.explore(i, j)

        return self.n_islands

    def explore(self, i, j):
        self.visited[i][j] = 1
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = i + dir[0], j + dir[1]
            if (new_i < 0) or (new_i >= self.rows):
                continue
            if (new_j < 0) or (new_j >= self.cols):
                continue
            if self.visited[new_i][new_j] == 1:
                continue
            if self.grid[new_i][new_j] == "1":
                self.explore(new_i, new_j)
