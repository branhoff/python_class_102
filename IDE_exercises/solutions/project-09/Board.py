

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
