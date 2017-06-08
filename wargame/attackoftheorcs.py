
import random
import os
from hut import Hut
from knight import Knight
from orcrider import OrcRider
from nonehere import NoneHere

from gameutils import Stos

##############################################################################
MAX_NO_OF_HUTS = 5
PLAYER_NAME = 'Sir Goatt'
##############################################################################

class AttackOfTheOrcs:
    """Main class to play Attack of The Orcs game""" 
    def __init__(self):
        self.huts = []
        self.player = None

        self.styling = Stos()  # shell text output styling  
        

    def get_occupants(self):
        """Return a list of occupant types for all huts.
        """
        return [x.get_occupant_type() for x in self.huts]

    def show_game_mission(self):
        """Print the game mission in the console"""
        self.styling.use("---------------------------------------------------------","cyan")
        self.styling.use("Attack of the p\'Orcs v3.0.0:","cyan")
        print("\n") 
        self.styling.use("Mission:","cyan")
        print("  1. Battle the enemies from p\'Orc tribe.")
        print("  2. Bring all " + str(MAX_NO_OF_HUTS) + " huts in New Hamton under your control")  
        print("\n")
        self.styling.use("TIP: 'enemy{n}' - let the enemy's remaining hit points \n\tguide your strategy","grey")
        self.styling.use("---------------------------------------------------------\n","cyan")

    def _process_user_choice(self):
        """Process the user input for choice of hut to enter"""
        verifying_choice = True
        idx = 0
        self.styling.use("Current occupants: \n","underline")
        print('...'.join(self.get_occupants()))
        while verifying_choice:
            user_choice = input("Choose a hut number to enter (1-" + str(MAX_NO_OF_HUTS) + "): ")            
            
            try:
                idx = int(user_choice)                 
                assert((idx-1) in range(MAX_NO_OF_HUTS))
            except (ValueError,AssertionError) as e:
                # catching ValueError for alpha input, and asserting that numerics fall within t defined range
                #print("Invalid input, args: " + str(e.args))
                self.styling.use(str("[You can't enter a hut with  '" + user_choice + "']"),"purple")
                continue
            #try: 
            if self.huts[idx-1].is_acquired:
                self.styling.use("This hut is already yours. Try again."
                      "\n<INFO: You can NOT be healed in an already acquired hut.>", "bold")
            else:
                verifying_choice = False
            #except IndexError:
            #    print(styling.out(str(">> You can't enter a hut with  '" + user_choice + "' <<"),"red"))
            #    continue
 
        return idx

    def create_huts(self):
        """Randomly occupy the huts with one of: friend, orc or empty """
        for i in range(MAX_NO_OF_HUTS):
            #sway choice towards more enemies
            choice_lst = ['orc', 'friend', 'nonehere', 'orc']
            self.huts.append(Hut(i+1, random.choice(choice_lst)))

    def setup_game_scenario(self):
        """Create player, huts and randomly pre-occupy the huts"""
        self.player = Knight(PLAYER_NAME)
        self.create_huts()  
        self.show_game_mission()
        self.player.show_health(bold=True)  

    def play(self):
        """Workhorse method to play the game.
        Controls the high level logic to play the game. This is called from
        the main program to begin the game execution.
        """
        #create Knight instance, huts and fill them with game character
        self.setup_game_scenario()

        acquired_hut_counter = 0

        while acquired_hut_counter < MAX_NO_OF_HUTS:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx-1])

            if self.player.health_meter <= 0:
                foe = self.huts[idx-1].get_occupant_name()
                self.styling.use("\n\t" + foe + " ensures your demise is legendary  :( \n\tShouldn't you trot back to cleaning horse stalls?\n","red")
                
                break

            if self.huts[idx-1].is_acquired:
                acquired_hut_counter += 1

        if acquired_hut_counter == MAX_NO_OF_HUTS:
            self.styling.use("\n\tCongratulations! YOU SCORE an epic victory!!!\n","green")

if __name__ == '__main__':

    os.system('clear') #play on a clean screen :)
 
    game = AttackOfTheOrcs()
    game.play()

