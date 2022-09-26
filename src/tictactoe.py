"""This module runs a game"""
from exceptions.custom_errors import CustomError
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
        """This method takes input and checks its validation"""

        if (len(input_value.split())) != 1:
            raise CustomError.InvalidArgsError

        if not is_number(input_value):
            raise CustomError.NotNumberError

        player_answer = int(input_value) - 1

        if player_answer not in range(9):
            raise CustomError.OutOfRangeError

        if str(self.board[player_answer]) in "XO":
            raise CustomError.OccupiedCellError

        return player_answer

    def start_game(self):
        """This method implements the game from to start to end"""

        message = ""
        counter = 0
        is_there_winner = False
        self.show_board()
        while not is_there_winner:
            player_number = counter % 2 + 1
            player_token = "X" if player_number == 1 else "O"
            print(f"\x1b[6;30;43mIt's turn of Player {player_number} ({player_token})."
                  f"\x1b[0m\n\x1b[6;30;43mEnter a number:\x1b[0m")

            try:
                self.board[self.validate_input(input())] = player_token
            except CustomError.InvalidArgsError:
                print("\x1b[6;30;41mIncorrect input! Invalid number of arguments.\x1b[0m")
                continue
            except CustomError.NotNumberError:
                print("\x1b[6;30;41mIncorrect input! It isn't a number.\x1b[0m")
                continue
            except CustomError.OccupiedCellError:
                print("\x1b[6;30;41mIncorrect input! This cell is occupied.\x1b[0m")
                continue
            except CustomError.OutOfRangeError:
                print("\x1b[6;30;41mIncorrect input! Enter a number in range from 1 to 9.\x1b[0m")
                continue

            counter += 1
            self.show_board()

            if counter > 4:
                winner = self.check_winner()
                if winner:
                    message = f"\x1b[6;30;42mPlayer {player_number} won!\x1b[0m"
                    is_there_winner = True
                elif counter == 9:
                    message = "\x1b[6;30;45mDraw!\x1b[0m"
                    is_there_winner = True

        print(message)

    def check_winner(self):
        """This method checks if there is any winner on board"""

        board = self.board
        win_coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                           (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

        for each in win_coordinates:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return True
        return False


if __name__ == '__main__':
    game = TicTacToeGame()
    game.start_game()
