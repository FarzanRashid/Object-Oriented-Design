from unittest import TestCase
from players.player1326.player1326_state import Player1326ThreeWins


class TestPlayer1326ThreeWins(TestCase):
    def setUp(self):
        self.player1326_three_wins = Player1326ThreeWins()

    def test_only_one_instance_is_created(self):
        instance_2 = Player1326ThreeWins()
        self.assertIs(self.player1326_three_wins, instance_2)

        instance_3 = Player1326ThreeWins()
        self.assertIs(self.player1326_three_wins, instance_3)
