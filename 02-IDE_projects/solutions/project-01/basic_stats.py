# Author: Brandon Hoffman
# Date: 1/1/2021
# Description: contains a Person Class to take name and age
#              then a function called basic stats to return a tuple of
#              mean, median, and mode of a list of "Person" object ages

from statistics import mean, median, mode

class Person:
    """
    Contains two private data members representing someone's name and age
    and a get_age method
    """

    def __init__(self, name, age):
        """
        initializes a person objects name and age
        """
        self._name = name
        self._age = age

    def get_age(self):
        """
        returns the private data member _age
        """
        return self._age


def basic_stats(person_list):
    """
    creates a list of ages from a list of person objects then calculates
    mean, median, and mode from the statistics module
    """
    age_list = [i.get_age() for i in person_list]
    
    return (mean(age_list), median(age_list), mode(age_list))