# Author: Brandon Hoffman
# Date: 2/10/2021
# Description: takes list of integers and a starting position
#              You have a token that starts on the leftmost square. On each turn, 
#              the token can shift left or right a number of squares equal to the value 
#              in its current square, but is not allowed to move off either end

def row_puzzle(squares, position=0):
    """
    takes list of integers and a starting position
    You have a token that starts on the leftmost square. On each turn, 
    the token can shift left or right a number of squares equal to the value 
    in its current square, but is not allowed to move off either end

    input: squares - list of ints, position - place of token
    output: returns True if arrives at end of puzzle
            returns False if cannot arrive at end of puzzle
    """
    if position == len(squares) - 1:
        return True

    else:
        left_pos = position - squares[position]
        right_pos = position + squares[position]

        if right_pos < len(squares) and row_puzzle(squares, right_pos):
            return True

        if left_pos > 0 and row_puzzle(squares, left_pos):
            return True

        return False