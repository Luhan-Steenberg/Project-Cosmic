import sys
import math
import stddraw
from picture import Picture
import stdio
from playertype import Player

def PlayerUpdate(p: Player) -> None:

    # checks that the player has typed a key, and if so, stores the value of that key

    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()

        # Changes the horizontal velocity of the player depending on what the player typed 

        if key == 'd':
            p.vx = 0.05
        elif key == 'a':
            p.vx = -0.05
        elif key == 's':
            p.vx = 0.0

        # Changes the angle velocity of the player depending on what the player typed

        elif key == 'q':
            p.vangle = -13
        elif key == 'e':
            p.vangle = 13
        elif key == 'w':
            p.vangle = 0.0

    # Updates the shooter and players position depending on the velocity
    p.x += p.vx
    p.angle += p.vangle

    # Boundaries of the player
    if p.x < 0.05:
        p.x = 0.05
    if p.x > 0.95:
        p.x = 0.95

    if p.angle < -60:
        p.angle = -60
    if p.angle > 60:
        p.angle = 60


def PlayerDisplay(p: Player) -> None:


    a = math.radians(p.angle)

    # Direction line (0° = UP)
    # Calculation to determin the angle and position of the shooter(line)

    x2 = p.x + 0.06 * math.sin(a)
    y2 = p.y + 0.06 * math.cos(a)

    stddraw.setPenColor(stddraw.RED)
    stddraw.line(p.x, p.y, x2, y2)

    # Uploads an image to show the player at said position

    pic = Picture("ship_final.png")

    stddraw.picture(pic, p.x, p.y, 0.1, 0.1)

def UpdatePlayerHealth(p : Player) -> None:
    p.health = p.health - 1     # updates the player health if it takes damage

def PlayerDead(p : Player) -> bool:

    # Checks if the player is dead depending on their health

    if p.health <= 0:
        return True
    else:
        return False
