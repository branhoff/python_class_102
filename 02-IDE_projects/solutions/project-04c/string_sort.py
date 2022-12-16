 # Author: Brandon Hoffman
 # Date: 1/27/2021
 # Description: Project sorts list of strings in alphabetical order

def string_sort(a_list):    
  """    
  Sorts a_list of strings in descending alphabetical order    
  """    
  for index in range(1, len(a_list)):        
    value = a_list[index]     
    pos = index - 1        
    while pos >= 0 and a_list[pos].lower() > value.lower():            
      a_list[pos + 1] = a_list[pos]            
      pos -= 1        
    a_list[pos + 1] = value
