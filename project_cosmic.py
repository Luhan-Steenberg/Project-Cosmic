import stddraw, stdio, sys, time
from Jovan.playertype import Player
from Jovan.player import PlayerDisplay, PlayerUpdate
from Luhan.aliens import Alien_Manager, Alien

def main() -> None: 
    stdio.writeln("Initialising Project Cosmic")
    p = Player(0.5, 0.1, 0.0, 5)

    # Luhan Steenberg | Canvas Setup
    stddraw.setCanvasSize(w=812, h=812)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1)



    # Luhan Steenberg | Main Program control loop
    x = 0
    
    # Setup Code for permanent variables
    frame_timing = 33

    # ALIEN SETUP
    alien_manager = Alien_Manager()
    last_enemy_spawn_time = time.time()
    spawn_interval = 5

    while True: 

        
        stddraw.clear(stddraw.GRAY)
        
        # Function-Calling code goes here

        current_time = time.time() # Used for enemy spawning

        if current_time - last_enemy_spawn_time >= spawn_interval: 
            alien_manager.addRow(5)
            last_enemy_spawn_time = current_time

        alien_manager.moveDown(0.005)

        alien_manager.update()
        alien_manager.outOfBounds() # This can later be used for the game-over stuff
        PlayerUpdate(p)
        PlayerDisplay(p)
        
        x += 0.01
        stddraw.filledCircle(x,0.5, 0.2)

        # Draw the next frame here

        stddraw.show(frame_timing)



if __name__ == "__main__": main()
