import stddraw, stdio, stdaudio
from instream import InStream
from outstream import OutStream
from color import Color
from picture import Picture

from Visuals.screens import show_start, count_down

BACKGROUND = Picture("Cosmic_background.png")

BLUE = Color(87, 89, 186)
YELLOW = Color(254, 204, 109)
RED = Color(150, 18, 25)
DARK_RED = Color(111, 31, 35)
WHITE = stddraw.WHITE
BLACK = stddraw.BLACK

# Luhan | Main gamestate handling done by Luhan
def win_screen(level: int, score: int, multiplayer: bool):
    stddraw.clear()
    stddraw.picture(BACKGROUND, 0.5, 0.7)
    stddraw.setPenColor(YELLOW)
    stddraw.filledRectangle(0.2, 0.15, 0.6, 1)

    y_offset = 1
    stddraw.setPenColor(BLUE)
    stddraw.setFontSize(42)
    stddraw.text(0.5, 0.1 + y_offset, "YOU WON!")

    stddraw.setFontSize(20)
    stddraw.text(0.5, 0.03 + y_offset, f"You reached level {level}")
    if multiplayer:
        stddraw.text(0.5, 0.00 + y_offset, f"Your combined score was {score}")
    else:
        stddraw.text(0.5, 0.00 + y_offset, f"Your score was {score}")

    y_offset = 0.4
    stddraw.setPenColor(BLACK)
    stddraw.setFontSize(22)
    stddraw.text(0.5, 0.08 + y_offset, "Would you like to save your score?")
    stddraw.setFontSize(30)
    stddraw.text(0.5, 0.00 + y_offset, "Y/N")
    stddraw.setFontSize(16)
    stddraw.text(0.5, -0.06 + y_offset, "writing your score will end your run.")

    y_offset = 0.25
    stddraw.setFontSize(18)
    stddraw.text(0.5, 0.04 + y_offset, "Press <esc>/<N> to go")
    stddraw.text(0.5, 0.01 + y_offset, "back to the start or")
    stddraw.text(0.5, -0.03 + y_offset, "<E> to continue playing endless mode!")

    y_offset = 0.8

    stddraw.setPenColor(BLACK)
    stddraw.filledRectangle(0.2, 0.5, 0.6, 0.35)
    stddraw.setPenColor(WHITE)
    stddraw.setFontSize(18)
    stddraw.setFontFamily("Courier")

    score_in = InStream("Highscores.txt")

    while score_in.hasNextLine():
        # Prepares the line from the file
        line = score_in.readLine()
        line = line.strip()

        # breaks it into parts and then interprets said parts
        parts = line.split(":")

        old_name = parts[0]
        old_score = parts[1]
        stddraw.text(0.3 + (len(old_name) * 0.016) / 2, y_offset, old_name)
        stddraw.text(0.7 - (len(old_score) * 0.02) / 2, y_offset, old_score)
        y_offset -= 0.028

    running = True
    while running:
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            # Luhan | Borrowed Jovan's implementation here'

            if key == "\x1b":
                running = False
                show_start()
            if key == "y":
                write_score_page(level, score, multiplayer)
                running = False
            if key == "e":
                running = False

        stddraw.show(33)
    count_down(3)
    return

# Luhan | Main gamestate handling done by Luhan
def game_over(level: int, score: int, multiplayer: bool):
    stddraw.clear()
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

    y_offset = 0.4
    stddraw.setPenColor(WHITE)
    stddraw.setFontSize(22)
    stddraw.text(0.5, 0.08 + y_offset, "Would you like to save your score?")
    stddraw.setFontSize(30)
    stddraw.text(0.5, 0.00 + y_offset, "Y/N")

    y_offset = 0.25
    stddraw.setFontSize(18)
    stddraw.text(0.5, 0.04 + y_offset, "Press <esc> to quit or")
    stddraw.text(0.5, 0.00 + y_offset, "<space>/<N> to go back to the start!")

    y_offset = 0.8

    stddraw.setPenColor(BLACK)
    stddraw.filledRectangle(0.2, 0.5, 0.6, 0.35)
    stddraw.setPenColor(WHITE)
    stddraw.setFontSize(18)
    stddraw.setFontFamily("Courier")

    score_in = InStream("Highscores.txt")

    while score_in.hasNextLine():
        # Prepares the line from the file
        line = score_in.readLine()
        line = line.strip()

        if not line:
            continue

        # breaks it into parts and then interprets said parts
        parts = line.split(":")

        old_name = parts[0]
        old_score = parts[1]
        stddraw.text(0.3 + (len(old_name) * 0.016) / 2, y_offset, old_name)
        stddraw.text(0.7 - (len(old_score) * 0.02) / 2, y_offset, old_score)
        y_offset -= 0.028

    running = True
    while running:
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            # Luhan | Borrowed Jovan's implementation here'

            if key == "\x1b":
                running = False
                return
            if key == "y":
                write_score_page(level, score, multiplayer)
                running = False
            if key == "n" or key == " ":
                running = False

        stddraw.show(33)

    show_start()

# Luhan | Highscores done by Luhan

def write_score_page(level: int, score: int, multiplayer: bool):

    player_name = ""

    running = True
    while running:
        stddraw.clear()
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

        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            if key == "\n" or key == "\r":
                running = False

            # 3. Check for the "Backspace" key to delete the last letter
            elif key == "\b":
                if len(player_name) > 0:
                    player_name = player_name[:-1]  # Slices off the last character
            else:
                player_name += key

        stddraw.setPenColor(stddraw.WHITE)
        stddraw.text(0.5, 0.6, "Please enter your name:")
        stddraw.text(0.5, 0.57, "Press <enter> to finish")

        # Draw the actual name the player is typing
        stddraw.text(0.5, 0.5, player_name)

        # 6. Show the frame (using a small delay like 20ms)
        stddraw.show(20)
    write_high_score(player_name, score)


# Luhan | Highscores done by Luhan
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
        parts = line.split(":")
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
