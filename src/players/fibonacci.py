from bet import Bet
from players.player import Player
from table import Table
from outcome import Outcome


class PlayerFibonacci(Player):
    """
    :class:`PlayerFibonacci` uses the Fibonacci betting system. This player allocates their
    available budget into a sequence of bets that have an accelerating potential gain.

    .. attribute:: recent

       This is the most recent bet amount. Initially, this is 1.

    .. attribute:: previous

       This is the bet amount previous to the most recent bet amount. Initially, this is zero.
    """

    def __init__(self, table: Table) -> None:
        """
        Initialize the Fibonacci player.

        :param table: The :py:class:`~table.Table` object which will accept the bets.
        """

        super().__init__(table)
        self.outcome = Outcome("Black", 1)
        self.recent = 1
        self.previous = 0
        self.bet_amount = self.recent + self.previous

    def win(self, bet: Bet) -> None:
        """
        :param bet: :py:class:`~bet.Bet` The bet which won



        Uses the superclass method to update the stake with an amount won. It resets
        :class:`PlayerFibonacci.recent` and :class:`PlayerFibonacci.previous` to their initial
        values of 1 and 0.
        """

        super().win(bet)
        self.recent = 1
        self.previous = 0

    def lose(self, bet: Bet) -> None:
        """
        Uses the superclass method to update the stake with an amount lost.
        This will go “forwards” in the sequence. It updates :class:`PlayerFibonacci.recent`
        and :class:`PlayerFibonacci.previous` as follows.
                                                                next = recent + previous

                                                                previous = recent

                                                                recent = next

        :param bet: The py:class:`~bet.Bet` which lost.
        """

        self.bet_amount = self.recent + self.previous
        self.previous = self.recent
        self.recent = self.bet_amount

    def playing(self) -> bool:
        if not super().playing() or self.stake < self.bet_amount:
            self.recent = 1
            self.previous = 0
            self.bet_amount = self.recent + self.previous
            return False
        return True

    def placeBets(self) -> None:
        self.table.placeBet(Bet(self.bet_amount, self.outcome))
        self.stake -= self.bet_amount
