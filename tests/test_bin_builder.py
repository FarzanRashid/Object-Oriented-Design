from unittest import TestCase
from unittest.mock import Mock, patch
from roulette import Outcome, Wheel, BinBuilder


class TestBinBuilder(TestCase):
    def setUp(self):
        self.bin_builder = BinBuilder()
        self.wheel = Wheel()

    def test_bins_are_filled_for_straight_bets(self):
        straight_bet_odds = 35
        straight_outcomes = {
            0: Outcome("0", straight_bet_odds),
            1: Outcome("1", straight_bet_odds),
            36: Outcome("36", straight_bet_odds),
            37: Outcome("00", straight_bet_odds)
            }

        self.bin_builder.build_bins_for_straight_bets(self.wheel)

        for bin_index in straight_outcomes:
            self.assertIn(straight_outcomes[bin_index], self.wheel.bins[bin_index])

    def test_bins_are_filled_for_horizontal_split_bets(self):
        split_bet_odds = 17
        horizontal_split_outcomes = {
            1: Outcome("1-2", split_bet_odds),
            2: Outcome("1-2", split_bet_odds),
            35: Outcome("35-36", split_bet_odds),
            36: Outcome("35-36", split_bet_odds)
        }

        self.bin_builder.build_bins_for_horizontal_split_bets(self.wheel)

        for bin_index in horizontal_split_outcomes:
            self.assertIn(horizontal_split_outcomes[bin_index], self.wheel.bins[bin_index])

    def test_bins_are_filled_for_vertical_split_bets(self):
        split_bet_odds = 17
        vertical_split_outcomes = {
            1: Outcome("1-4", split_bet_odds),
            4: Outcome("1-4", split_bet_odds),
            33: Outcome("33-36", split_bet_odds),
            36: Outcome("33-36", split_bet_odds)
        }

        self.bin_builder.build_bins_for_vertical_split_bets(self.wheel)

        for bin_index in vertical_split_outcomes:
            self.assertIn(vertical_split_outcomes[bin_index], self.wheel.bins[bin_index])

    def test_bins_are_filled_for_street_bets(self):
        street_bet_odds = 11
        street_outcomes = {
            1: Outcome("1-2-3", street_bet_odds),
            36: Outcome("34-35-36", street_bet_odds)
        }

        self.bin_builder.build_bins_for_street_bets(self.wheel)

        for bin_index in street_outcomes:
            self.assertIn(street_outcomes[bin_index], self.wheel.bins[bin_index])

    def test_bins_are_filled_for_corner_bets(self):
        corner_bet_odds = 8
        corner_outcomes = {
            1: [Outcome("1-2-4-5", corner_bet_odds)],
            4: [Outcome("1-2-4-5", corner_bet_odds), Outcome("4-5-7-8", corner_bet_odds)],
            5: [Outcome("1-2-4-5", corner_bet_odds), Outcome("4-5-7-8", corner_bet_odds),
                Outcome("2-3-5-6", corner_bet_odds), Outcome("5-6-8-9", corner_bet_odds)]
                }

        self.bin_builder.build_bins_for_corner_bets(self.wheel)

        for bin_index in corner_outcomes:
            for outcome in corner_outcomes[bin_index]:
                self.assertIn(outcome, self.wheel.bins[bin_index])

    def test_bins_are_filled_for_line_bets(self):
        line_bet_odds = 5
        line_outcomes = {
            1: [Outcome("1-2-3-4-5-6", line_bet_odds)],
            4: [Outcome("1-2-3-4-5-6", line_bet_odds), Outcome("4-5-6-7-8-9", line_bet_odds)]
        }

        self.bin_builder.build_bins_for_line_bets(self.wheel)

        for bin_index in line_outcomes:
            for outcome in line_outcomes[bin_index]:
                self.assertIn(outcome, self.wheel.bins[bin_index])

    def test_bins_are_filled_for_dozen_bets(self):
        dozen_bet_odds = 2
        dozen_bet_outcomes = {
            1: [Outcome("1-2-3-4-5-6-7-8-9-10-11-12", dozen_bet_odds)],
            17: [Outcome("13-14-15-16-17-18-19-20-21-22-23-24", dozen_bet_odds)],
            36: [Outcome("25-26-27-28-29-30-31-32-33-34-35-36", dozen_bet_odds)]
        }

        self.bin_builder.build_bins_for_dozen_bets(self.wheel)

        for bin_index in dozen_bet_outcomes:
            for outcome in dozen_bet_outcomes[bin_index]:
                self.assertIn(outcome, self.wheel.bins[bin_index])

    def test_bins_are_filled_for_column_bets(self):
        column_bet_odds = 2
        column_bet_outcomes = {
            1: [Outcome("-".join([str(_) for _ in range(1, 35, 3)]), column_bet_odds)],
            17: [Outcome("-".join([str(_) for _ in range(2, 36, 3)]), column_bet_odds)],
            36: [Outcome("-".join([str(_) for _ in range(3, 37, 3)]), column_bet_odds)]
        }

        self.bin_builder.build_bins_for_column_bets(self.wheel)

        for bin_index in column_bet_outcomes:
            for outcome in column_bet_outcomes[bin_index]:
                self.assertIn(outcome, self.wheel.bins[bin_index])

    def test_bins_are_filed_for_five_bet(self):
        five_bet_odds = 6
        five_bet_name = "00-0-1-2-3"
        five_bet_outcome = Outcome(five_bet_name, five_bet_odds)

        five_bet_bin_indexes = [0, 1, 2, 3, 37]

        self.bin_builder.build_bins_for_five_bet(self.wheel)

        for bin_index in five_bet_bin_indexes:
            self.assertIn(five_bet_outcome, self.wheel.bins[bin_index])

    def test_bins_are_filled_for_even_money_bets(self):
        even_money_bet_odds = 1

        red_bet_outcome = Outcome("Red", even_money_bet_odds)
        black_bet_outcome = Outcome("Black", even_money_bet_odds)
        low_bet_outcome = Outcome("Low", even_money_bet_odds)
        high_bet_outcome = Outcome("High", even_money_bet_odds)
        even_bet_outcome = Outcome("Even", even_money_bet_odds)
        odd_bet_outcome = Outcome("Odd", even_money_bet_odds)

        red_bet_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}

        even_bet_bin_indexes = {1, 17, 18, 36}

        self.bin_builder.build_bins_for_even_money_bets(self.wheel)

        for bin_index in even_bet_bin_indexes:
            if bin_index in red_bet_numbers:
                self.assertIn(red_bet_outcome, self.wheel.bins[bin_index])
            else:
                self.assertIn(black_bet_outcome, self.wheel.bins[bin_index])
            if bin_index < 19:
                self.assertIn(low_bet_outcome, self.wheel.bins[bin_index])
            else:
                self.assertIn(high_bet_outcome, self.wheel.bins[bin_index])
            if bin_index % 2 == 0:
                self.assertIn(even_bet_outcome, self.wheel.bins[bin_index])
            else:
                self.assertIn(odd_bet_outcome, self.wheel.bins[bin_index])

    def test_buildBins_invokes_helper_methods(self):
        helper_methods = {
            "roulette.BinBuilder.build_bins_for_straight_bets",
            "roulette.BinBuilder.build_bins_for_horizontal_split_bets",
            "roulette.BinBuilder.build_bins_for_vertical_split_bets",
            "roulette.BinBuilder.build_bins_for_street_bets",
            "roulette.BinBuilder.build_bins_for_corner_bets",
            "roulette.BinBuilder.build_bins_for_line_bets",
            "roulette.BinBuilder.build_bins_for_five_bet",
            "roulette.BinBuilder.build_bins_for_even_money_bets",
            "roulette.BinBuilder.build_bins_for_dozen_bets",
            "roulette.BinBuilder.build_bins_for_column_bets",

        }

        mock_helper_method = Mock(name="mock_methods")

        for method in helper_methods:
            with patch(method, new=mock_helper_method):
                self.bin_builder.buildBins(self.wheel)
                mock_helper_method.assert_called_with(self.wheel)
