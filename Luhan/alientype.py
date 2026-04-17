from dataclasses import dataclass
from typing import List
from Luhan.aliens import *

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

class Alien_Manager:
    """
    The alien manager is essentially a set of aliens organized by rows. 
    This manager is currently meant to work through the set of all aliens and handle: 
    - Adding a row to the top
    - Removing a row from the bottom
    - Moving a row down by some interval

    Future functionality: 
    - Alien health tracking

    """

    def __init__(self):
        self.alien_array = []

    def addRow(self, new_row: List[Alien]):
        self.alien_array.append(new_row)

