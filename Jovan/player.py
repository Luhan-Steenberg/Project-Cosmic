import sys, math
import stddraw, stdio # type: ignore

from picture import Picture # type: ignore

from Francois.bullet import BulletManager

# Jovan Fourie

class Player:
    # Jovan Fourie | Creating a player data type that tracks the players position, angle of shooter and health
    
    def __init__(self, x: float, y: float, angle: float, health: int):
        self.x = float(x)
        self.y = float(y)
        self.angle = float(angle)
        self.health = int(health)

        # Jovan fourie | Variables that gets changed to update the players movement

        self.vx = 0.0
        self.vangle = 0.0

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

        pic = Picture("Jovan/ship_final.png")

        stddraw.picture(pic, self.x, self.y, 0.1, 0.1)


    def update(self, bullet_manager: BulletManager, bullet_velocity: float):
        # Jovan Fourie | checks that the player has typed a key, and if so, stores the value of that key

        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            # Jovan Fourie | Changes the horizontal velocity of the player depending on what the player typed

            if key == 'd':
                self.vx = 0.05
            elif key == 'a':
                self.vx = -0.05
            elif key == 's':
                self.vx = 0.0

            # Jovan Fourie | Changes the angle velocity of the player depending on what the player typed

            elif key == 'q':
                self.vangle = -13
            elif key == 'e':
                self.vangle = 13
            elif key == 'w':
                self.vangle = 0.0

            if key == ' ':
                self.shoot(bullet_manager, bullet_velocity)


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

    def is_dead(self) -> bool:
        return (p.health <= 0)

    def shoot(self, bullet_manager: BulletManager, bullet_velocity):
        angle = 0.0
        if self.angle < 0:
           angle = maths.radian(abs(self.angle) + 90)
        else:
            angle = math.radians(90 - self.angle)

        bullet_manager.shoot(
                self.x + 0.06 * math.cos(angle),
                self.y + 0.06 * math.sin(angle),
                angle,
                bullet_velocity
                )




