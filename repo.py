import random
from domain import Board


class Movement:
    def place_ten_stars(self, board):
        """
        :param board: The game board for stellar journey.
        :return: Returns none. It places ten stars on the game board in a way in such no two stars overlap or
        ar adjacent on row, column or diagonal. Stars are placed randomly if they are valid.
        """
        placed = 0
        while placed < 10:
            i = random.randint(1, 8)
            j = random.randint(1, 8)
            if 1 < i < 8 and 1 < j < 8:
                if board[i][j] == 0 and board[i - 1][j] == 0 and board[i + 1][j] == 0 and \
                        board[i][j - 1] == 0 and board[i][j + 1] == 0 and board[i - 1][j - 1] == 0 and \
                        board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == 0 and board[i + 1][j + 1] == 0:
                    board[i][j] = 1
                    placed = placed + 1

            elif i == 1 and 1 < j < 8:
                if board[i][j] == 0 and board[i+1][j] == 0 and board[i][j - 1] == 0 and board[i][j + 1] == 0 and \
                        board[i + 1][j - 1] == 0 and board[i + 1][j + 1] == 0:
                    board[i][j] = 1
                    placed = placed + 1

            elif i == 8 and 1 < j < 8:
                if board[i][j] == 0 and board[i][j - 1] == 0 and board[i][j + 1] == 0 and \
                        board[i - 1][j - 1] == 0 and board[i - 1][j + 1] == 0:
                    board[i][j] = 1
                    placed = placed + 1

            elif j == 1 and 1 < i < 8:
                if board[i][j] == 0 and board[i - 1][j] == 0 and board[i + 1][j] == 0 and \
                        board[i][j + 1] == 0 and board[i - 1][j + 1] == 0 and board[i + 1][j + 1] == 0:
                    board[i][j] = 1
                    placed = placed + 1

            elif j == 8 and 1 < i < 8:
                if board[i][j] == 0 and board[i - 1][j] == 0 and board[i + 1][j] == 0 and \
                        board[i][j - 1] == 0 and board[i - 1][j - 1] == 0 and board[i + 1][j - 1] == 0:
                    board[i][j] = 1
                    placed = placed + 1

    def place_USS_ship(self, board, row, column):
        """
        :param board: The game board for stellar journey.
        :param row: User input, integer, for row placement of the Endeavour.
        :param column: User input, character, for column placement of the Endeavour.
        :return:
        """
        char = ord(str(row)) - 16
        # Converts (A-H) to (1-8) in ascii codes.
        row = int(chr(char))
        if board[row][column] == 0:
            board[row][column] = 2

    def refresh_board(self, board):
        for i in range(1,8):
            for j in range(1,8):
                if board[i][j] == 3 or board[i][j] == 4:
                    board[i][j] = 0

    def place_cruisers(self,board, how_many):
        """
        :param board: The game board for stellar journey.
        :param how_many: Number of cruisers to be placed.
        :return: None. Places three cruisers on the game board such that no cruisers overlap with stars or the
        ship, and only cruisers adjacent to the Endeavour are shown.
        """
        self.refresh_board(board)
        placed = 0
        while placed < how_many :
            i = random.randint(1, 8)
            j = random.randint(1, 8)
            if board[i][j] == 0:
                if 1 < i < 8 and 1 < j < 8:
                    if board[i - 1][j] == 2 or board[i + 1][j] == 2 or \
                            board[i][j - 1] == 2 or board[i][j + 1] == 2 or board[i - 1][j - 1] == 2 or \
                            board[i - 1][j + 1] == 2 or board[i + 1][j - 1] == 2 or board[i + 1][j + 1] == 2:
                        board[i][j] = 4  # grid is marked as B since it is adjacent to the Endeavour
                    else:
                        board[i][j] = 3  # grid is marked as empty since it is not adjacent to the Endeavour
                    placed = placed + 1

                elif i == 1 and 1 < j < 8:
                    if board[i + 1][j] == 2 or board[i][j - 1] == 2 or board[i][j + 1] == 2 or \
                            board[i + 1][j - 1] == 2 or board[i + 1][j + 1] == 2:
                        board[i][j] = 4  # grid is marked as B since it is adjacent to the Endeavour
                    else:
                        board[i][j] = 3  # grid is marked as empty since it is not adjacent to the Endeavour
                    placed = placed + 1

                elif i == 8 and 1 < j < 8:
                    if board[i][j - 1] == 2 or board[i][j + 1] == 2 or \
                            board[i - 1][j - 1] == 2 or board[i - 1][j + 1] == 2:
                        board[i][j] = 4  # grid is marked as B since it is adjacent to the Endeavour
                    else:
                        board[i][j] = 3  # grid is marked as empty since it is not adjacent to the Endeavour
                    placed = placed + 1

                elif j == 1 and 1 < i < 8:
                    if board[i - 1][j] == 2 or board[i + 1][j] == 2 or \
                            board[i][j + 1] == 2 or  board[i - 1][j + 1] == 2 or board[i + 1][j + 1] == 2:
                        board[i][j] = 4  # grid is marked as B since it is adjacent to the Endeavour
                    else:
                        board[i][j] = 3  # grid is marked as empty since it is not adjacent to the Endeavour
                    placed = placed + 1

                elif j == 8 and 1 < i < 8:
                    if board[i - 1][j] == 2 or board[i + 1][j] == 2 or \
                            board[i][j - 1] == 2 or board[i - 1][j - 1] == 2 or board[i + 1][j - 1] == 2:
                        board[i][j] = 4  # grid is marked as B since it is adjacent to the Endeavour
                    else:
                        board[i][j] = 3  # grid is marked as empty since it is not adjacent to the Endeavour
                    placed = placed + 1

    def cheat_code(self, board):
        """
        :param board: The game board for stellar journey.
        :return: None. If cheat code is entered, cruisers are revealed ( 3 -> 4 according to the dictionary )
        """
        for i in range(1, 9):
            for j in range(1, 9):
                if board[i][j] == 3:
                    board[i][j] = 4

    def can_you_warp_move(self, board, init_row, init_column, row, column):
        """
        :param board: The game board for stellar journey.
        :param init_row: The initial row placement of the Endeavour.
        :param init_column: The initial column placement of the Endeavour.
        :param row: Row where the user wants to place the endeavour.
        :param column: Column where the user wants to place the endeavour.
        :return: Checks if there is a star in the way of the movement. If there is one, returns False, else
        returns True. Returns -1 in case of game over.
        """
        char = ord(str(row)) - 16
        # Converts (A-H) to (1-8) in ascii codes.
        row = int(chr(char))
        char = ord(str(init_row)) - 16
        # Converts (A-H) to (1-8) in ascii codes.
        init_row = int(chr(char))
        star = True
        if board[row][column] == 3 or board[row][column] == 4:
            return -1  # game over scenario, player landed on enemy ship.
        elif board[row][column] == 0:
            if init_row == row:  # check if there's a star on the row.
                for i in range(init_column, column):
                    if board[init_row][i] == 1:
                        star = False
            elif init_column == column:  # check if there's a star on the column.
                for i in range(init_row, row):
                    if board[i][column] == 1:
                        star = False
            else:  # checking all diagonals of the chosen grid
                l = row
                k = column
                while k >= 1:
                    if board[l][k] == 1:
                        star = False
                    k = k - 1
                    l = l - 1
                l = row
                k = column
                while k >= 1:
                    if board[l][k] == 1:
                        star = False
                    k = k + 1
                    l = l - 1
                while k <= 8:
                    if board[l][k] == 1:
                        star = False
                    k = k + 1
                    l = l + 1
            return star

    def warp_move(self,board, init_row, init_column, row, column):
        #actual warp move
        char = ord(str(row)) - 16
        row = int(chr(char))
        char = ord(str(init_row)) - 16
        init_row = int(chr(char))
        board[init_row][init_column] = 0
        board[row][column] = 2

    def fire_command(self, board, init_row, init_column, row, column):
        char = ord(str(row)) - 16
        # Converts (A-H) to (1-8) in ascii codes.
        row = int(chr(char))
        char = ord(str(init_row)) - 16
        # Converts (A-H) to (1-8) in ascii codes.
        init_row = int(chr(char))
        alright = False
        if init_row == row and init_column != column:
            # checks if fire move is done on the same row
            alright = True
        elif init_column == column and init_row != row:
            # checks if the fire move is done on the same column
            alright = True
        else:
            # checks if the fire move is done on the same diagonals
            l = init_row
            k = init_column
            while k >= 1:
                k = k - 1
                l = l - 1
                if k == column and l == row:
                    alright = True
            l = init_row
            k = init_column
            while k >= 1:
                k = k - 1
                l = l - 1
                if k == column and l == row:
                    alright = True
            l = init_row
            k = init_column
            while k <= 8:
                k = k + 1
                l = l + 1
                if k == column and l == row:
                    alright = True
            l = init_row
            k = init_column
            while k <= 8:
                k = k + 1
                l = l - 1
                if k == column and l == row:
                    alright = True
        if alright is True and board[row][column] == 3 or board[row][column] == 4:
            return -1
        return alright
