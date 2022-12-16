# Author: Brandon Hoffman
# Date: 2/3/2021
# Description: NobelData class iterates through nobels.json and returns list of prize winners that match
#              year and category

import json

class NobelData:
    """
    NobelData class iterates through nobels.json and returns list of prize winners that ma
    year and category
    """
    
    def __init__(self):
        """
        inits nobels.json file as _prize_dict
        """
        with open("nobels.json", 'r') as infile:
            self._prize_dict = json.load(infile)

        self._first_index = None
        self._second_index = None

    def get_prize_dict(self):
        """
        returns private variable prize_dict
        """
        return self._prize_dict

    def get_prize_list(self):
        """
        returns the list of prizes from prize_dict
        """
        return self._prize_dict["prizes"]

    def get_first_index(self):
        """

        """
        return self._first_index

    def get_second_index(self):
        """

        """
        return self._second_index

    def set_first_index(self, index):
        """

        """
        self._first_index = index

    def set_second_index(self, index):
        """

        """
        self._second_index = index
        

    def search_nobel(self, year, category):
        """
        takes year and category
        returns a sorted list: english dict order of the surnames of the winners
        in that category for that year
        """
        output = []
        for prize in self.get_prize_list():
            try:
                if prize['year'] == year:
                    if prize['category'] == category:
                        print(prize)
                        for laureate in prize["laureates"]:
                            output.append(laureate['surname'])
            except KeyError:
                pass

        output.sort()

        return output


    def _binary_search(self, a_list, target):    
        """    
        Searches a_list for an occurrence of target    
        If found, returns the index of its position in the list    
        If not found, returns -1, indicating the target value isn't in the list    
        """
        first, last = self._assign_binary_search_range()

        while first <= last:
            middle = (first + last) // 2
            middle_val = a_list[middle]['year']
            print(middle_val)
            if middle_val == target:
                before_val = a_list[middle - 1]['year']
                after_val = a_list[middle + 1]['year']

                if after_val == target:
                    pass

                if before_val == target:
                    pass

                if after_val != target:
                    self.set_second_index(middle)
                if before_val != target:
                    self.set_first_index(middle)

            if middle_val < target:
                last = middle - 1
            elif middle_val > target:
                first = middle + 1
        return -1

    def _middle_val_equiv_conditionals(self):
        if self._first_index == None:
            pass

        if self._second_index == None:
            pass

    def _assign_binary_search_range(self):
        """

        """
        if self.get_first_index() == None and self.get_second_index() == None:
            first = 0 # index for binary search
            last = len(self.get_prize_list()) - 1
        elif self.get_first_index() == None:
            first = 0
            last = self.get_second_index() - 1
        elif self._second_index == None:
            first = self.get_first_index() + 1
            last = len(self.get_prize_list()) - 1

        return (first, last)

def main():
    """

    """
    nd = NobelData()
    print(nd.search_nobel("2020", "chemistry"))


if __name__ == "__main__":
    main()