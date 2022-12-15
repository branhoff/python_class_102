 # Author: Brandon Hoffman
 # Date: 1/27/2021
 # Description: binary search function that uses a TargetNotFound exception, when item not in list


class TargetNotFound(Exception):
    """
    Error to be used for when target not found in list
    """
    pass

def bin_except(a_list, target):
    """    
    Searches a_list for an occurrence of target    
    If found, returns the index of its position in the list    
    If not found, returns TargetNotFound Error, indicating the target value isn't in the list    
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
      middle = (first + last) // 2        
      if a_list[middle] == target:            
        return middle        
      if a_list[middle] > target:            
        last = middle - 1        
      else:            
        first = middle + 1    
    raise TargetNotFound