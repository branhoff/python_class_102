# Name: Brandon Hoffman
# Date: 2/3/2021
# Description: NeighbordPets class creates dictionary of key: pets, value dict pet_species and name_of owners
#              Methods add and delete pet, get owner, get_all_species, save_as_json, read_json

import json

class NeighborhoodPets:
    """
    NeighbordPets class creates dictionary of key: pets, value dict pet_species and name_of owners
    Methods add and delete pet, get owner, get_all_species, save_as_json, read_json
    """

    def __init__(self):
        """
        intializes empty dictionary to store JSON data
        """
        self._pet_dictionary = {}

    def add_pet(self, pet_name, pet_species, name_of_owner):
        """
        adds pet data to _pet_dictionary
        """
        self._pet_dictionary[pet_name] = {"species": pet_species, "owner": name_of_owner}

    def delete_pet(self, pet_name):
        """
        deletes pet from _pet_dictionary
        """
        self._pet_dictionary.pop(pet_name)

    def get_owner(self, pet_name):
        """
        gets owner with associated pet_name
        """
        return self._pet_dictionary[pet_name]['owner']

    def get_all_species(self):
        """
        pulls a set of all_species store in pet_dictionary
        """
        species_set = set()
        for pet_value in self._pet_dictionary.values():
            species_set.add(pet_value["species"])

        return species_set

    def save_as_json(self, file_name):
        """
        saves json file from _pet_dictionary
        """
        with open(file_name, 'w') as outfile:
            json.dump(self._pet_dictionary, outfile)

    def read_json(self, file_name):
        """
        reads json file into _pet_dictionary
        """
        with open(file_name, 'r') as infile:
            self._pet_dictionary = json.load(infile)


