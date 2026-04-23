import stddraw, stdio

from instream import InStream
from outstream import OutStream

from color import Color
from picture import Picture
from Jovan.player import Player


BLUE   = Color(87, 89, 186)
YELLOW = Color(254, 204, 109)
RED    = Color(150, 18, 25)
DARK_RED = Color(111, 31, 35)
WHITE  = stddraw.WHITE

#BACKGROUND = Picture("Cosmic_background.png")
#TITLE = Picture("Visuals/cosmic_banner.png")
#HEART = Picture("Jovan/Heart.png")

"""
MODULE DOC
show_start -- start screen
count_down -- used to leave start screen & pause screen
pause -- pause screen (duh)
score_bar  -- constant bar to track scores & whatnot
"""


def show_start() -> None:
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

    stddraw.picture(TITLE, 0.5, 0.7)

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
def score_bar(level:int, player1):
    # BACKGROUND
    stddraw.setPenColor(BLUE)
    stddraw.filledRectangle(0.0, 1.28, 1, 0.12)

    # SCORE TEXT
    stddraw.setFontSize(18)
    stddraw.setPenColor(WHITE)
    stddraw.text(0.5, 1.36, "LEVEL")
    stddraw.setFontSize(30)
    stddraw.setPenColor(YELLOW)
    stddraw.text(0.5, 1.32, f"{level}")

    l_offset = 0.96
    for i in range(player1.health):
        stddraw.picture(HEART, (l_offset - (i*0.05)), 1.36, 0.1, 0.07)

    # DISPLAYING SCORE
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(30)
    stddraw.text(l_offset - (0.03 * (len(str(player1.score)) // 2)), 1.31, f"{player1.score}")

""" MULTIPLAYER PLACEHOLDER
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
"""

def game_over(level, player) -> bool:
    stddraw.picture(BACKGROUND, 0.5, 0.7)
    stddraw.setPenColor(RED)
    stddraw.filledRectangle(0.2, 0.15, 0.6, 1)

    y_offset = 1
    stddraw.setPenColor(YELLOW)
    stddraw.setFontSize(42)
    stddraw.text(0.5, 0.1 + y_offset, "GAME OVER")

    stddraw.setFontSize(20)
    stddraw.text(0.5, 0.03 + y_offset, f"You reached level {level}")
    stddraw.text(0.5, 0.00 + y_offset, f"Your score was {player.score}")

    y_offset = 0.3
    stddraw.setPenColor(WHITE)
    stddraw.setFontSize(30)
    stddraw.text(0.5, 0.08 + y_offset, "Would you like to save your score?")
    stddraw.setFontSize(40)
    stddraw.text(0.5, 0.00 + y_offset, "Y/N")

    score = InStream("Highscores.txt")
    score_dict = [()]


    running = True
    while running:
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            # Luhan | Borrowed Jovan's implementation here'

            if key == '\x1b':
                running = False
                return False
            # if key == 'y':



        stddraw.show(33)
    return True

# Luhan
def write_high_score(name: str, score: int):
    score_in = InStream("Highscores.txt")

    score_array = []

    # Protection for the display to make sure no weird overflow happens
    # If you get a highscore of a million, go play another game.
    if score > 999999:
        score = 999999

    while score_in.hasNextLine():
        # Prepares the line from the file
        line = score_in.readLine()
        line = line.strip()

        # breaks it into parts and then interprets said parts
        parts = line.split(':')
        old_name = parts[0]
        old_score = int(parts[1])

        # Appends parts to an array as tuples to ensure they stay together
        score_array.append((old_name, old_score))

    # Adds the new score to the end of the array
    score_array.append((name[:6], score))

    # Sorts the array from highest to lowest
    # The lambda here is essentially a tiny function to say "Let the value x be the second element of the tuple", which is used as the key to sort by.
    # We then also only keep the top 10, because that's all that will be displayed. If you don't fall into the top ten, git gud
    score_array.sort(key=lambda x: x[1], reverse=True)
    score_array = score_array[:10]

    score_out = OutStream("Highscores.txt")
    for new_name, new_score in score_array:
        score_out.writeln(f"{new_name}: {new_score}")


def main() -> None:
    stddraw.setCanvasSize(w=750, h=1000)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1.4)

    write_high_score("Mew", 10110)

if __name__ == "__main__":  main()
