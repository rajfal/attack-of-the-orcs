
from knight import Knight
from orcrider import OrcRider
from nonehere import NoneHere

class UnitFactory:
    """A factory class to create game units.

    This is an example that shows how we can use Python classes (which are
    first-class objects) and a class method to represent a simple factory. In
    this example, the client does not instantiates factory. See the book
    mentioned at the top of this file for detailed explanation.

    :cvar units_dict: Python dictionary created as a class variable. This
            dictionary holds names (types) of the game units as its keys and
            the corresponding values are the concrete classes representing the
            game character.
    .. seealso:: `Kingdom` class and various classes like `ElfRider`, `Knight`
    """
    units_dict = {
        'friend': Knight,
        'orc': OrcRider,
        'nonehere' : NoneHere
    }

    @classmethod
    def create_unit(cls, unit_type):
        """Return an instance of a game unit.

        This is a class method and it uses the class variable unit_dict to
        create and return an instance of a game unit class (e.g. ElfRider(),
        Knight(), Dwarf() and so on.

        :arg unit_type: A string representing the unit type (e.g. 'elfrider')
        :return:Instance of a game unit.
        """
        key = unit_type.lower()
        return cls.units_dict.get(key)()

def create_game_unit(character_type=''):
    """instantiate character unit and return it as object
       usage: create_game_unit('orc')
       this was used prior to factory pattern class above
    """
    
    if character_type == 'orc':                  
       game_unit = OrcRider()
    elif character_type == 'friend':
       game_unit = Knight()
    else:
       game_unit = NoneHere() #'empty' # None

    return game_unit
