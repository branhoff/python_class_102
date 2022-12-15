# Author: Brandon Hoffman
# Date: 2/10/2021
# Description: function is_sebequence takes 2 strings and returns True if
#              string_a is a substring of string_b returns False otherwise

def is_subsequence(string_a, string_b):
    """
    takes 2 strings and returns True if string_a is a substring of string_b
    returns False otherwise
    """
    if len(string_a) == 0:
        return True

    if len(string_b) == 0:
        return False

    if string_a[0] == string_b[0]:
        return is_subsequence(string_a[1:], string_b[1:])

    return is_subsequence(string_a, string_b[1:])