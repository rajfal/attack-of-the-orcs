
import random
from abc import ABCMeta, abstractmethod
from gameutils import Stos, weighted_random_selection

class AbstractGameUnit(metaclass=ABCMeta):
    """An Abstract base class for creating various game characters"""
    def __init__(self, name=''):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None 
        self.unit_type = None 

        # tracks whether enemy character earned combat experience
        # if True then enemy stats will be revealed to player
        self.has_combat_xp = False  

        # note to self: this is also available to all inheriting subclasses
        # shell text output styling
        self.styling = Stos()         

    @abstractmethod
    def info(self):
        """Information on the unit (MUST be overridden in subclasses)"""
        pass

    def attack(self, enemy):
        """The main logic to determine injured unit and amount of damage

        .. todo:: Check if enemy exists!
        """
        # slight advantage given to self
        injured_unit = weighted_random_selection(self, enemy, 57, 43)
        damage = random.randint(10, 15)  # inflict between 10 and 15 hitpoints
        injured_unit.health_meter = max(injured_unit.health_meter - damage, 0)

        war_cry_list = (
                    ['GOING ALL IN to shred some skin...', 'RAPIERS UP and bust some bone...', 
                    'ATTACK to slap some skull...', 'SAY, I THE KNIGHT, off with ya head ...']
                   ) 
        self.styling.use(random.choice(war_cry_list),"grey")

        self.show_health(end='  ')
        enemy.show_health(end='  ')
        # indicate that enemy character has been in combat
        enemy.has_combat_xp = True

    def heal(self, heal_by=2, full_healing=True):
        """Heal the unit replenishing all the hit points"""
        if self.health_meter == self.max_hp:
            return

        if full_healing:
            self.health_meter = self.max_hp
            self.styling.use("You are fully HEALED!", "green")
        else:
            # silently exit if exceeds max hit points 
            if self.health_meter + heal_by > self.max_hp:
                return

            self.health_meter += heal_by
            self.styling.use("You recover " + str(heal_by)  + " hitpoints!", "green")

        #if self.health_meter > self.max_hp:
        #    #raise GameUnitError("health_meter > max_hp!",101)
        #    raise HealthMeterException("health_meter > max_hp! {hm_e}")

        self.show_health(bold=True)

    def reset_health_meter(self):
        """Reset the `health_meter` (assign default hit points)"""
        self.health_meter = self.max_hp 

    def show_health(self, bold=False, end='\n'):
        """Show the remaining hit points of the player and the enemy"""
        # TODO: what if there is no enemy?
        msg = "Health: " + self.name + ": " + str(self.health_meter)

        if bold:
            self.styling.use(msg, "bold")
        else:
            print(msg, end=end)

