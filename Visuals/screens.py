import stddraw
from color import Color
from picture import Picture

def showStart() -> None:
    blue = Color(87, 89, 186)
    stddraw.setPenColor(blue)
    stddraw.filledSquare(0.5,0.5, 0.4)


    running = True
    while running:
        print("Loop is Running")
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            # Luhan | Borrowed Jovan's implementation here'

            if key == ' ':
                print("Recieved a space")
                running = False

        stddraw.show(1000)


    return


def startScreen():
    blue = Color(87, 89, 186)
    stddraw.setPenColor(blue)
    stddraw.filledSquare(0.5,0.5, 0.4)

    title = Picture("Luhan/cosmic_banner.png")
    stddraw.picture(title, 0.5, 0.75)

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(0.5, 0.4, "Press <space> to Resume")
    stddraw.text(0.5, 0.3, "Press <space> to Resume")

    stddraw.setFontSize(21)
    stddraw.text(0.5, 0.2, "Press <space> to Resume")



def pauseScreen():
    blue = Color(87, 89, 186)
    stddraw.setPenColor(blue)
    stddraw.filledSquare(0.5,0.5, 0.4)

    title = Picture("Luhan/cosmic_banner.png")
    stddraw.picture(title, 0.5, 0.75)

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(0.5, 0.4, "Press <space> to Resume")
    stddraw.text(0.5, 0.3, "Press <space> to Resume")

    stddraw.setFontSize(21)
    stddraw.text(0.5, 0.2, "Press <space> to Resume")



    
def main() -> None:
    stddraw.setCanvasSize(w=812, h=812)
    stddraw.clear()
    pauseScreen()
    stddraw.show()
    

if __name__ == "__main__": main()
