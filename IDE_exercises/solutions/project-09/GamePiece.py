import board

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

    def get_piece_name(self):
        """
        returns private piece_type variable
        """
        return self._piece_type

    def get_diagonal_moves(self, position):
        """
        
        """
        return self._diagonal_generator(position)

    def _diagonal_generator(self, position):
        """[summary]

        Args:
            position (tuple): [description]

        Returns:
            list: array of tuples with x,y matrix coordinates
        """
        x,y = position
        deltas = (-1, 1)
        x_positions = [x + i for i in deltas if -1 < x + i < 9]
        y_positions = [y + i for i in deltas if -1 < y + i < 10]

        #print(list(x_positions))
        #print(list(y_positions))

        for x_pos in x_positions:
            for y_pos in y_positions:
                yield x_pos, y_pos

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

    def is_legal_move(self, x_from, y_from, x_to, y_to, game_board):
        """
        checks that General piece can make attempted move
        returns True if legal, False otherwise
        """
        if (x_to, y_to) in board.Board().get_palace(self.get_color()):
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


    def is_legal_move(self, x_from, y_from, x_to, y_to, game_board):
        """
        checks that Guard piece can make attempted move
        returns True if legal, False otherwise
        """
        if (x_to, y_to) in board.Board().get_palace(self.get_color()):
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
    
    def is_legal_move(self, x_from, y_from, x_to, y_to, game_board):
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


    def is_legal_move(self, x_from, y_from, x_to, y_to, game_game_board):
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

    def is_legal_move(self, x_from, y_from, x_to, y_to, game_game_game_board):
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
                if game_game_game_board[col][row] != "":
                    return False

        if y_from == y_to:
            row = y_from
            for col in range(x_from + x_step, x_to, x_step):
                if game_game_game_board[col][row] != "":
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


    def is_legal_move(self, x_from, y_from, x_to, y_to, game_board):
        """
        checks that Cannon piece can make attempted move
        returns True if legal, False otherwise
        """
        x_step = 1 if x_from < x_to else -1
        y_step = 1 if y_from < y_to else -1

        if not (x_from == x_to or y_from == y_to):
            return False

        try:
            if game_board[x_to][y_to].get_piece_name() == "Cannon":
                return False
        except AttributeError:
            pass
        
        piece_count = 0
        if x_from == x_to:
            col = x_from
            for row in range(y_from + y_step, y_to, y_step):
                if game_board[col][row] != "":
                    piece_count += 1
                    if piece_count > 1:
                        return False
                    if game_board[col][row].get_piece_name() == "Cannon":
                        return False

        if y_from == y_to:
            row = y_from
            for col in range(x_from + x_step, x_to, x_step):
                if game_board[col][row] != "":
                    piece_count += 1
                    if piece_count > 1:
                        return False
                    if game_board[col][row].get_piece_name() == "Cannon":
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

    def is_legal_move(self, x_from, y_from, x_to, y_to, game_board):
        """
        checks that Soldier piece can make attempted move
        returns True if legal, False otherwise
        """
        diff = (x_to - x_from, y_to - y_from)
        return diff in self._moves