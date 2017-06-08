
import random
from abstractgameunit import AbstractGameUnit

class Knight(AbstractGameUnit):
    """ Class that represents the game character 'Knight'

    The player instance in the game is a Knight instance. Other Knight
    instances are considered as 'friends' of the player and is
    indicated by the attribute `self.unit_type` .
    """
    def __init__(self, name=''):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = 'friend'              

    def info(self):
        """Print basic information about this character"""
        print("I  am a Knight!")

    def _inspect_hut_for_enemy(self, hut):
        """Have a look at the hut's occupant
           if unoccupied or friend THEN acquire hut
           otherwise gonna fight
        """
        self.styling.use("You tippytoe to open hut " + str(hut.number) + "...","bold")
        #print(hut.get_occupant_type())
        
        #if hut.occupant.unit_type == 'enemy':
        if hut.get_occupant_type() == 'enemy' or "{" in hut.get_occupant_type():  
            return True  # found enemy
 
        elif hut.get_occupant_type() == 'unoccupied':
            self.styling.use("...hut is unoccupied and yours for the taking.","bold")
        elif hut.get_occupant_type() == 'friend':
            self.styling.use("... and friendly forces welcome you to their humble abode!","bold")
           
        hut.acquire(self)
        self.heal()
                
        return False  # no enemy here  


    def acquire_hut(self, hut):
        """Fight the combat (command line) to acquire the hut
        """
 
        if self._inspect_hut_for_enemy(hut):
            continue_attack = 'y'
            self.enemy = hut.occupant
            #print(hut.get_occupant_name())
            #print(self.enemy.name) 

            self.styling.use("...and it's " + self.enemy.name + " eyeing you in the shadows!","bold")
            self.show_health(bold=False, end='\n ')
            #hut.occupant.show_health(bold=False, end=' ')
            while continue_attack:
                continue_attack = input(self.styling.out(".......continue attack? (y/n): ","grey"))
                try: 
                    assert(continue_attack in ('y','n'))
                except AssertionError as e:
                    #print("Invalid input, args: " + str(e.args))
                    print(self.styling.out(str("[You can't combat with '" + continue_attack + "']"),"purple"))
                    continue

                if continue_attack == 'n':
                    self.run_away()
                    break
                   
                self.attack(hut.occupant)

                if hut.occupant.health_meter <= 0:
                    print("")
                    hut.acquire(self)
                    break
                if self.health_meter <= 0:
                    print("")
                    break
             
 
    def run_away(self):
        """Abandon the battle.

        .. seealso:: `self.acquire_hut`
        """
        print(self.enemy.name)
        self.styling.use("YOU SLIP AWAY...to save your sorry bacon for another fray!" ,"yellow")
        #get healed by a few hitpoints only 
        self.heal(random.randint(4, 7),False)
        self.enemy = None

