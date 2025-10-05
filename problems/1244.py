class Leaderboard:

    def __init__(self):
        self.board = dict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.board:
            self.board[playerId] += score
        else:
            self.board[playerId] = score

    def top(self, K: int) -> int:
        sorted_board = sorted(self.board.values(), reverse=True)
        return sum(sorted_board[:K])

    def reset(self, playerId: int) -> None:
        del self.board[playerId]
