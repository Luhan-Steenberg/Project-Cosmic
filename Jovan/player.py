import sys
import math
import stddraw
import stdio
from playertype import Player

def PlayerUpdate(p: Player) -> None:
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()

        # Movement
        if key == 'd':
            p.vx = 0.05
        elif key == 'a':
            p.vx = -0.05
        elif key == 's':
            p.vx = 0.0

        # Rotation
        elif key == 'q':
            p.vangle = 0.05
        elif key == 'e':
            p.vangle = -0.05
        elif key == 'w':
            p.vangle = 0.0

    # Update every frame
    p.x += p.vx
    p.angle += p.vangle

    # Boundaries
    if p.x < 0.05:
        p.x = 0.05
    if p.x > 0.95:
        p.x = 0.95


def PlayerDisplay(p: Player) -> None:
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledCircle(p.x, p.y, 0.05)
