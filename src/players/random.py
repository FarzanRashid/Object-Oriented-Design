import random
from bet import Bet
from players.player import Player


class PlayerRandom(Player):
    """
    :class:`PlayerRandom` is a :py:class:`~players.player.Player` who places bets in Roulette.
    This player makes random bets around the layout.

    .. attribute:: rng

       A Random Number Generator which will return the next random number.

       When writing unit tests, we will want to patch this with a mock object to return a known
       sequence of bets.
    """

    def __init__(self, table, wheel) -> None:
        """
        This uses the **super()** construct to invoke the superclass constructor using the Table
        class.

        :param table: table (Table) – The :py:class:`~table.Table` object which will
        accept the bets.
        :param wheel: wheel (wheel) - The :py:class:`~wheel.Wheel` object which will be used to
        populate :py:class:`~outcome.Outcome`s.
        """

        super().__init__(table)
        self.wheel = wheel
        self.rng = random.Random()
        bin_iterator = self.wheel.binIterator()
        self.all_OC = set(outcome for bin in bin_iterator for outcome in bin)

    def placeBets(self) -> None:
        self.table.placeBet(Bet(1, self.rng.choice(list(self.all_OC))))
