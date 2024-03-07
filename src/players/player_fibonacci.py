from bet import Bet
from players.player import Player
from table import Table
from outcome import Outcome


class PlayerFibonacci(Player):
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.outcome = Outcome("Black", 1)
        self.recent = 1
        self.previous = 0

    def win(self, bet: Bet) -> None:
        super().win(bet)
        self.recent = 1
        self.previous = 0
