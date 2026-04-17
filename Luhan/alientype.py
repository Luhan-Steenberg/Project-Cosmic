from dataclasses import dataclass
from collections import deque
from typing import List
from Luhan.aliens import *

@dataclass
class Alien:
    x: float
    y: float
    health: int = 1 # allows the creation of high-health enemies

    def drawAlien(self):
        """
        Draws the alien to the screen
        Note that the internal parameters can be set
        """

        alien_radius = 0.03

        # Draw a green circle for now, alien sprite later
        
        if not self.isDead(): # Only draw if still alive
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.filledCircle(self.x, self.y, alien_radius)

    def moveDown(self, step: float):
        """
        Move alien down by a step of 0.3
        """
        if step > 0:
            step = -step

        self.y += step

    def updateHealth(self, damage: int):
        self.health -= damage

    def isDead(self) -> bool:
        """
        Returns true if the enemies health is below zero
        """
        return (self.health <= 0)

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
        self.alien_queue = deque()
    
    def update(self):
        """
        This function just draws the current alien queue to screen
        """
        for i, row in enumerate(self.alien_queue):
            for j, alien in enumerate(row):
                alien.drawAlien()

         

    def addRow(self, n_aliens:int):
        new_row = generateAliens(n_aliens)
        self.alien_queue.append(new_row)
    
    def removeBottomRow(self):
        self.alien_queue.popleft()

    def moveDown(self, step: float):
        for i, row in enumerate(self.alien_queue):
            for j, alien in enumerate(row):
                alien.moveDown(step)


    def outOfBounds(self) -> bool: # returning a bool for a "game over" condition
        """
        Meant to be called as a part of the "update function", which means it is taking in a row already
        """
        for i, row in enumerate(self.alien_queue):
            if row[1].y <= 0.2:
                self.removeBottomRow()
                return True
            else: 
                return False

