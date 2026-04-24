import stddraw, stdio, stdaudio
from instream import InStream
from outstream import OutStream
from color import Color
from picture import Picture


BACKGROUND = Picture("Cosmic_background.png")


def game_over(level: int, score: int, multiplayer: bool) -> bool:
    stddraw.picture(BACKGROUND, 0.5, 0.7)
    stddraw.setPenColor(RED)
    stddraw.filledRectangle(0.2, 0.15, 0.6, 1)

    y_offset = 1
    stddraw.setPenColor(YELLOW)
    stddraw.setFontSize(42)
    stddraw.text(0.5, 0.1 + y_offset, "GAME OVER")

    stddraw.setFontSize(20)
    stddraw.text(0.5, 0.03 + y_offset, f"You reached level {level}")
    if multiplayer:
        stddraw.text(0.5, 0.00 + y_offset, f"Your combined score was {score}")
    else:
        stddraw.text(0.5, 0.00 + y_offset, f"Your score was {score}")

    y_offset = 0.3
    stddraw.setPenColor(WHITE)
    stddraw.setFontSize(30)
    stddraw.text(0.5, 0.08 + y_offset, "Would you like to save your score?")
    stddraw.setFontSize(40)
    stddraw.text(0.5, 0.00 + y_offset, "Y/N")



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
