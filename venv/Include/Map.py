# Map class file
# Author : Sayid Derder
# Date   : 26.01.2020

class Map:
    """
    name: int
    ressource_positions: list of tuple
    """

    def __init__(self, name: str, ressource_positions):

        self.name = name
        self.ressource_positions = ressource_positions

    # Get the name of the map, for future use
    def get_name(self):
        return self.name

    # Set the name of the map
    def set_name(self, name: str):
        self.name = name
        return