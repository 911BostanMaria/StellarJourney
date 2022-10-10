from repo import Movement
from domain import  Board
from validator.validationexception import ValidationException
from validator.validator import Validator

class UI:
    def __init__(self, board):
        self._board = board
        self._game = Movement()
        self._valid = Validator

    def console(self):
        self._game.place_ten_stars(self._board.get_data())
        print(str(self._board))
        print("it's time to place the USS Endeavour.")
        try:
            init_row = (input("row > "))
            init_column = int(input("column > "))
            init_row = init_row.upper()
            self._valid.validate_user_input(init_row, init_column)
            self._game.place_USS_ship(self._board.get_data(), init_row, init_column)
        except ValueError as err:
            print(err)
        how_many_ships = 3
        self._game.place_cruisers(self._board.get_data(), how_many_ships)
        while True:
            if how_many_ships == 0:
                print("you won bestie! ♥ ")
                return
            print(str(self._board))
            print("warp <coordinate>")
            print("fire <coordinate")
            user_input = input("> ")
            if user_input == 'cheat':
                self._game.cheat_code(self._board.get_data())
                print(str(self._board))
                return
            try:
                token = user_input.split(" ", maxsplit=1)
                row = token[1][0]
                row = row.upper()
                column = int(token[1][1])
                self._valid.validate_user_input(row, column)
            except ValidationException as err:
                print(err)
            if token[0] == 'warp':
                alright = self._game.can_you_warp_move(self._board.get_data(), init_row, init_column, row, column)
                if alright == -1:
                    print("you landed on enemy ship. game over.")
                    return
                elif alright is True:
                    self._game.warp_move(self._board.get_data(), init_row,init_column, row, column)
                    init_row = row
                    init_column = column
                elif alright is False:
                    print("star is placed in your path.")
            elif token[0] == 'fire':
                alright = self._game.fire_command(self._board.get_data(), init_row, init_column, row, column)
                if alright == -1:
                    print('you hit enemy ship.')
                    how_many_ships = how_many_ships - 1
                    self._game.place_cruisers(self._board.get_data(), how_many_ships)
                elif alright is True:
                    print("you hit none.")
                elif alright is False:
                    print("invalid coordinates. try again.")

gameboard = Board(9,9)
ui = UI(gameboard)
ui.console()
