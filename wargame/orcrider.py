
import random
from abstractgameunit import AbstractGameUnit
 
class OrcRider(AbstractGameUnit):
    """Class that represents the game character Orc Rider"""
    def __init__(self, name=''):
        orc_name = self._select_name()
        super().__init__(name = orc_name)
        # allow for different sized orcs
        self.max_hp = random.randint(15, 35)
        self.health_meter = self.max_hp
        self.unit_type = 'enemy'
        self.hut_number = 0

    def info(self):
        """Print basic information about this character"""
        print("Grrrr..I am an Orc Wolf Rider. Don't mess with me.")

    def _select_name(self):
        """choose a random name for this character"""
        #make Orcs more personal
        name = random.choice(['Piglet','Trotter','gRinder','Bakons','Fathock',
                              'Snouto','Squeela','SirHog','Pigrump','Porkstu',
                              'Hampit','Crackle']
                            )  
        return name       
