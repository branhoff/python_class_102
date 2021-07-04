# Author: Brandon Hoffman
 # Date: 3/11/2021
 # Description: Models classes necessary to create backend for Janggi Game
from Board import Board



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

