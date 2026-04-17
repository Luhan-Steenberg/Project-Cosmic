import stddraw, stdio, sys
from Jovan.playertype import Player
from Jovan.player import PlayerDisplay, PlayerUpdate
from Luhan.aliens import Alien, generateAliens

def main() -> None: 
    stdio.writeln("Initialising Project Cosmic")
    p = Player(0.5, 0.1, 0.0, 5)

    # Luhan Steenberg | Canvas Setup
    stddraw.setCanvasSize(w=812, h=812)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1)



    # Luhan Steenberg | Main Program control loop
    
    while True: 
        # Function-Calling code goes here
        
        stddraw.clear(stddraw.GRAY)

        aliens_array = []
        aliens_array.append(generateAliens(5)) # generates 5 aliens in a row:w

        for i, row in enumerate(aliens_array):
            for i, aliens in enumerate(row):
                aliens.drawAlien() # Draws all aliens in their current position
                aliens.moveDown(0.4) # Puts their next move into the frame buffer

        PlayerUpdate(p)
        PlayerDisplay(p)

        
        # Draw the next frame here

        stddraw.show()



if __name__ == "__main__": main()
