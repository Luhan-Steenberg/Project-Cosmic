import sys, time, math
import stddraw, stdio # type: ignore
from Jovan.playertype import Player
from Jovan.player import PlayerDisplay, PlayerUpdate
from Luhan.aliens import Alien_Manager, Alien
from coordinate_visual import draw_coordinate_grid
from Francois.bullet import Bullet, Bullet_Manager, Explosion_Manager

def main() -> None: 
    stdio.writeln("Initialising Project Cosmic")
    p = Player(0.5, 0.1, 0.0, 5)

    # Luhan Steenberg | Canvas Setup
    stddraw.setCanvasSize(w=750, h=1000)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1.33)

    # This is just a helper to get a sense of scale
    # draw_coordinate_grid(1, 1.33, 0.1)

    # Luhan Steenberg | Main Program control loop
    x = 0
    
    # Setup Code for permanent variables
    frame_timing = 33

    # ALIEN SETUP
    alien_manager = Alien_Manager()
    last_enemy_spawn_time = time.time()

    # BULLET SETUP
    """
    Luhan | I quickly did this to test out of my collision system was working
    """
    bullet_manager = Bullet_Manager()
    explosion_manager = Explosion_Manager()
    last_bullet_spawn_time = time.time()

    while True: 
        # SETUP FOR EACH LOOP
        stddraw.clear(stddraw.GRAY)
        current_time = time.time()


        # ALIEN HANDLING
        ## Alien spawner
        if current_time - last_enemy_spawn_time >= 3.2: # spawns every 2 seconds
            alien_manager.add_row(5) # spawns 5 enemies
            last_enemy_spawn_time = current_time

        alien_manager.move_down(0.001)

        # Luhan | BULLET & COLLISION TESTING
        if current_time - last_bullet_spawn_time >= 1: # spawns every 1 seconds
            bullet_manager.shoot(0.5, 0.5, math.radians(100), 0.02)
            last_bullet_spawn_time = current_time

        alien_manager.check_collision(bullet_manager, 0.05)

        """
        Luhan | This is a bit of code I used for a "animation test"

        x += 0.01
        stddraw.filledCircle(x,0.5, 0.2)
        """

        # FRAME UPDATES
        PlayerUpdate(p)
        PlayerDisplay(p)
        alien_manager.update()
        bullet_manager.update()

        # GAME OVER STUFF
        alien_manager.out_of_bounds() # This can later be used for the game-over stuff



        stddraw.show(frame_timing)



if __name__ == "__main__": main()
