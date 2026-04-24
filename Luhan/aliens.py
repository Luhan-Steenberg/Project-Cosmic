import random, math

import stddraw # type: ignore
from picture import Picture # type: ignore

from dataclasses import dataclass
from collections import deque
from typing import List

from Francois.bullet import Bullet_Manager
from Francois.bullet import Explosion_Manager

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

        alien = Picture("Luhan/alien.png")

        # Draw a green circle for now, alien sprite later
        
        if not self.is_dead(): # Only draw if still alive
            stddraw.picture(alien, self.x, self.y, 0.07, 0.05)

    def move_down(self, step: float):
        """
        Move alien down by a step of 0.3
        """
        if step > 0:
            step = -step

        self.y += step

    def update_health(self, damage: int):
        self.health -= damage

    def is_dead(self) -> bool:
        """
        Returns true if the enemies health is below zero
        """
        return (self.health <= 0)
@dataclass
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
    _last_spawn: float
    alien_queue = deque()
    alien_scale: int = 3
    alien_health: int = 1
    alien_speed: float = 0.001
    spawn_timing: float = 3

    def update(self, c_time):
        """
        This function just draws the current alien queue to screen
        """
        if c_time - self._last_spawn >= self.spawn_timing:
            self.add_row(self.alien_scale, self.alien_health)
            self._last_spawn = c_time

        self.move_down(self.alien_speed)

        for i, row in enumerate(self.alien_queue):
            for j, alien in enumerate(row):
                alien.drawAlien()

         
    def add_row(self, n_aliens:int, alien_health:int):
        new_row = generate_aliens(n_aliens, alien_health)
        self.alien_queue.append(new_row)
    

    def remove_bottom_row(self):
        self.alien_queue.popleft()



    def check_collision(self, bullet_manager: Bullet_Manager, explosion_manager: Explosion_Manager, hitbox_radius: float) -> bool:

        for i, row in enumerate(self.alien_queue):
            for j, alien in enumerate(row):
                for bullet in bullet_manager.bullet_array:
                    distance = math.sqrt((alien.x - bullet.x) ** 2 + (alien.y - bullet.y) ** 2)
                    if distance < hitbox_radius:
                        bullet.active = False
                        alien.update_health(1)
                        explosion_manager.new_explosion(alien.x, alien.y) # Francois | trigger explosion
                        if alien.is_dead:
                            del self.alien_queue[i][j]
                            return True

        return False


    def move_down(self, step: float):
        for i, row in enumerate(self.alien_queue):
            for j, alien in enumerate(row):
                alien.move_down(step)


    def out_of_bounds(self) -> bool:
        # returning a bool for a "game over" condition
        """
        Meant to be called as a part of the "update function", which means it is taking in a row already
        """
        for i, row in enumerate(self.alien_queue):
            if row:
                if row[0].y <= 0.1:
                    self.remove_bottom_row()
                    return True
                else:
                    return False
        return False


def generate_aliens(n: int, health: int) -> List[Alien]:
    """
    Generates n aliens and puts them on one row. Note that there is a maximum of 10 aliens per row
    """

    start_y = 1.3
    left_offset = 0.05 # Ensures nothing goes off the left side of the page

    aliens_list = []

    while n > 10: # Just a guard against creating more aliens than is in a row.
        n = 10

    # Creates a list of n unique positions
    x = random.sample(range(0,10), n)

    for i in range(n):
        new_alien = Alien(x[i] * 0.1 + left_offset, start_y, health)
        aliens_list.append(new_alien)

    return aliens_list

