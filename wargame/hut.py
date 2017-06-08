
from gameutils import Stos
from factoryutils import UnitFactory , create_game_unit

class Hut:
    """Class to create hut object(s) in the game Attack of the Orcs"""

    factory = UnitFactory

    def __init__(self, number, occupant):
        #factory = UnitFactory()
        self.occupant = self.place_occupant(occupant)
        ## self.occupant = create_game_unit(occupant)  
        self.number = number
        self.is_acquired = False
        self.styling = Stos()  # shell text output styling

    def place_occupant(self, unit_type):
        """Place the occupant of unit_type in this hut"""
        occupant = self.factory.create_unit(unit_type)
        return occupant

    def acquire(self, new_occupant):
        """Update the occupant of this hut"""
        self.styling.use("GOOD JOB! You acquired Hut " + str(self.number) + ".\n","green")
        self.occupant = new_occupant
        self.is_acquired = True
         
    def get_occupant_type(self):
        """Return as string giving info on the hut occupant"""
        if self.is_acquired:
            occupant_type = 'ACQUIRED'
        ## elif self.occupant is None:
        ## elif self.occupant == 'empty':
        elif self.occupant.unit_type == 'empty':
            occupant_type = 'unoccupied'
        elif self.occupant.unit_type == 'friend':
            occupant_type = 'friend'
        else:
            #report remaining points for all enemies previously exposed to combat
            if self.occupant.has_combat_xp:
                return self.occupant.name + "{" + str(self.occupant.health_meter) + "}"
            else:
                occupant_type = 'enemy'
        return occupant_type 

    def get_occupant_name(self):
        """Return as string giving name of the hut occupant"""
        return self.occupant.name 

