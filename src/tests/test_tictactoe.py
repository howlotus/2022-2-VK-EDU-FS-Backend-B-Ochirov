"""This module tests a game"""
import unittest
from tictactoe import TicTacToeGame
from exceptions.custom_errors import InvalidArgsError, NotNumberError, \
    OccupiedCellError, OutOfRangeError


class TestTicTacToeGame(unittest.TestCase):
    """This class implements unittests for TicTacToeGame"""

    def setUp(self) -> None:
        self.game = TicTacToeGame()

    def test_validate_input(self):
        """This test checks the right input"""

        self.assertEqual(self.game.validate_input("8"), 7)

    def test_exceptions(self):
        """This test checks wrong answers and raising exceptions"""

        self.assertRaises(InvalidArgsError, self.game.validate_input, "1 2")
        self.assertRaises(NotNumberError, self.game.validate_input, "dsfsc")
        self.game.board[0] = "X"
        self.assertRaises(OccupiedCellError, self.game.validate_input, "1")
        self.assertRaises(OutOfRangeError, self.game.validate_input, "10")

    def test_draw(self):
        """This test validates a situation, when all cells are occupied, but there is no a winner"""

        self.game.board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertEqual(self.game.check_winner(), False)

    def test_first_winner(self):
        """This test validates a situation, when first player wins"""

        self.game.board = ["X", "O", 3, 4, "X", 6, 7, "O", "X"]
        self.assertEqual(self.game.check_winner(), True)

    def test_second_winner(self):
        """This test validates a situation, when second player wins"""

        self.game.board = ["X", "X", "O", "X", "O", "O", "O", "X", 9]
        self.assertEqual(self.game.check_winner(), True)


if __name__ == "__main__":
    unittest.main()
