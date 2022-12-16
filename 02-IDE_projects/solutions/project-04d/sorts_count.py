 # Author: Brandon Hoffman
 # Date: 1/27/2021
 # Description: two functions, bubble_count and insertion_count, provide a tuple of counts of comparisons and exchanges performed with sort functions



def bubble_count(a_list):    
    """    
    Sorts a_list in ascending order
    returns tuple of comparison_count and exchange_count    
    """
    comparison_count = 0
    exchange_count = 0
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            comparison_count += 1
            if a_list[index] > a_list[index + 1]:                
                temp = a_list[index]                
                a_list[index] = a_list[index + 1]                
                a_list[index + 1] = temp
                exchange_count += 1

    return (comparison_count, exchange_count)


def insertion_count(a_list):    
    """    
    Sorts a_list of strings in descending alphabetical order
    returns tuple of comparison_count and exchange_count     
    """
    comparison_count = 0
    exchange_count = 0
    for index in range(1, len(a_list)):        
        value = a_list[index]     
        pos = index - 1  
        while pos >= 0 and a_list[pos] > value:
            if a_list[pos] > value:
                comparison_count += 1         
            a_list[pos + 1] = a_list[pos]            
            pos -= 1        
            a_list[pos + 1] = value
            exchange_count += 1

    return (comparison_count, exchange_count)
