 # Author: Brandon Hoffman
 # Date: 2/24/2021
 # Description: function that writes count_seq

def count_seq():
    """
    generator function that takes no parameters
    initializes an n_string '2', subsequently, counts the previous yield
    so "one" 2, represented as 12
    the next yield would be "one" 1 and "one" 2 represented as 1112
    and so on...
    """
    n_string = '2'

    while True:
        yield n_string
        next_value = ''

        while len(n_string) > 0:
            first = n_string[0]
            count = 0

            while len(n_string) > 0 and n_string[0] == first:
                count += 1
                n_string = n_string[1:]

            next_value += f'{count}{first}'

        n_string = next_value