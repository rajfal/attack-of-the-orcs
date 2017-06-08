
import random

class Stos:
    """Class to create Shell Text Output Styling objects
    apply custom text style and print output to shell
    usage: 2 informal, 1 formal, 1 lambda style
    Stos().use("Attack of the Orcs v0.0.xx:","blue") #works
    p = Stos().use("Attack of the Orcs v0.0.xx:","blue") #works
    p = Stos()
    p.use("Attack of the Orcs v0.0.xx:", "blue") #works
    (lambda x,y: Stos().use(x,y))("Attack of the Orcs v0.0.xx:","green") #works
    """   
    def __init__(self):
        """method that will print out formatted text
        """
        self.shell_text_styles = ({'bold':'1', 'grey':'2', 'italic':'3', 'underline':'4',
                                   'black':'30', 'red':'31', 'green':'32', 'yellow':'33',
                                   'blue':'34', 'purple':'35', 'cyan':'36', 'white':'37'}
                                 )

    def use(self, msg='', style=''):
        """method to print out formatted text
        """
        print("\033[" + self.shell_text_styles[style]  + "m" +  msg  + "\033[0m")

    def out(self, msg='', style=''):
        """method to return formatted text as string
        """
        return "\033[" + self.shell_text_styles[style]  + "m" +  msg  + "\033[0m"

def weighted_random_selection(obj1, obj2, obj1_weight=5, obj2_weight=5):
    """Randomly select between two objects based on assigned 'weight'
       By default, equal chances  
       if the selection is obj1 then return it, else obj2
       usage: weighted_random_selection(self, enemy, 57, 43)
    """
    if random.choice(obj1_weight * [id(obj1)] + obj2_weight * [id(obj2)]) == id(obj1):
        return obj1
    return obj2
