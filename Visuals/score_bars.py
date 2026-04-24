import stddraw
from color import Color
from picture import Picture

from Jovan.player import Player

HEART = Picture("Jovan/Heart.png")
BACKGROUND = Picture("Cosmic_background.png")

BLUE = Color(87, 89, 186)
YELLOW = Color(254, 204, 109)
RED = Color(150, 18, 25)
DARK_RED = Color(111, 31, 35)
WHITE = stddraw.WHITE
BLACK = stddraw.BLACK


# Luhan | Scorebar function
def score_bar(level: int, player1):
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

    # Health implementation by Jovan
    l_offset = 0.96
    for i in range(player1.health):
        stddraw.picture(HEART, (l_offset - (i * 0.05)), 1.36, 0.1, 0.07)

    # DISPLAYING SCORE
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(30)
    stddraw.text(
        l_offset - (0.03 * (len(str(player1.score)) // 2)), 1.31, f"{player1.score}"
    )

# Luhan | Scoring done by Luhan

def m_score_bar(level: int, health: int, p1_score: int, p2_score: int):
    # BACKGROUND
    stddraw.setPenColor(BLUE)
    stddraw.filledRectangle(0.0, 1.28, 1, 0.12)

    # SCORE TEXT
    stddraw.setFontSize(18)
    stddraw.setPenColor(WHITE)
    stddraw.text(0.08, 1.36, "LEVEL")
    stddraw.setFontSize(30)
    stddraw.setPenColor(YELLOW)
    stddraw.text(0.08, 1.32, f"{level}")

    l_offset = 0.96
    for i in range(health):
        stddraw.picture(HEART, (l_offset - (i * 0.05)), 1.36, 0.1, 0.07)

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(30)

    r_offset = 0.2
    # Player 2 Score (Left side, mirrored)
    # Implemented by Jovan
    stddraw.setPenColor(RED)
    stddraw.text(r_offset + (0.02 * (len(str(p1_score)) // 2)), 1.31, f"{p1_score}")

    # Player 1 Score (Right side under the health bar)
    stddraw.setPenColor(YELLOW)
    stddraw.text(l_offset - (0.02 * (len(str(p2_score)) // 2)), 1.31, f"{p2_score}")
