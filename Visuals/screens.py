import stddraw
from color import Color
from picture import Picture

BLUE = Color(87, 89, 186)
BACKGROUND = Picture("Cosmic_background.png")


def show_start() -> None:
    stddraw.picture(BACKGROUND, 0.5, 0.7)
    stddraw.setPenColor(BLUE)
    stddraw.filledRectangle(0.2, 0.15, 0.6, 1)


    # HOLD CONTROL UNTIL SPACE IS PRESSED
    running = True
    while running:
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            # Luhan | Borrowed Jovan's implementation here'

            if key == ' ':
                print("Recieved a space")
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
        stddraw.show(800)

    return


def pauseScreen():
    blue = Color(87, 89, 186)
    stddraw.setPenColor(BLUE)
    stddraw.filledSquare(0.5,0.5, 0.4)

    title = Picture("Luhan/cosmic_banner.png")
    stddraw.picture(title, 0.5, 0.7)

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(0.5, 0.4, "Press <space> to Resume")
    stddraw.text(0.5, 0.3, "Press <space> to Resume")

    stddraw.setFontSize(21)
    stddraw.text(0.5, 0.2, "Press <space> to Resume")

def scoreBar(player):
    pass


def main() -> None:
    stddraw.setCanvasSize(w=750, h=1000)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1.4)

    show_start()

if __name__ == "__main__":  main()
