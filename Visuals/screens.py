import stddraw
from color import Color
from picture import Picture
from Jovan.player import Player

BLUE = Color(87, 89, 186)
YELLOW = Color(254, 204, 109)
WHITE = stddraw.WHITE
BACKGROUND = Picture("Cosmic_background.png")
TITLE = Picture("Luhan/cosmic_banner.png")
HEART = Picture("Jovan/Heart.png")



def show_start() -> None:
    stddraw.picture(BACKGROUND, 0.5, 0.7)
    stddraw.setPenColor(BLUE)
    stddraw.filledRectangle(0.2, 0.15, 0.6, 1)

    stddraw.picture(TITLE, 0.5, 1)

    stddraw.setPenColor(WHITE)
    stddraw.setFontSize(16)
    y_offset = 0.7
    stddraw.text(0.5, 0.10 + y_offset,"You are one of earth's elite spaceforce marines.")
    stddraw.text(0.5, 0.06 + y_offset, "The aliens from jupiter are")
    stddraw.text(0.5, 0.04 + y_offset, "trying to destroy the moon base!")
    stddraw.text(0.5, 0.00 + y_offset, "You must DESTROY ALL ALIENS to succeed.")

    stddraw.setFontSize(21)
    stddraw.text(0.5, 0.3, "Press <space> to begin")

    """ FOR A FUTURE MULTIPLAYER IMPLEMENTATION
    y_offset = 0.3
    stddraw.setFontSize(16)
    stddraw.text(0.5, 0.05 + y_offset, "Current Mode:")
    stddraw.setPenColor(YELLOW)
    stddraw.text(0.5, 0.00 + y_offset, "Singleplayer")
    """


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
        stddraw.show(700)
    return

def game_over():
    pass

def pause(Player):
    blue = Color(87, 89, 186) #this doesnt need to be here?
    stddraw.setPenColor(BLUE)
    stddraw.filledSquare(0.5,0.5, 0.4)

    title = Picture("Luhan/cosmic_banner.png")
    stddraw.picture(title, 0.5, 0.7)

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(0.5, 0.4, "Press <space> to Resume")
    
    #stddraw.text(0.5, 0.2, "Press <space> to Resume")
    # Francois Cooper | showing health and score on pause screen
    stddraw.text(0.5, 0.6, "Game Paused")
    stddraw.text(0.5, 0.2, f"Health: {Player.health}")
    stddraw.text(0.5, 0.1, f"Score: {Player.score}")
   


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

# Luhan | Scorebar function
def scoreBar(level:int, player1, player2=None ):
    # BACKGROUND
    stddraw.setPenColor(BLUE)
    stddraw.filledRectangle(0.0, 1.28, 1, 0.12)


    stddraw.setFontSize(18)
    stddraw.setPenColor(WHITE)
    stddraw.text(0.5, 1.36, "LEVEL")
    stddraw.setFontSize(30)
    stddraw.setPenColor(YELLOW)
    stddraw.text(0.5, 1.32, f"{level}")


    if player2 == None:
        # DISPLAYING HEALTH
        l_offset = 0.96
        for i in range(player1.health):
            stddraw.picture(HEART, (l_offset - (i*0.05)), 1.36, 0.1, 0.07)

        # DISPLAYING SCORE
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.setFontSize(30)
        stddraw.text(l_offset - (0.03 * (len(str(player1.score)) // 2)), 1.31, f"{player1.score}")
    else:
        l_offset = 0.96
        for i in range(player1.health):
            stddraw.picture(HEART, (l_offset - (i*0.05)), 1.36, 0.1, 0.07)

        stddraw.setPenColor(stddraw.WHITE)
        stddraw.setFontSize(30)
        stddraw.text(l_offset - (0.02 * (len(str(player1.score)) // 2)), 1.32, f"{player1.score}")

        l_offset = 0
        for i in range(player2.health):
            stddraw.picture(HEART, (l_offset + (i*0.05)), 1.36, 0.1, 0.07)

        # DISPLAYING SCORE
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.setFontSize(30)
        stddraw.text(l_offset + (0.02 * (len(str(player2.score)) // 2)), 1.32, f"{player2.score}")



def main() -> None:
    stddraw.setCanvasSize(w=750, h=1000)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1.4)

if __name__ == "__main__":  main()
