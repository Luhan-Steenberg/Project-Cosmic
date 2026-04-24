import stddraw, stdio

from color import Color
from picture import Picture

BLUE   = Color(87, 89, 186)
YELLOW = Color(254, 204, 109)
RED    = Color(150, 18, 25)
DARK_RED = Color(111, 31, 35)
WHITE  = stddraw.WHITE
BLACK = stddraw.BLACK

BACKGROUND = Picture("Cosmic_background.png")
TITLE = Picture("Visuals/cosmic_banner.png")

"""
MODULE DOC
show_start -- start screen
count_down -- used to leave start screen & pause screen
pause -- pause screen (duh)
"""

def show_start() -> None:
    running = True
    multiplayer: bool = False
    while running:
        stddraw.picture(BACKGROUND, 0.5, 0.7)
        stddraw.setPenColor(BLUE)
        stddraw.filledRectangle(0.2, 0.15, 0.6, 1.2)

        stddraw.picture(TITLE, 0.5, 1.2)

        stddraw.setPenColor(WHITE)
        stddraw.setFontSize(16)
        y_offset = 0.95
        stddraw.text(0.5, 0.10 + y_offset,"You are one of earth's elite spaceforce marines.")
        stddraw.text(0.5, 0.06 + y_offset, "The aliens from jupiter are")
        stddraw.text(0.5, 0.04 + y_offset, "trying to destroy the moon base!")
        stddraw.text(0.5, 0.00 + y_offset, "You must DESTROY ALL ALIENS to succeed.")

        y_offset = 0.8
        if multiplayer:
            stddraw.text(0.5, 0.00 + y_offset, "Press S for Singleplayer")
            x_offset = 0.25
        else:
            stddraw.text(0.5, 0.00 + y_offset, "Press M for Multiplayer")
            x_offset = 0.32
        # Drawing the Controls
        y_offset = 0.45
        stddraw.setPenColor(WHITE)
        stddraw.filledRectangle(0.2, 0.0 + y_offset, 0.6, 0.3)

        stddraw.setPenColor(BLACK)
        stddraw.setFontSize(25)

        stddraw.text(0.5, 0.28 + y_offset, "Controls")

        # Drawing the Controls
        stddraw.setPenRadius(0.002)
        stddraw.line(0.2, 0.262 + y_offset, 0.8, 0.262 + y_offset)

        stddraw.setFontSize(21)
        y_offset = 0.5


        """
        | .000  | .100  | .175  | .250  |
        |  0.20 |
        |  0.15 |
        |  0.10 |
        """
        stddraw.setPenColor(RED)

        stddraw.text(x_offset + 0.100, y_offset + 0.18, "L")
        stddraw.text(x_offset + 0.175, y_offset + 0.18, "Stop")
        stddraw.text(x_offset + 0.250, y_offset + 0.18, "R")

        stddraw.text(0.000 + x_offset, y_offset + 0.13, "Rotate")
        stddraw.text(0.010 + x_offset, y_offset + 0.08, "Move")
        stddraw.text(0.005 + x_offset, y_offset + 0.01, "Shoot")

        stddraw.text(x_offset + 0.100, y_offset + 0.13, "Q")
        stddraw.text(x_offset + 0.175, y_offset + 0.13, "W")
        stddraw.text(x_offset + 0.250, y_offset + 0.13, "E")
        stddraw.text(x_offset + 0.100, y_offset + 0.08, "S")
        stddraw.text(x_offset + 0.175, y_offset + 0.08, "A")
        stddraw.text(x_offset + 0.250, y_offset + 0.08, "D")
        stddraw.text(x_offset + 0.175, y_offset + 0.01, "X")

        if multiplayer:
            x_offset = x_offset + 0.2

            stddraw.setPenColor(BLACK)
            stddraw.line(0.525, 0.5, 0.525, 0.7)

            stddraw.setPenColor(BLUE)

            stddraw.text(x_offset + 0.100, y_offset + 0.18, "L")
            stddraw.text(x_offset + 0.175, y_offset + 0.18, "Stop")
            stddraw.text(x_offset + 0.250, y_offset + 0.18, "R")

            stddraw.text(x_offset + 0.100, y_offset + 0.13, "U")
            stddraw.text(x_offset + 0.175, y_offset + 0.13, "I")
            stddraw.text(x_offset + 0.250, y_offset + 0.13, "O")
            stddraw.text(x_offset + 0.100, y_offset + 0.08, "J")
            stddraw.text(x_offset + 0.175, y_offset + 0.08, "K")
            stddraw.text(x_offset + 0.250, y_offset + 0.08, "L")
            stddraw.text(x_offset + 0.175, y_offset + 0.01, "M")




        stddraw.setPenColor(WHITE)
        stddraw.setFontSize(21)
        stddraw.text(0.5, 0.3, "Press <space> to begin")
        stddraw.text(0.5, 0.24, "Press <esc> to exit")

        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            # Luhan | Borrowed Jovan's implementation here'

            if key == ' ':
                running = False
            elif key == '\x1b':
                running = False
                return
            if key == 'm':
                multiplayer = True
            elif key == 's':
                multiplayer = False


        stddraw.show(33)

    count_down(3)

    import play_game as Play_Game
    Play_Game.play(multiplayer)

def pause():
    stddraw.setPenColor(BLUE)
    stddraw.filledSquare(0.5,0.5, 0.4)

    stddraw.picture(TITLE, 0.5, 0.7)

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(0.5, 0.4, "Press <space> to Resume")

    # Francois Cooper | showing health and score on pause screen
    stddraw.text(0.5, 0.6, "Game Paused")

    running = True
    while running:
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            # Luhan | Borrowed Jovan's implementation here'

            if key == ' ':
                running = False


        stddraw.show(33)

    count_down(3)
    return

def count_down(n:int) -> None:
    for i in range(n, 0, -1):
        stddraw.clear()
        stddraw.picture(BACKGROUND, 0.5, 0.7)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.setFontSize(40)
        stddraw.text(0.5, 1, "Starting in: ")
        stddraw.setPenColor(stddraw.RED)
        stddraw.setFontSize(60)
        stddraw.text(0.5, 0.9, f"{i}")
        stddraw.show(700)
    return


def main() -> None:
    stddraw.setCanvasSize(w=750, h=1000)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1.4)

if __name__ == "__main__":  main()
