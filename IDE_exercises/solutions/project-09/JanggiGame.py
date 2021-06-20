# Author: Brandon Hoffman
 # Date: 3/11/2021
 # Description: Models classes necessary to create backend for Janggi Game

class GamePiece:
    """
    Parent Class to set standard attributes for Game pieces
    """

    def __init__(self, player_piece_color):
        """
        Parent class to intialize Game piece colors, their type, and a dictionary with alist of diagonal moves
        """
        self._color = player_piece_color
        self._piece_type = self.__class__.__name__
        self._diagonal_moves = {(0, 3): [(1, 4), (2, 5)],
                                (0, 5): [(1, 4), (2, 3)],
                                (1, 4): [(0, 3), (0, 5), (2, 3), (2, 5)],
                                (2, 3): [(1, 4), (0, 5)],
                                (2, 5): [(1, 4), (0, 3)],
                            
                                (7, 3): [(8, 4), (9, 5)],
                                (7, 5): [(8, 4), (9, 3)],
                                (8, 4): [(7, 3), (7, 5), (9, 3), (9, 5)],
                                (9, 3): [(8, 4), (7, 5)],
                                (9, 5): [(8, 4), (7, 3)]}

    def __str__(self):
        """
        Dunder method to allow for class string representation for testing purposes
        """
        return self.__class__.__name__ + self.get_color()

    def get_color(self):
        """
        Returns player piece by its color
        """
        return self._color

    def get_piece_type(self):
        """
        returns private piece_type variable
        """
        return self._piece_type


class General(GamePiece):
    """
    Represents General game piece, inherits from Game Piece class
    """
    pass

    def __init__(self, _color):
        """
        initalizes color from Parent class and list of possible move coordinates
        """
        super().__init__(_color)
        self._moves = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1), (0, 0), (0, 1), 
                       (1, 1), (1, 0), (1, -1), ]

    def is_legal_move(self, x_from, y_from, x_to, y_to, board):
        """
        checks that General piece can make attempted move
        returns True if legal, False otherwise
        """
        if (x_to, y_to) in Board().get_palace(self.get_color()):
            diff = (x_to - x_from, y_to - y_from)
            return diff in self._moves
        else:
            False
             
class Guard(GamePiece):
    """
    Represents Guard game piece, inherits from Game Piece class
    """

    def __init__(self, _color):
        """

        """
        super().__init__(_color)
        self._moves = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1), (0, 0), (0, 1), 
                       (1, 1), (1, 0), (1, -1)]


    def is_legal_move(self, x_from, y_from, x_to, y_to, board):
        """
        checks that Guard piece can make attempted move
        returns True if legal, False otherwise
        """
        if (x_to, y_to) in Board().get_palace(self.get_color()):
            diff = (x_to - x_from, y_to - y_from)
            return diff in self._moves
        else:
            return False

        
class Horse(GamePiece):
    """
    Represents Horse game piece, inherits from Game Piece class
    """

    def __init__(self, _color):
        """

        """
        super().__init__(_color)
        self._moves = [(-1, -2), (-1, 2), (-2, -1),
                       (-2, 1), (0, 0), (1, -2), 
                       (1, 2), (2, -1), (2, 1)]
    
    def is_legal_move(self, x_from, y_from, x_to, y_to, board):
        """
        checks that Horse piece can make attempted move
        returns True if legal, False otherwise
        """

        diff = (x_to - x_from, y_to - y_from)
        return diff in self._moves

class Elephant(GamePiece):
    """
    Represents Elephant game piece, inherits from Game Piece class
    """

    def __init__(self, _player_piece_color):
        """

        """
        super().__init__(_player_piece_color)
        self._moves = [(-3, -2), (-3, 2), (-2, -3),
                       (-2, 3), (0, 0), (2, -3), 
                       (2, 3), (3, -2), (3, 2)]


    def is_legal_move(self, x_from, y_from, x_to, y_to, board):
        """
        checks that Horse piece can make attempted move
        returns True if legal, False otherwise
        """
        
        diff = (x_to - x_from, y_to - y_from)
        return diff in self._moves

class Chariot(GamePiece):
    """
    Represents Chariot game piece, inherits from GamePiece class
    """
    def __init__(self, _color):
        """

        """
        super().__init__(_color)

    def is_legal_move(self, x_from, y_from, x_to, y_to, board):
        """
        checks that Chariot piece can make attempted move
        returns True if legal, False otherwise
        """
        x_step = 1 if x_from < x_to else -1
        y_step = 1 if y_from < y_to else -1

        if not (x_from == x_to or y_from == y_to):
            return False

        if x_from == x_to:
            col = x_from
            for row in range(y_from + y_step, y_to, y_step):
                if board[col][row] != "":
                    return False
        if y_from == y_to:
            row = y_from
            for col in range(x_from + x_step, x_to, x_step):
                if board[col][row] != "":
                    return False
        return True
    

class Cannon(GamePiece):
    """
    Represents Cannon game piece, inherits from GamePiece class
    """
    def __init__(self, _player_piece_color):
        """

        """
        super().__init__(_player_piece_color)


    def is_legal_move(self, x_from, y_from, x_to, y_to, board):
        """
        checks that Cannon piece can make attempted move
        returns True if legal, False otherwise
        """
        x_step = 1 if x_from < x_to else -1
        y_step = 1 if y_from < y_to else -1

        if not (x_from == x_to or y_from == y_to):
            return False

        try:
            if board[x_to][y_to].get_piece_type() == "Cannon":
                return False
        except AttributeError:
            pass
        
        piece_count = 0
        if x_from == x_to:
            col = x_from
            for row in range(y_from + y_step, y_to, y_step):
                if board[col][row] != "":
                    piece_count += 1
                    if piece_count > 1:
                        return False
                    if board[col][row].get_piece_type() == "Cannon":
                        return False

        if y_from == y_to:
            row = y_from
            for col in range(x_from + x_step, x_to, x_step):
                if board[col][row] != "":
                    piece_count += 1
                    if piece_count > 1:
                        return False
                    if board[col][row].get_piece_type() == "Cannon":
                        return False
        if piece_count == 0:
            return False
        return True

class Soldier(GamePiece):
    """
    Represents Soldier game piece, inherits from GamePiece class
    """

    def __init__(self, _player_piece_color):
        """

        """
        super().__init__(_player_piece_color)
        if self.get_color() == "BLUE":
            self._moves = [(-1, 0), (0, -1), (0, 0), (0, 1)] # for Blue

        elif self.get_color() == "RED":
            self._moves = [(1, 0), (0, -1), (0, 0), (0, 1)] # for Red

    def is_legal_move(self, x_from, y_from, x_to, y_to, board):
        """
        checks that Soldier piece can make attempted move
        returns True if legal, False otherwise
        """
        diff = (x_to - x_from, y_to - y_from)
        return diff in self._moves

class Board:
    """
    Represents board and stores instances of piece classes for every player
    """

    def __init__(self):
        """
        initializes board and pieces
        """

        self._num_row = 10
        self._num_col = 9
        self._general_positions = {"RED": (1, 4) , "BLUE": (8, 4)}
        
        self._board = [[Chariot("RED"), Elephant("RED"), Horse("RED"), Guard("RED"), "", Guard("RED"), Elephant("RED"), Horse("RED"), Chariot("RED")],
                       ["", "", "", "", General("RED"), "", "", "", ""],
                       ["", Cannon("RED"), "", "", "", "", "", Cannon("RED"), ""],
                       [Soldier("RED"), "", Soldier("RED"), "", Soldier("RED"), "", Soldier("RED"), "", Soldier("RED")],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       [Soldier("BLUE"), "", Soldier("BLUE"), "", Soldier("BLUE"), "", Soldier("BLUE"), "", Soldier("BLUE")],
                       ["", Cannon("BLUE"), "", "", "", "", "", Cannon("BLUE"), ""],
                       ["", "", "", "", General("BLUE"), "", "", "", ""],
                       [Chariot("BLUE"), Elephant("BLUE"), Horse("BLUE"), Guard("BLUE"), "", Guard("BLUE"), Elephant("BLUE"), Horse("BLUE"), Chariot("BLUE")]]

        self._palace =  {"RED":  [(0, 3), (0, 4), (0, 5),
                                  (1, 3), (1, 4), (1, 5),
                                  (2, 3), (2, 4), (2, 5)],

                         "BLUE": [(7, 3), (7, 4), (7, 5),
                                  (8, 3), (8, 4), (8, 5),
                                  (9, 3), (9, 4), (9, 5)]}

    def get_len_cols(self):
        """
        returns len of columns in board
        """
        return self._num_col

    def get_len_rows(self):
        """
        returns number of rows in board
        """
        return self._num_row

    def get_general_coordinates(self, color):
        """
        returns The corresponding player (by color's) current General Coordinates
        """
        return self._general_positions[color]

    def get_board(self):
        """
        returns board list of lists
        """
        return self._board

    def get_palace(self, player_color):
        """
        returns dictionary with list of lists for each color player representing palace coordinates
        """
        return self._palace[player_color]

    def set_general_coord(self, color, coords):
        """
        sets new coordinates for General
        """
        self._general_positions[color] = coords

    def set_board(self, from_idx, to_idx):
        """
        from_idx: tuple with (x,y) coordinates
        to_idx: tuple with (x,y) coordinates
        returns True if piece is moved successfully
        returns False otherwise
        """
        x_from, y_from = from_idx
        x_to, y_to = to_idx

        piece = self._board[x_from][y_from]

        if piece.is_legal_move(x_from, y_from, x_to, y_to, self.get_board()):
        
            self._board[x_to][y_to] = piece
            self._board[x_from][y_from] = ""
            if piece.get_piece_type() == "General":
                self.set_general_coord(piece.get_color(), (x_to, y_to))
        
            return True
        else:
            return False

    def _reset_board(self, new_board):
        """
        resets board in the event of a check
        """
        self._board = new_board


        
    def format_row(self, row, idx=0):
        """
        formats row for testing purposes to be printed
        """
        return f'{idx:2}|' + '|'.join(f'{str(x):12}' for x in row) + '|'

    def format_board(self, board):
        """
        formats board for testing purposes to be printed
        """
        return '\n'.join(self.format_row(row, i+1) for i, row in enumerate(board))

    def print_board(self):
        """
        Displays board
        """
        print(self.format_row(["A", "B", "C", "D", "E", "F", "G", "H", "I"]))
        print(self.format_board(self._board),'\n')

class JanggiGame():
    """
    Represents JangiGame to be played. Contains methods that modify game state
    """
    def __init__(self):
        """

        """
        self._current_state = "UNFINISHED"
        self._player_turn = "BLUE"
        self._board = Board()

    def get_game_state(self):
        """
        returns private _current_state variable
        """
        return self._current_state

    def get_player_turn(self):
        """
        returns private _player_turn variable
        """
        return self._player_turn

    def _is_valid_coordinates(self, row, col):
        """
        Returns True if within bounds of board matrix limits
        False otherwise
        """
        board = self._board
        return 0 <= row < board.get_len_rows() and 0 <= col < board.get_len_cols()

    def _is_valid_turn(self, from_coord):
        """
        tests whether piece attempting to move is associated with correct players turn
        """
        from_piece = self._board.get_board()[from_coord[0]][from_coord[1]]

        try:
            piece_color = from_piece.get_color()
        except AttributeError:
            return False

        if piece_color != self._player_turn:
            return False
        else:
            return True

    def _is_itself(self, from_coord, to_coord):
        """
        Confirms wihether a player is simply moving the same piece to its current position
        """
        from_piece = self._board.get_board()[from_coord[0]][from_coord[1]]
        to_piece = self._board.get_board()[to_coord[0]][to_coord[1]]

        return from_piece == to_piece

    def _is_enemy(self, to_coord):
        """
        tests whether piece at coordinates is en enemy piece
        """

        to_piece = self._board.get_board()[to_coord[0]][to_coord[1]]

        if to_piece == "":
            return True

        piece_color = to_piece.get_color()

        if piece_color is not self.get_player_turn():
            return True
        else:
            return False

    def _algebraic_notation_converter(self, alg_coord):
        """
        Takes in Alegebraic Notation like "A1" and returns tuple matrix notaion
        suchas (0,0)
        returns False if TypeError
        """
        try:
            return int(alg_coord[1:])-1, ord(alg_coord[0].upper())-65 
        except TypeError:
            return False

    def _set_player_turn(self):
        """
        private method to change the _player_turn variable to the next player
        """
        if self.get_player_turn() == "BLUE":
            self._player_turn = "RED"

        else:
            self._player_turn = "BLUE"

    def _set_current_state(self):
        """
        sets the current state to 'UNFINISHED' or 'RED_WON' or 'BLUE_WON'.
        """
        if self._player_turn == "RED":
            self._current_state = "BLUE_WON"
        elif self._player_turn == "BLUE":
            self._current_state = "RED_WON"

    def _is_possible(self, from_idx, to_idx):
        """
        Compiles conditional methods above. Returns False if inputs are illegal
        """
        if not self._is_valid_coordinates(from_idx[0], from_idx[1]):
            return False

        if not self._is_valid_coordinates(to_idx[0], to_idx[1]):
            return False

        if not self._is_valid_turn(from_idx):
            return False

        if not self._is_itself(from_idx, to_idx):

            if not self._is_enemy(to_idx):
                return False

        return True

    def is_in_check(self, player):
        """
        takes parameter for 'Red' or 'Blue' player
        Returns True if player is in check, returns False otherewise
        """
        color = player.upper()
        general_coords = self._board.get_general_coordinates(color)

        for row_num, row in enumerate(self._board.get_board()):
            for col_num, piece in enumerate(row):
                if piece != "":
                    if piece.get_color() != color:
                        
                        if piece.is_legal_move(row_num, col_num, general_coords[0], general_coords[1], self._board.get_board()):
                            return True

        return False


    def make_move(self, from_alg_notation, to_alg_notation):
        """
        first calls _check_legal_inputs variable. If inputs are legal, calls the set_current state method, set_player_turn method and increase _turn_count variable
        """
        try:
            from_idx = self._algebraic_notation_converter(from_alg_notation)
            to_idx = self._algebraic_notation_converter(to_alg_notation)
        
        except TypeError:
            return False

        board_copy = self._board.get_board()

        if self.get_game_state() != "UNFINISHED":
            return False

        if not (from_alg_notation == to_alg_notation):

            if not self._is_possible(from_idx, to_idx):
                return False

            if not self._board.set_board(from_idx, to_idx):
                return False

        if self.is_in_check(self._player_turn):
            self._board._reset_board(board_copy)
            return False

        else:
            self._set_player_turn()
            return True

