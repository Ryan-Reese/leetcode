from typing import List
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        

        n_players: int = len(skills)

        if n_players == 1:
            return 0
        if k >= (n_players - 1):
            return skills.index(max(skills))

        # otherwise simulate
        player_order: list[int] = [n for n in range(n_players)]
        winning_player: int = int(skills[1] > skills[0])
        n_wins: int = 1
        losing_player: int = player_order.pop(abs(winning_player - 1))
        player_order.append(losing_player)

        while n_wins < k:
            player1: int = player_order[0]
            player2: int = player_order[1]
            match_winner: int = player1 if skills[player1] > skills[player2] else player2

            if match_winner == winning_player:
                n_wins += 1
            else:
                winning_player = match_winner
                n_wins = 1
            losing_player = player_order.pop(








        if 
        

        pass
        
