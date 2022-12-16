# Author: Brandon Hoffman
# Date: 1/27/2021
# Description: Box Class and a separate function that uses insertion sort to sort a list of boxes from greatest volume to least volume

class Box:
    """
    Models a box with intialized private values of length, width, height
    """

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """
        returns length attribute
        """
        return self._length

    def get_width(self):
        """
        returns width attribute
        """
        return self._width

    def get_height(self):
        """
        returns height attribute
        """
        return self._height

    def volume(self):
        """
        returns volume attribute
        """
        return self._length * self._width * self._height


def box_sort(a_list):    
  """    
  Sorts a_list in from greatest volume to least volumne  
  """    
  for index in range(1, len(a_list)):        
    value = a_list[index]       
    pos = index - 1        
    while pos >= 0 and a_list[pos].volume() < value.volume():            
      a_list[pos + 1] = a_list[pos]            
      pos -= 1        
    a_list[pos + 1] = value