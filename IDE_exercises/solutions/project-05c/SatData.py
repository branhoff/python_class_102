# Author: Brandon Hoffman
# Date: 2/3/2021
# Description: takes SAT data in JSON and writes output csv file with match dbn items

import json
class SatData:
    """
    Takes in SAT json data and writes output csv file based on matching dbn items
    """

    def __init__(self):
        """
        inits sat.json
        """
        with open("sat.json", 'r') as infile:
            self._sat_dict = json.load(infile)

    def get_data(self):
        """
        gets data filed in sat.json file from _sat_dict
        """
        return self._sat_dict["data"]
    
    def save_as_csv(self, dbns):
        """
        takes in list of dbns
        if dbn matches dbn in json file will write to output.csv file
        """
        with open("output.csv", 'w') as outfile:
            headers = ",".join(["DBN", "School Name", "Number of Test Takers", "Critical Reading Mean", "Mathematics Mean", "Writing Mean"])
            outfile.write(headers + "\n")
            
            for row in self.get_data():
                if row[8] in dbns:
                    line = ",".join([row[8], row[9], row[10], row[11], row[12], row[13]])
                    outfile.write(line + "\n")


        
