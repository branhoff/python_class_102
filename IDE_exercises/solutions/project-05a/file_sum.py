# Author: Brandon Hoffman
# Date: 2/3/2021
# Description: function named file_sum that takes in txt file with numbers and writes sum of those numbesr
#              to new txt file.

def file_sum(txt_file_name):
    """
    input: txt file with numbers listed by newlines
    output: writes txt file sum.txt with sum of values from input
    """
    sum_ = 0
    with open (txt_file_name, 'r') as infile:
        for num in infile:
            sum_ += float(num)

    with open("sum.txt", 'w') as outfile:
        outfile.write(str(sum_))