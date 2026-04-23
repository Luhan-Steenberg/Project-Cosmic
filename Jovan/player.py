import sys, math, time
# import winsound
import stddraw, stdio, stdaudio # type: ignore
from dataclasses import dataclass, field

from picture import Picture # type: ignore

from Francois.bullet import BulletManager
from Visuals.screens import pause

# Jovan Fourie

KEY_SET_1 = [['q', 'w', 'e'], ['a', 's', 'd'], ['x']]
KEY_SET_2 = [['u', 'i', 'o'], ['j', 'k', 'l'], ['m']]


@dataclass
class Player:
    # Position
    x: float = 0.5
    y: float = 0.1
    angle: float = 0

    # Scoring
    health: float = 6
    score: int = 0

    # Movement
    vx: float = field(default=0.0, init=False)
    vangle: float = field(default = 0.0, init = False)


    # Shooting
    _last_shot: float = field(default = time.time(), init = False)
    _bullet_cooldown: float = field(default = 0.3, init = False)

    _sprite = Picture("Jovan/ship_final.png")

    # Luhan | Multiplayer
    multiplayer
    key_set = 1 # must be zero or one

    # This will select the correct key-set
    def __post_init__(self):
        if self.key_set == 1:
            self.key_set = KEY_SET_1
        elif self.key_set == 2:
            self.key_set = KEY_SET_2
        else:
            print("Did not choose a valid keyset")

    # Jovan Fourie | gets the actual angle from the horizontal axes to shoot the bullet

    def display(self):
        a = math.radians(self.angle)

        # Jovan Fourie | Direction line (0° = UP)
        # Jovan Fourie | alculation to determin the angle and position of the shooter(line)

        x2 = self.x + 0.06 * math.sin(a)
        y2 = self.y + 0.06 * math.cos(a)

        stddraw.setPenColor(stddraw.RED)
        stddraw.line(self.x, self.y, x2, y2)

        # Jovan Fourie | Uploads an image to show the player at said position

        stddraw.picture(self._sprite, self.x, self.y, 0.1, 0.1)

    def update(self, bullet_manager: BulletManager, bullet_velocity: float):
        # Jovan Fourie | checks that the player has typed a key, and if so, stores the value of that key

        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            # Jovan Fourie | Changes the horizontal velocity of the player depending on what the player typed

            if key == 'd':
                self.vx = 0.01
            elif key == 'a':
                self.vx = -0.01
            elif key == 's':
                self.vx = 0.0

            # Jovan Fourie | Changes the angle velocity of the player depending on what the player typed

            elif key == 'q':
                self.vangle = -3
            elif key == 'e':
                self.vangle = 3
            elif key == 'w':
                self.vangle = 0.0

            # Luhan | Pushes a bullet into the bullet manager with the current parameters
            if key == ' ':
                self.shoot(bullet_manager, bullet_velocity)

            if key == '\x1b':
                print("Triggered Pause")
                screens.pause(Player)


        # Jovan Fourie | Updates the shooter and players position depending on the velocity
        self.x += self.vx
        self.angle += self.vangle

        # Jovan Fourie | Boundaries of the player
        if self.x < 0.05:
            self.x = 0.05
        if self.x > 0.95:
            self.x = 0.95

        if self.angle < -60:
            self.angle = -60
        if self.angle > 60:
            self.angle = 60

        self.display()

    def update_health(self, damage: int):
        self.health -= damage
        # winsound.PlaySound("Jovan/Hit_Sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    def is_dead(self) -> bool:
        return (self.health <= 0)

    def shoot(self, bullet_manager: BulletManager, bullet_velocity: float):
        angle = 0.0
        current_time = time.time()
        if self.angle < 0:
           angle = math.radians(abs(self.angle) + 90)
        else:
            angle = math.radians(90 - self.angle)

        if current_time - self._last_shot > self._bullet_cooldown:
            bullet_manager.shoot(
                self.x + 0.06 * math.cos(angle),
                self.y + 0.06 * math.sin(angle),
                angle,
                bullet_velocity
                )
            self._last_shot = current_time

