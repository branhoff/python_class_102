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

        self._check = False
        self._checkmate = False
        self._threat_piece = None
        self._threat_piece_index = []

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
        print("This is the board key:")
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
            print("RED has won the game!")
        else:
            self._game_state = "BLUE_WON"
            print("BLUE has won the game!")

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

        self._check = False

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
            if new_pos_piece != "--" and new_pos_piece[0] != self.get_opponent():
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

                # check if opponent in check
                temp_check = self._check
                self.is_check()

                # check if move puts/leaves active_player's General in check
                if self.is_self_check() is True:
                    self._filled_board = copied_board
                    self._check = temp_check
                    print("ERROR! Move puts active_player in check")
                    return False

                # if check, check if checkmate
                if self._check == self.get_opponent():
                    # save threat_piece to use in is_checkmate
                    self._threat_piece = self._filled_board[x][y]
                    self._threat_piece_index = [x, y]
                    self.is_checkmate()

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
        elif piece_indicator == "c":
            self.chariot_moves()
            return self._poss_moves_index
        elif piece_indicator == "C":
            self.cannon_moves()
            return self._poss_moves_index
        elif piece_indicator == "g" or "G":
            self.general_and_guard_moves()
            return self._poss_moves_index

    def save_moves(self, poss_directions):
        """
        Saves all possible moves for each piece's indiv move functions.
        Also saves taken pieces.
        """
        row = self._curr_pos_index[0]  # first value represents row
        col = self._curr_pos_index[1]  # second value represents column

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
        row = self._curr_pos_index[0]  # first value represents row
        col = self._curr_pos_index[1]  # second value represents column

        if self.get_active_player() == "b":
            poss_directions = [(0, -1), (-1, 0), (0, 1)]  # LEFT, UP, RIGHT
        else:
            poss_directions = [(0, -1), (1, 0), (0, 1)]  # RIGHT, UP, LEFT (POV RED)

        # more possibilities if in palace (can move diagonally)
        diag_positions = [(0, 3), (2, 3), (7, 3), (9, 3), (1, 4), (8, 4), (0, 5), (2, 5), (7, 5), (9, 5)]
        poss_diag_directions = []
        if (row, col) in diag_positions:
            if self.get_active_player() == "b":
                poss_diag_directions = [(-1, -1), (-1, 1)]  # can move diagonally forward in palace
            else:
                poss_diag_directions = [(1, -1), (1, 1)]  # can move diagonally forward in palace (POV RED)

        # add all possible moves to poss_moves_index
        self.save_moves(poss_directions + poss_diag_directions)
        return self._poss_moves_index

    def horse_moves(self):
        """
        Returns all possible moves for Horse pieces
        """
        row = self._curr_pos_index[0]  # first value represents row
        col = self._curr_pos_index[1]  # second value represents column

        poss_paths = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # UP, DOWN, LEFT, RIGHT (POV BLUE)
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

        poss_paths1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]            # UP, DOWN, LEFT, RIGHT (POV BLUE)
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
                elif new_pos_piece[0] == self.get_opponent():
                    valid_directions.append((x * i, y * i))
                    break

                # if piece is active player's piece, direction not valid
                else:
                    break

        # if in palace, add more for diagonal movements
        diag_positions = [(0, 3), (2, 3), (7, 3), (9, 3), (0, 5), (2, 5), (7, 5), (9, 5)]
        poss_diag_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # if in palace and move entered is diagonal
        if (row, col) in diag_positions:

            for (x, y) in poss_diag_directions:
                i = 1

                # new_pos space must still be in the palace
                while (row + (x * i), col + (y * i)) in diag_positions:
                    new_pos_piece = self.get_piece(row + (x * i), col + (y * i))

                    # valid if new_pos space is empty
                    if new_pos_piece == "--":
                        valid_directions.append((x * i, y * i))
                        i += 1

                    # valid if new_pos space has opponent piece
                    elif new_pos_piece[0] == self.get_opponent():
                        valid_directions.append((x * i, y * i))
                        break

                    # invalid if new_pos space has active player's piece
                    else:
                        break

        # add all possible moves to poss_moves_index
        self.save_moves(valid_directions)
        return self._poss_moves_index

    def cannon_moves(self):
        """
        Returns all possible moves for Cannon pieces
        """
        row = self._curr_pos_index[0]  # first value represents row
        col = self._curr_pos_index[1]  # second value represents column

        poss_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # UP, DOWN, LEFT, RIGHT (POV BLUE)
        valid_directions = []

        for (x, y) in poss_directions:
            i = 1
            jumpover_piece = None

            while self.check_range(row + (x * i), col + (y * i)):
                space_occupant = self.get_piece(row + (x * i), col + (y * i))

                # if cannon has not jumped yet
                if jumpover_piece is None:
                    # if space not occupied by piece, valid and continue loop
                    if space_occupant == "--":
                        i += 1
                    # if space occupied by non-Cannon piece, valid, save piece and continue
                    elif space_occupant[1] != "C":
                        jumpover_piece = space_occupant
                        i += 1
                    # if space occupied by Cannon piece, invalid, stop loop
                    else:
                        break

                # if cannon already jumped over 1 piece
                else:
                    # if space is not occupied, valid and continue loop
                    if space_occupant == "--":
                        valid_directions.append((x * i, y * i))
                        i += 1
                    # if space occupied by opponent piece, valid, add direction and stop
                    elif space_occupant[0] == self.get_opponent() and space_occupant[1] != "C":
                        valid_directions.append((x * i, y * i))
                        break
                    # if space occupied by Cannon or own piece, invalid, stop loop
                    else:
                        break

        # if cannon on palace corners, can move diagonally
        diag_positions = [(0, 3), (2, 3), (7, 3), (9, 3), (0, 5), (2, 5), (7, 5), (9, 5)]
        poss_diag_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # if in palace and move entered is diagonal
        if (row, col) in diag_positions:

            for (x, y) in poss_diag_directions:
                # the move must keep the piece within the palace
                if (row + (x * 2), col + (y * 2)) in diag_positions:
                    jumpover_piece = self.get_piece(row + x, col + y)
                    new_pos_piece = self.get_piece(row + (x * 2), col + (y * 2))

                    # if jumpover_piece exists and is not Cannon
                    if jumpover_piece != "--" and jumpover_piece != "C":

                        # if new_pos space is empty, valid
                        if new_pos_piece == "--":
                            valid_directions.append((x * 2, y * 2))

                        # if new_pos space is occupied by opponent non-Cannon piece, valid
                        elif new_pos_piece[0] == self.get_opponent() and new_pos_piece[1] != "C":
                            valid_directions.append((x * 2, y * 2))

        # add all possible moves to poss_moves_index
        self.save_moves(valid_directions)
        return self._poss_moves_index

    def general_and_guard_moves(self):
        """
        Returns all possible moves for General and Guard pieces.
        """
        row = self._curr_pos_index[0]  # first value represents row
        col = self._curr_pos_index[1]  # second value represents column

        #
        if self.get_active_player() == "b":
            # positions that allow diagonal movement in palace
            diag_positions = [(7, 3), (9, 3), (7, 5), (9, 5), (8, 4)]
            # positions that only allow linear movement in palace
            linear_positions = [(8, 3), (8, 5), (7, 4), (9, 4)]
        else:
            diag_positions = [(0, 3), (2, 3), (0, 5), (2, 5), (1, 4)]
            linear_positions = [(1, 3), (1, 5), (0, 4), (2, 4)]

        if (row, col) in diag_positions:
            poss_directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        else:
            poss_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # pieces CANNOT leave the palace
        palace_spaces = diag_positions + linear_positions
        for (x, y) in poss_directions:
            if self.check_range(row + x, col + y):
                if (row + x, col + y) not in palace_spaces:
                    poss_directions.remove((x, y))

        # add all possible moves to poss_moves_index
        self.save_moves(poss_directions)
        return self._poss_moves_index

    def is_check(self):
        """
        Generates all possible moves of all active_player pieces
        Checks if opponent's General is threatened/could be taken on active_player's next move
        """
        # reset taken_pieces list
        self._taken_pieces = ["--"]

        # goes through entire board, checking all possible moves for all active_player pieces
        for i in range(0, 10):
            for j in range(0, 9):
                if self._filled_board[i][j][0] == self.get_active_player():
                    piece_indicator = self._filled_board[i][j][1]

                    # save piece's index, gets all possible moves of specific piece
                    temp_index = self._curr_pos_index
                    self._curr_pos_index = [i, j]
                    self.get_all_moves(piece_indicator)
                    self._curr_pos_index = temp_index

                    # if opp_general can be taken by any active_player piece, opponent in check!
                    for x in range(len(self._taken_pieces)):
                        if self._taken_pieces[x][0] == self.get_opponent() and self._taken_pieces[x][1] == "G":
                            self._check = self.get_opponent()

    def is_checkmate(self):
        """
        Assumes checkmate is true, tries to find escape route
        FIRST: Checks if General can move out of check or take the threat_piece
        SECOND: Checks if any active_player pieces can take the threat_piece
        THIRD: Checks if any active_player pieces can block the path of the threat_piece
        """
        # assumes checkmate is true
        self._checkmate = True

        # gets General's position
        general = None
        for i in range(1, 10):
            for j in range(1, 9):
                if self._filled_board[i][j] == self.get_active_player() + "G":
                    general = self._filled_board[i][j]
                    self._curr_pos_index = [i, j]
                    break
                j += 1
            i += 1

        row = self._curr_pos_index[0]       # first value represents row
        col = self._curr_pos_index[1]       # second value represents col

        # FIRST --- checks if General can move out of check or take the threat_piece

        # gets all possible moves of the General
        self.get_all_moves("G")

        # save current board in case moving the General does not resolve check
        copied_board = copy.deepcopy(self._filled_board)

        # tries all possible General moves
        for (x, y) in self._poss_moves_index:
            self._filled_board[x][y] = general
            self._filled_board[row][col] = "--"

            # checks if still check; if no longer check, not checkmate
            # switches active_player for is_check test
            self._turn_count += 1
            temp_check = self._check
            self._check = False
            # calls is_check to see if still check or not
            self.is_check()
            if self.is_check() is False:
                self._checkmate = False
            self._check = temp_check
            # switches active_player back
            self._turn_count -= 1

        # reverts the board to how it was before moving General
        self._filled_board = copied_board

        # SECOND --- checks if any active_player pieces can take the threat_piece

        # reset taken_pieces list
        self._taken_pieces = ["--"]

        # goes through entire board, checks if any active_player pieces can take the threat_piece
        for x in range(0, 10):
            for y in range(0, 9):
                if self.get_piece(x, y)[0] == self.get_active_player():
                    piece_indicator = self._filled_board[x][y][1]

                    self._curr_pos_index = [x, y]
                    self.get_all_moves(piece_indicator)

                    # if threat_piece can be taken, not checkmate
                    for i in range(len(self._taken_pieces)):
                        if self._taken_pieces[i] == self._threat_piece:
                            self._checkmate = False
                            break
                            # if not, loop continues

        # THIRD --- checks if any active_player pieces can block the path of the threat_piece

        # if checkmate status is still True, calls check_block
        if self._checkmate:
            if self.check_block(row, col):      # passing in General's location
                self._checkmate = False

        # if checkmate is STILL True, it MUST be checkmate
        if self._checkmate:
            self.set_game_state()

    def check_block(self, row, col):
        """
        Checks if any active_player non-General pieces can block the path of the threat_piece
        """
        check_path = []
        # General's row and col
        G_row = row
        G_col = col
        # threat_piece's row and col
        threat_row = self._threat_piece_index[0]
        threat_col = self._threat_piece_index[1]

        # if threat_piece is Horse
        if self._threat_piece[1] == "h":
            # get the spaces on the path from the threat_piece to the General
            # vertical move
            if abs(threat_row - G_row) > abs(threat_col - G_col):
                # one space in front/behind
                check_path.append((threat_row - int((threat_row - G_row) / 2), threat_col))
            # horizontal move
            else:
                # one space L or R
                check_path.append((threat_row, threat_col - int((threat_col - G_col) / 2)))

        # if threat_piece is Elephant
        if self._threat_piece[1] == "e":
            # get the spaces on the path from the threat_piece to the General
            # vertical move
            if abs(threat_row - G_row) > abs(threat_col - G_col):
                # one space in front/behind
                check_path.append((threat_row - int((threat_row - G_row) / 3), threat_col))
                # one space diag L or R
                check_path.append((threat_row - int((threat_row - G_row) * 2 / 3),
                                   threat_col - int((threat_col - G_col) / 2)))
            # horizontal move
            else:
                # one space L or R
                check_path.append((threat_row, threat_col - int((threat_col - G_col) / 3)))
                # one space diag up/down
                check_path.append((threat_row - int((threat_row - G_row) / 2),
                                   threat_col - int((threat_col - G_col) * 2 / 3)))

        # if threat_piece is Chariot or Cannon
        if self._threat_piece[1] == "c" or self._threat_piece[1] == "C":
            # get the spaces on the path from the threat_piece to the General
            # vertical move
            if threat_col == G_col:
                # checks if going forwards or backwards
                direction = (threat_row - G_row) / (abs(threat_row - G_row))

                for i in range(abs(threat_row - G_row)):
                    space_occupant = self.get_piece(int(threat_row - direction * (i + 1)), G_col)
                    if space_occupant == "--":
                        check_path.append((int(threat_row - direction * (i + 1)), G_col))
            # horizontal move
            if threat_row == G_row:
                # checks if going left or right
                direction = (threat_col - G_col) / (abs(threat_col - G_col))

                for i in range(abs(threat_col - G_col)):
                    space_occupant = self.get_piece(G_row, int(threat_col - direction * (i + 1)))
                    if space_occupant == "--":
                        check_path.append((G_row, int(threat_col - direction * (i + 1))))

        # goes through entire board, checks in any active_player pieces can block the check_path
        for x in range(0, 10):
            for y in range(0, 9):
                space_occupant = self.get_piece(x, y)

                # checks if any active_player pieces (except the General) can block the check_path
                if space_occupant[0] == self.get_active_player() and space_occupant[1] != "G":
                    piece_indicator = space_occupant[1]

                    # save piece's index, gets all possible moves of specific piece
                    temp_index = self._curr_pos_index
                    self._curr_pos_index = [x, y]
                    self.get_all_moves(piece_indicator)
                    self._curr_pos_index = temp_index

                    # returns True if the specific piece can block the check_path
                    for position in check_path:
                        if position in self._poss_moves_index:
                            return True

    def is_self_check(self):
        """
        Checks if active_player makes a move that puts themselves in check
        Checks if active_player is in check and makes a move that leaves active_player in check
        """
        # reset taken_pieces list
        self._taken_pieces = ["--"]

        # goes through entire board, checking all possible moves for all active_player pieces
        for i in range(0, 10):
            for j in range(0, 9):
                if self._filled_board[i][j][0] == self.get_opponent():
                    piece_indicator = self._filled_board[i][j][1]

                    # saves piece's index, gets all possible moves of specific piece
                    # switches active_player to check if opponent checks active_player
                    self._turn_count += 1
                    temp_index = self._curr_pos_index
                    self._curr_pos_index = [i, j]
                    self.get_all_moves(piece_indicator)
                    self._curr_pos_index = temp_index
                    # switches active_player back
                    self._turn_count -= 1

                    # if General is taken, the move puts/leaves active_player's General in check
                    # move considered INVALID
                    for x in range(len(self._taken_pieces)):
                        if self._taken_pieces[x][0] == self.get_active_player() and self._taken_pieces[x][1] == "G":
                            return True
        return False

    def is_in_check(self):
        """
        Returns T or F to see if player is_in_check or not for testing purposes
        """
        if self._check == "b" and self.get_active_player() == "b":
            return True
        elif self._check == "r" and self.get_active_player() == "r":
            return True
        return False

    def remove_piece(self, row, col):
        """
        Removes pieces from the board for testing purposes
        """
        space_occupant = self.get_piece(row, col)
        if space_occupant != "--":
            self._filled_board[row][col] = "--"
        else:
            print("ERROR removing piece")
            return False


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
