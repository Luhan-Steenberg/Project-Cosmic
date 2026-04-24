import random, math, time

import stddraw  # type: ignore
from picture import Picture  # type: ignore

from dataclasses import dataclass
from collections import deque
from typing import List

from Francois.bullet import Bullet_Manager
from Francois.bullet import Explosion_Manager


@dataclass
class Alien:
    x: float
    y: float
    health: int = 1  # allows the creation of high-health enemies
    hitbox_radius = 0.044
    points = 50

    def drawAlien(self):
        """
        Draws the alien to the screen
        Note that the internal parameters can be set
        """

        alien = Picture("Luhan/alien.png")

        # Draw a green circle for now, alien sprite later

        if not self.is_dead():  # Only draw if still alive
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
        return self.health <= 0


@dataclass
class Fat_Ouk:
    bullet_manager: Bullet_Manager
    x: int = 0.5
    y: int = 1.3
    step: float = 0.05
    health: int = 15
    hitbox_radius = 0.2
    points = 1000

    cooldown: float = 3
    _last_shot: float = 0.0

    def drawAlien(self):
        fat_ouk = Picture("Luhan/Fat_ouk.png")
        if not self.is_dead():  # Only draw if still alive
            stddraw.picture(fat_ouk, self.x, self.y)

    def move_down(self, step: float):  # Required by the Alien Manager
        if self.y >= 1.3:
            self.y -= self.step
        else:
            pass

    def attack(self, c_time: float):

        if c_time - self._last_shot >= self.cooldown:
            random_x = random.uniform(0.2, 0.8)
            self.bullet_manager.shoot(random_x - 0.150, self.y, math.radians(270), 0.01)
            self.bullet_manager.shoot(random_x - 0.075, self.y, math.radians(270), 0.01)
            self.bullet_manager.shoot(random_x, self.y, math.radians(270), 0.01)
            self.bullet_manager.shoot(random_x + 0.075, self.y, math.radians(270), 0.01)
            self.bullet_manager.shoot(random_x + 0.15, self.y, math.radians(270), 0.01)
            self._last_shot = c_time

    def update_health(self, damage: int):
        self.health -= damage

    def is_dead(self) -> bool:
        """
        Returns true if the enemies health is below zero
        """
        return self.health <= 0


@dataclass
class Alien_Manager:
    """
    The alien manager is essentially a set of aliens organized by rows.
    """

    last_spawn: float = 0
    level = 0
    alien_scale: int = 3
    alien_health: int = 1
    alien_speed: float = 0.001
    spawn_timing: float = 10
    alien_queue = deque()

    boss_active: bool = False
    boss_just_died: bool = False
    boss = None

    def update(self, c_time):
        """
        This function just draws the current alien queue to screen
        """
        if (c_time - self.last_spawn >= self.spawn_timing) and not self.boss_active:
            self.add_row()
            self.last_spawn = c_time
        elif self.boss_active:
            if self.boss.health <= 0:
                self.remove_bottom_row()
                self.boss_active = False
                self.boss_just_died = True
                self.last_spawn = c_time  # Reset timer for normal aliens
            else:
                # Pass c_time to the boss so he can check his personal stopwatch
                self.boss.attack(c_time)
        self.move_down(self.alien_speed)

        for i, row in enumerate(self.alien_queue):
            for j, alien in enumerate(row):
                alien.drawAlien()

    def add_row(self):
        new_row = generate_aliens(self.alien_scale, self.alien_health)
        self.alien_queue.append(new_row)

    def add_boss(self, bullet_manager: Bullet_Manager):
        if self.boss_active:
            return
        self.alien_queue.clear()
        self.boss_active = True
        self.boss = Fat_Ouk(bullet_manager)
        self.alien_queue.append([self.boss])

    def remove_bottom_row(self):
        self.alien_queue.popleft()

    def check_collision(
        self, bullet_manager: Bullet_Manager, explosion_manager: Explosion_Manager
    ) -> int:

        for i, row in enumerate(self.alien_queue):
            for j, alien in enumerate(row):
                for bullet in bullet_manager.bullet_array:
                    distance = math.sqrt(
                        (alien.x - bullet.x) ** 2 + (alien.y - bullet.y) ** 2
                    )
                    if distance < alien.hitbox_radius:
                        bullet.active = False
                        alien.update_health(1)
                        explosion_manager.new_explosion(
                            alien.x, alien.y
                        )  # Francois | trigger explosion
                        if alien.is_dead():
                            points_earned = alien.points
                            del self.alien_queue[i][j]
                            return points_earned
        return 0

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
    left_offset = 0.05  # Ensures nothing goes off the left side of the page

    aliens_list = []

    while n > 10:  # Just a guard against creating more aliens than is in a row.
        n = 10

    # Creates a list of n unique positions
    x = random.sample(range(0, 10), n)

    for i in range(n):
        new_alien = Alien(x[i] * 0.1 + left_offset, start_y, health)
        aliens_list.append(new_alien)

    return aliens_list
