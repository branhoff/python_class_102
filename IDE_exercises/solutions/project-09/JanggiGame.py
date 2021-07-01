import copy

class JanggiGame:
    """
    The JanggiGame class initializes all data members, facilitates the rules of the game, facilitates moving the
    pieces on the board, and manages the possible movements for each piece on the board.
    """

    def __init__(self):
        """
        Initializes all data members
        """
        self._game_state = "UNFINISHED"
        self._turn_count = 0

        self._curr_pos_index = []
        self._new_pos_index = []
        self._poss_moves_index = []
        self._taken_pieces = ["--"]

        self._board_key = [
            ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1"],
            ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2"],
            ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3"],
            ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4"],
            ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "i5"],
            ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "i6"],
            ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "i7"],
            ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "i8"],
            ["a9", "b9", "c9", "d9", "e9", "f9", "g9", "h9", "i9"],
            ["a10", "b10", "c10", "d10", "e10", "f10", "g10", "h10", "i10"],
        ]

        # r = red, b = blue
        # c = chariot, e = elephant, h = horse, g = guard, s = soldier
        # G = General, C = Cannon
        self._filled_board = [
            ["rc", "re", "rh", "rg", "--", "rg", "re", "rh", "rc"],
            ["--", "--", "--", "--", "rG", "--", "--", "--", "--"],
            ["--", "rC", "--", "--", "--", "--", "--", "rC", "--"],
            ["rs", "--", "rs", "--", "rs", "--", "rs", "--", "rs"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["bs", "--", "bs", "--", "bs", "--", "bs", "--", "bs"],
            ["--", "bC", "--", "--", "--", "--", "--", "bC", "--"],
            ["--", "--", "--", "--", "bG", "--", "--", "--", "--"],
            ["bc", "be", "bh", "bg", "--", "bg", "be", "bh", "bc"]
        ]

    def board_translator(self):
        pass

    def check_range(self, row, col):
        """
        Checks if given space is on the board
        """
        if (row < 0 or row > 9) or (col < 0 or col > 8):
            return False
        return True

    def get_board_key(self):
        """
        Prints out the board key
        """
        print("This is the board key")
        for x in self._board_key:
            for i in range(0, 9):
                print(x[i], end = " ")
            print()

    def get_board(self):
        """
        Prints out the board with pieces
        """
        print("This is the Janggi board:")
        for x in self._filled_board:
            for i in range(0, 9):
                print(x[i], end = "  ")
            print()

    def get_game_state(self):
        """
        Returns the current game state
        """
        return self._game_state

    def set_game_state(self):
        """
        Sets game state to decide winner
        """
        if self.get_active_player() == "b":
            self._game_state = "RED_WON"
        else:
            self._game_state = "BLUE_WON"

    def get_active_player(self):
        """
        Returns the player whose turn it is
        """
        if self._turn_count % 2 == 0:
            return "b"
        else:
            return "r"

    def get_opponent(self):
        """
        Returns the opponent to the player
        """
        if self.get_active_player() == "b":
            return "r"
        else:
            return "b"

    def get_piece(self, row, col):
        """
        Returns the piece at the given space
        """
        return self._filled_board[row][col]



    def make_move(self, curr_pos, new_pos):
        """
        Function for moving the pieces on the board
        """
        curr_pos_piece = None
        new_pos_piece = None

        # if the player wants to pass their turn
        if curr_pos == new_pos:
            print(self.get_active_player() + " has passed their turn")
            self._turn_count += 1
            return True

        else:
            # gets piece and index from curr_pos
            i = int(curr_pos[1:]) - 1
            j = 0
            for j in range(0, 9):
                if self._board_key[i][j] == curr_pos:
                    curr_pos_piece = self._filled_board[i][j]
                    self._curr_pos_index = [i, j]
                    break

            # gets the piece and index for the new_pos
            x = int(new_pos[1:]) - 1
            y = 0
            for y in range(0, 9):
                if self._board_key[x][y] == new_pos:
                    new_pos_piece = self._filled_board[x][y]
                    self._new_pos_index = [x, y]
                    break

            # if the player tries to move a piece from a space without a piece
            if self.get_piece(i, j) != curr_pos_piece:
                print("ERROR! Active player does not have a piece on this space")
                return False

            # if the player tries to place a piece on top of another piece
            # COME BACK TO THIS for TAKING PIECES
            if new_pos_piece != "--" and new_pos_piece[0] == self.get_opponent():
                print("ERROR! Cannot place a piece on top of another piece")
                return False

            # gets all possible moves for the piece
            self.get_all_moves(curr_pos_piece[1])

            # if the move is valid (one of the possible moves)
            if (self._new_pos_index[0], self._new_pos_index[1]) in self._poss_moves_index:

                # makes a copy of the board before the move
                copied_board = copy.deepcopy(self._filled_board)

                # makes the move
                self._filled_board[i][j] = "--"
                self._filled_board[x][y] = curr_pos_piece

                self._turn_count += 1

                return True
            else:
                print("ERROR! Move entered is invalid. Try again")
            return False

    def get_all_moves(self, piece_indicator):
        """
        Returns all possible moves for each indicated piece
        """
        # resetting these lists
        self._poss_moves_index = []
        self._taken_pieces = ["--"]

        if piece_indicator == "s":
            self.soldier_moves()
            return self._poss_moves_index
        elif piece_indicator == "h":
            self.horse_moves()
            return self._poss_moves_index
        elif piece_indicator == "e":
            self.elephant_moves()
            return self._poss_moves_index
        if piece_indicator == "c":
            self.chariot_moves()
            return self._poss_moves_index
        if piece_indicator == "g":
            self.guard_moves()
            return self._poss_moves_index
        if piece_indicator == "C":
            self.cannon_moves()
            return self._poss_moves_index
        if piece_indicator == "G":
            self.general_moves()
            return self._poss_moves_index

    def save_moves(self, poss_directions):
        """
        Saves all possible moves for each piece's indiv move functions.
        Also saves captured pieces.
        """
        row = self._curr_pos_index[0]           # first value represents row
        col = self._curr_pos_index[1]           # second value represents column

        for (x, y) in poss_directions:
            if self.check_range(row + x, col + y):
                space_occupant = self.get_piece(row + x, col + y)

                # if taking a piece
                if space_occupant != "--":
                    # adds piece to taken_pieces list and adds the move to list of poss moves
                    if space_occupant[0] == self.get_opponent():
                        self._taken_pieces.append(space_occupant)
                        move = (row + x, col + y)
                        self._poss_moves_index.append(move)

                # if moving without taking a piece
                else:
                    # just adds the move to the list of poss moves
                    move = (row + x, col + y)
                    self._poss_moves_index.append(move)

    # PIECES FORMULA
    # eval all possible directions
    # add more if piece in the palace
    # HORSES, ELEPHANTS: eval all possible movement paths (in case a piece blocks the move)
    # HORSES, ELEPHANTS: if piece blocks move, remove/adjust the possible directions
    # add all possible moves to poss_moves_index

    def soldier_moves(self):
        """
        Returns all possible moves for Soldier pieces
        """
        row = self._curr_pos_index[0]          # first value represents row
        col = self._curr_pos_index[1]          # second value represents column

        if self.get_active_player() == "b":
            poss_directions = [(0, -1), (-1, 0), (0, 1)]         # LEFT, UP, RIGHT
        else:
            poss_directions = [(0, -1), (1, 0), (0, 1)]          # RIGHT, UP, LEFT (POV RED)

        # more possibilities if in palace (can move diagonally)
        diag_positions = [(0, 3), (2, 3), (7, 3), (9, 3), (1, 4), (8, 4), (0, 5), (2, 5), (7, 5), (9, 5)]
        poss_diag_directions = []
        if (row, col) in diag_positions:
            if self.get_active_player() == "b":
                poss_diag_directions = [(-1, -1), (-1, 1)]       # can move diagonally forward in palace
            else:
                poss_diag_directions = [(1, -1), (1, 1)]         # can move diagonally forward in palace (POV RED)

        # add all possible moves to poss_moves_index
        self.save_moves(poss_directions + poss_diag_directions)
        return self._poss_moves_index

    def horse_moves(self):
        """
        Returns all possible moves for Horse pieces
        """
        row = self._curr_pos_index[0]  # first value represents row
        col = self._curr_pos_index[1]  # second value represents column

        poss_paths = [(-1, 0), (1, 0), (0, -1), (0, 1)]                 # UP, DOWN, LEFT, RIGHT (POV BLUE)
        poss_directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        # remove directions blocked by a piece
        for (x, y) in poss_paths:
            if self.check_range(row + x, col + y):
                if self.get_piece(row + x, col + y) != "--":
                    # horizontal move
                    if x == 0:
                        poss_directions.remove((x + 1, y * 2))
                        poss_directions.remove((x - 1, y * 2))
                    # vertical move
                    if y == 0:
                        poss_directions.remove((x * 2, y + 1))
                        poss_directions.remove((x * 2, y - 1))

        # add all possible moves to poss_moves_index
        self.save_moves(poss_directions)
        return self._poss_moves_index

    def elephant_moves(self):
        """
        Returns all possible moves for Elephant pieces
        """
        row = self._curr_pos_index[0]  # first value represents row
        col = self._curr_pos_index[1]  # second value represents column

        poss_paths1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]                 # UP, DOWN, LEFT, RIGHT (POV BLUE)
        poss_paths2 = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
        poss_directions = [(3, -2), (3, 2), (-3, -2), (-3, 2), (2, -3), (2, 3), (-2, -3), (-2, 3)]

        # remove directions blocked by a piece
        # checking poss_paths1
        for (x, y) in poss_paths1:
            if self.check_range(row + x, col + y):
                if self.get_piece(row + x, col + y) != "--":
                    # horizontal move
                    if x == 0:
                        poss_paths2.remove((x + 1, y * 2))
                        poss_paths2.remove((x - 1, y * 2))
                        poss_directions.remove((x + 2, y * 3))
                        poss_directions.remove((x - 2, y * 3))
                    # vertical move
                    if y == 0:
                        poss_paths2.remove((x * 2, y + 1))
                        poss_paths2.remove((x * 2, y - 1))
                        poss_directions.remove((x * 3, y + 2))
                        poss_directions.remove((x * 3, y - 2))
        # checking poss_path2
        for (x, y) in poss_paths2:
            if self.check_range(row + x, col + y):
                if self.get_piece(row + x, col + y) != "--":
                    if abs(x) == 2:
                        poss_directions.remove((int(x * 1.5), y * 2))
                    if abs(y) == 2:
                        poss_directions.remove((x * 2, int(y * 1.5)))

        # add all possible moves to poss_moves_index
        self.save_moves(poss_directions)
        return self._poss_moves_index

    def chariot_moves(self):
        """
        Returns all possible moves for Chariot pieces
        """
        row = self._curr_pos_index[0]  # first value represents row
        col = self._curr_pos_index[1]  # second value represents column

        poss_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]        # UP, DOWN, LEFT, RIGHT (POV BLUE)
        valid_directions = []

        for (x, y) in poss_directions:
            i = 1       # multiplier for directions

            while self.check_range(row + (x * i), col + (y * i)):
                new_pos_piece = self.get_piece(row + (x * i), col + (y * i))

                # valid direction if space is empty
                if new_pos_piece == "--":
                    valid_directions.append((x * i, y * i))
                    i += 1

                # if a piece is in the path, stops loop, direction is valid
                elif new_pos_piece[0] != self.get_opponent():
                    valid_directions.append((x * i, y * i))
                    break

                # if piece is active player's piece, direction not valid
                else:
                    break

                # if in palace, add more for diagonal movements



        # add all possible moves to poss_moves_index
        self.save_moves(poss_directions)
        return self._poss_moves_index



    def guard_moves(self):
        pass

    def cannon_moves(self):
        pass

    def general_moves(self):
        pass


def main():
    game = JanggiGame()
    game.get_board()
    game.make_move("a7", "a6")
    game.get_board()

    filled_board = [
        ["rc", "re", "rh", "rg", "--", "rg", "re", "rh", "rc"],
        ["--", "--", "--", "--", "rG", "--", "--", "--", "--"],
        ["--", "rC", "--", "--", "--", "--", "--", "rC", "--"],
        ["rs", "--", "rs", "--", "rs", "--", "rs", "--", "rs"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["bs", "--", "bs", "--", "bs", "--", "bs", "--", "bs"],
        ["--", "bC", "--", "--", "--", "--", "--", "bC", "--"],
        ["--", "--", "--", "--", "bG", "--", "--", "--", "--"],
        ["bc", "be", "bh", "bg", "--", "bg", "be", "bh", "bc"]
    ]

    print(filled_board[0][1])

if __name__ == "__main__":
    main()