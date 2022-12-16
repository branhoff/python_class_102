# Author: Brandon Hoffman
# Date: 2/10/2021
# Description: returns max number from list of numbers

def list_max(num_list):
    """
    Recursive function to return max number in list
    input: list of numbers
    output: max number from list
    """
    if len(num_list) == 1:
        return num_list[0]

    else:
        previous = list_max(num_list[1:])
        current = num_list[0]
        if previous > current:
            return previous
        else:
            return current