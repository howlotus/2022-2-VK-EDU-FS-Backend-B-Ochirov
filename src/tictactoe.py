class TicTacToeGame:
    """This class implements console game - TicTacToe"""

    def __init__(self):
        self.board = list(range(1, 10))

    def show_board(self):
        """This method prints board for TicTacToe"""
        board = self.board
        print("-------------")
        for i in range(3):
            print(f"| {board[i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |\n-------------")

    def validate_input(self, player_number, player_token):
        """This method takes input and checks its validation"""
        print(f"\x1b[6;30;43mIt's turn of Player {player_number} ({player_token})."
              f"\x1b[0m\n\x1b[6;30;43mEnter a number:\x1b[0m")
        is_answer_valid = False
        while not is_answer_valid:
            player_answer = input()
            try:
                player_answer = int(player_answer)
            except ValueError:
                print("\x1b[6;30;41mIncorrect input! It isn't a number.\x1b[0m")
                continue
            if player_answer in range(1, 10):
                if str(self.board[player_answer - 1]) not in "XO":
                    self.board[player_answer - 1] = player_token
                    is_answer_valid = True
                else:
                    print("\x1b[6;30;41mIncorrect input! This cell is occupied.\x1b[0m")
            else:
                print("\x1b[6;30;41mIncorrect input! Enter a number in range from 1 to 9.\x1b[0m")

    def start_game(self):
        """This method implements the game from to start to end"""
        message = ""
        counter = 0
        is_there_winner = False
        while not is_there_winner:
            self.show_board()
            tmp = counter % 2 + 1
            if tmp == 1:
                self.validate_input(tmp, "X")
            else:
                self.validate_input(tmp, "O")

            counter += 1

            if counter > 4:
                winner = self.check_winner()
                if winner:
                    message = f"\x1b[6;30;42mPlayer {tmp} won!\x1b[0m"
                    is_there_winner = True
                    continue

            if counter == 9:
                message = "\x1b[6;30;43mDraw!\x1b[0m"
                is_there_winner = True

        self.show_board()
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
