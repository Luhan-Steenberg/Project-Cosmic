import stddraw, stdio, sys
from playertype import Player
from player import PlayerDisplay, PlayerUpdate

def main() -> None: 
    stdio.writeln("Initialising Project Cosmic")
    p = Player(0.5, 0.1, 0.0, 5)

    # Luhan Steenberg | Canvas Setup
    stddraw.setCanvasSize(w=812, h=812)



    # Luhan Steenberg | Main Program control loop
    
    while True: 
        # Function-Calling code goes here
        
        stddraw.clear(stddraw.GRAY)

        PlayerUpdate(p)
        PlayerDisplay(p)

        
        # Draw the next frame here

        stddraw.show()



if __name__ == "__main__": main()
