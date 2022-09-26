"""This module runs a game"""
from exceptions.custom_errors import InvalidArgsError, NotNumberError, \
    OutOfRangeError, OccupiedCellError
from functions.is_str_a_number import is_number


class TicTacToeGame:
    """This class implements a console game - TicTacToe"""

    def __init__(self):
        self.board = list(range(1, 10))

    def show_board(self):
        """This method prints board for TicTacToe"""

        board = self.board

        print("=============")
        for i in range(3):
            print(f"| {board[i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |")
        print("=============")

    def validate_input(self, input_value):
        """This method takes input and validates it"""

        if (len(input_value.split())) != 1:
            raise InvalidArgsError("\x1b[6;30;41mInvalidArgsError: "
                                   "Invalid number of arguments.\x1b[0m")

        if not is_number(input_value):
            raise NotNumberError("\x1b[6;30;41mNotNumberError: "
                                 "It isn't a number.\x1b[0m")

        player_answer = int(input_value) - 1

        if not -1 < player_answer < 9:
            raise OutOfRangeError("\x1b[6;30;41mOutOfRangeError: "
                                  "Enter a number in range from 1 to 9.\x1b[0m")

        if str(self.board[player_answer]) in "XO":
            raise OccupiedCellError("\x1b[6;30;41mOccupiedCellError: "
                                    "This cell is occupied.\x1b[0m")

        return player_answer

    def start_game(self):
        """This method implements the game from start to end"""

        message = ""
        counter = 0
        is_game_over = False

        self.show_board()

        while not is_game_over:
            player_number = counter % 2 + 1
            player_token = "X" if player_number == 1 else "O"

            input_str = input(f"\x1b[6;30;43mIt's turn of Player {player_number} ({player_token})."
                              f"\x1b[0m\n\x1b[6;30;43mEnter a number:\x1b[0m ")

            try:
                self.board[self.validate_input(input_str)] = player_token
            except InvalidArgsError as err:
                print(str(err))
                continue
            except NotNumberError as err:
                print(str(err))
                continue
            except OccupiedCellError as err:
                print(str(err))
                continue
            except OutOfRangeError as err:
                print(str(err))
                continue

            counter += 1
            self.show_board()

            if counter > 4:
                winner = self.check_winner()
                if winner:
                    message = f"\x1b[6;30;42mPlayer {player_number} won!\x1b[0m"
                    is_game_over = True
                elif counter == 9:
                    message = "\x1b[6;30;45mDraw!\x1b[0m"
                    is_game_over = True

        print(message)

    def check_winner(self):
        """This method checks if there is any winner on board"""

        board = self.board
        win_coords = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                      (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

        for each in win_coords:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return True
        return False


if __name__ == '__main__':
    game = TicTacToeGame()
    game.start_game()
