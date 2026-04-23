import stddraw
from color import Color
from picture import Picture

BLUE = Color(87, 89, 186)
YELLOW = Color(254, 204, 109)
BACKGROUND = Picture("Cosmic_background.png")
TITLE = Picture("Luhan/cosmic_banner.png")
HEART = Picture("Jovan/Heart.png")


def show_start() -> None:
    stddraw.picture(BACKGROUND, 0.5, 0.7)
    stddraw.setPenColor(BLUE)
    stddraw.filledRectangle(0.2, 0.15, 0.6, 1)

    stddraw.setFontSize(21)
    stddraw.text(0.5, 0.3, "Press <space> to begin")


    # HOLD CONTROL UNTIL SPACE IS PRESSED
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
        stddraw.show(500)

    return


def pauseScreen():
    blue = Color(87, 89, 186)
    stddraw.setPenColor(BLUE)
    stddraw.filledSquare(0.5,0.5, 0.4)

    title = Picture("Luhan/cosmic_banner.png")
    stddraw.picture(title, 0.5, 0.7)

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(0.5, 0.4, "Press <space> to Resume")

    stddraw.text(0.5, 0.2, "Press <space> to Resume")

# Luhan | Scorebar function
def scoreBar(player):
    # BACKGROUND
    stddraw.setPenColor(BLUE)
    stddraw.filledRectangle(0.0, 1.25, 1, 0.15)

    # DISPLAYING HEALTH
    l_offset = 0.96
    for i in range(player.health):
        stddraw.picture(HEART, (l_offset - (i*0.05)), 1.36, 0.1, 0.07)

    # DISPLAYING SCORE
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(30)
    stddraw.text(l_offset - (0.02 * (len(str(player.score)) // 2)), 1.32, f"{player.score}")



def main() -> None:
    stddraw.setCanvasSize(w=750, h=1000)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1.4)

if __name__ == "__main__":  main()
