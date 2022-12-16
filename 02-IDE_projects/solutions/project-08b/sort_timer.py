 # Author: Brandon Hoffman
 # Date: 2/24/2021
 # Description: Proejct compares the runtimes of bubble sort and insertion sort on randomly generated data

import random

from matplotlib import pyplot
from time import perf_counter


def sort_timer(func):
    """
    times how many seconds it takes the decorated function to run
    """
    def wrapper(args):
        """
        sort functions don't need to return anything, 
        the decorator's wrapper function returns the elapsed time
        """
        start = perf_counter() # start recorded by perf_counter
        result = func(args)
        end = perf_counter()   # stop recorded by perf_counter

        # appending in appropriate list by seeing function name if its bubble sort add the elapsed time in bubble time list else in insertion time list
        if func.__name__=="bubble_sort":
            bubble.append((end - start) )
        else:
            insertion.append((end - start))
        return result
    return wrapper

@sort_timer
def bubble_sort(a_list):    
  """    
  Sorts a_list in ascending order    
  """    
  for pass_num in range(len(a_list) - 1):        
    for index in range(len(a_list) - 1 - pass_num):            
      if a_list[index] > a_list[index + 1]:                
        temp = a_list[index]                
        a_list[index] = a_list[index + 1]                
        a_list[index + 1] = temp

@sort_timer
def insertion_sort(a_list):    
  """    
  Sorts a_list in ascending order    
  """    
  for index in range(1, len(a_list)):        
    value = a_list[index]        
    pos = index - 1        
    while pos >= 0 and a_list[pos] > value:            
      a_list[pos + 1] = a_list[pos]            
      pos -= 1        
    a_list[pos + 1] = value

# 2 arrays which stores the time for each testing values for each sorting algorithm
bubble=[]
insertion=[]

def compare(function1,function2):
    """
    takes two sorting functions and compares runtime
    plots results in matplot graph
    """
    testing_values=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
    for t in testing_values:
        list1 = []
        # genrate list of random numbers
        for _i in range(1,t+1):
            list1.append(random.randint(1, 10000))

        # copying list1 into list2
        list2=list(list1)

        function1(list1)
        function2(list2)

    pyplot.plot(testing_values, bubble, 'ro--', linewidth=2)       # red for bubblesort
    pyplot.plot(testing_values, insertion, 'go--', linewidth=2)    # green for insertion sort
    pyplot.xlabel("# of data points")
    pyplot.ylabel("seconds")
    pyplot.show()

if __name__ == "__main__":
    compare(bubble_sort,insertion_sort)
