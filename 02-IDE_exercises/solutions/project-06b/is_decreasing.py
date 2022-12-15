# Author: Brandon Hoffman
# Date: 2/10/2021
# Description: function is_decreasing takes list of numbers and returns True if all numbers are strictly decreasing
#              will return False if not strictly decreasing


def is_decreasing(num_list):
    """
    input: takes list of numbers
    output: returns True if list is strictly decreasing, False if not
    """
    if len(num_list) < 2:
        return True

    if num_list[0] < num_list[1]:
        return False

    return is_decreasing(num_list[1:])
