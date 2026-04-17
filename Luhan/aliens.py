from dataclasses import dataclass
from typing import List
import stddraw, sys, stdio, random

@dataclass
class Alien:
    x: float
    y: float

    def drawAlien(self):
        """
        Draws the alien to the screen
        Note that the internal parameters can be set
        """

        alien_radius = 0.03 

        # Draw a green circle for now, alien sprite later

        stddraw.setPenColor(stddraw.GREEN)
        stddraw.filledCircle(self.x, self.y, alien_radius)

    def moveDown(self, step: int):
        """
        Move alien down by a step of 0.3
        """
        if step > 0: 
            step = -step



        self.y += step

def generateAliens(n: int) -> List[Alien]:
    """
    Generates n aliens and puts them on one row. Note that there is a maximum of 10 aliens per row
    """


    start_y = 0.9
    left_offset = 0.05

    aliens_list = []
    
    while n > 10: # Just a guard against creating more aliens than is in a row. 
        n = 10 

    # Creates a list of n unique positions 
    x = random.sample(range(0,10), n) 

    for i in range(n):
        new_alien = Alien(x[i] * 0.1 + left_offset, start_y)
        aliens_list.append(new_alien)

    return aliens_list

def main():
    allen = Alien(0, 0)
    allen.drawAlien()

    alien_list = generateAliens(10)
    for i, alien in enumerate(alien_list):
        # alien.moveAlienDown(random.randint(2,5))
        alien.moveDown(random.randint(2,5)*0.05)
        alien.drawAlien()




    stddraw.show()

if __name__ == "__main__": main()
        

