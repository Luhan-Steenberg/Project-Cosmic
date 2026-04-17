import stddraw, stdio, sys
from Jovan.playertype import Player
from Jovan.player import PlayerDisplay, PlayerUpdate
from Luhan.alientype import Alien_Manager, Alien

def main() -> None: 
    stdio.writeln("Initialising Project Cosmic")
    p = Player(0.5, 0.1, 0.0, 5)

    # Luhan Steenberg | Canvas Setup
    stddraw.setCanvasSize(w=812, h=812)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1)



    # Luhan Steenberg | Main Program control loop
    x = 0
    frame_timing = 33
    while True: 
        # Function-Calling code goes here
        
        stddraw.clear(stddraw.GRAY)
        
        alien_manager = Alien_Manager()

        PlayerUpdate(p)
        PlayerDisplay(p)
        
        x += 0.01
        stddraw.filledCircle(x,0.5, 0.2)

        # Draw the next frame here

        stddraw.show(frame_timing)



if __name__ == "__main__": main()
