import random
from dataclasses import dataclass


@dataclass(frozen=True)
class Outcome:
    """
     :class:`Outcome` contains a single outcome on which a bet can be placed.

     In Roulette, each spin of the wheel has a number of :class:`Outcome` objects with bets that will be paid off. For
     example, the “1” bin has the following winning :class:`Outcome` instances: “1”, “Red”, “Odd”, “Low”, “Column 1”,
     “Dozen 1-12”, “Split 1-2”, “Split 1-4”, “Street 1-2-3”, “Corner 1-2-4-5”, “Five Bet”, “Line 1-2-3-4-5-6”,
     “00-0-1-2-3”, “Dozen 1”, “Low” and “Column 1”.

     All of thee above-named bets will pay off if the wheel spins a “1”. This makes a Wheel and a Bin fairly
     complex containers of :class:`Outcome` objects.

     ..  attribute:: name

         Holds the name of the Outcome. Examples include "1", "Red".

     .. attribute:: odds

         Holds the payout odds for this Outcome. Most odds are stated as 1:1 or 17:1, we only keep the numerator (17)
         and assume the denominator is 1.

     """

    name: str
    odds: int

    def __str__(self) -> str:
        """
        Easy-to-read representation of outcome instances.

        :return: String of the form *name (odds*:1).
        :rtype: str
        """
        return f"{self.name:s} ({self.odds:d}:1)"

    def winAmount(self, amount: float) -> float:
        """
        Multiply this :class:`Outcome`'s odds by the given amount. The product is returned.

        :param amount: amount being bet
        :type amount: float
        """
        return self.odds * amount


class Bin(frozenset):
    """
    :class:`Bin` contains a collection of :class:`Outcome` instances which reflect the winning bets that are paid for a
    particular bin on a Roulette wheel. In Roulette, each spin of the wheel has a number of :class:`Outcome` instances.
    Example: A spin of 1, selects the “1” bin with the following winning :class:`Outcome` instances: “1” , “Red”,
    “Odd”,“Low” , “Column 1” , “Dozen 1-12” , “Split 1-2” , “Split 1-4” , “Street 1-2-3” , “Corner 1-2-4-5”, “Five Bet”,
    “Line 1-2-3-4-5-6” , “00-0-1-2-3” , “Dozen 1”, “Low” and “Column 1”. These are collected into a single :class:`Bin`.
    """
    pass


class Wheel:
    def __init__(self) -> None:
        self.bins = tuple(Bin() for i in range(38))
        self.rng = random.Random()

    def addOutcome(self, number: int, outcome: Outcome) -> None:
        updated_bin = Bin(list(self.bins[number].union(Bin([outcome]))))
        self.bins = self.bins[:number] + (updated_bin,) + self.bins[number + 1:]

    def choose(self) -> Bin:
        return random.choice(self.bins)
