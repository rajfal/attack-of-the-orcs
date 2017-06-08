
import random
from abstractgameunit import AbstractGameUnit
 
class NoneHere(AbstractGameUnit):
    """Class that represents the game character NoneHere that fills a hut making it empty"""
    def __init__(self, name=''):
        super().__init__(name = name)
        self.max_hp = 0
        self.health_meter = self.max_hp
        self.unit_type = 'empty'
        self.hut_number = 0

    def info(self):
        """Print basic information about this character"""
        print("Shh..I am just a vapour filling empty spaces.")


