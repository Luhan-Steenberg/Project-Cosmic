import sys, time, math
import stddraw, stdio # type: ignore

from picture import Picture

from Jovan.player import Player
from Luhan.aliens import Alien_Manager, Alien
import Visuals.screens as screens
from Helpers.coordinate_visual import draw_coordinate_grid
from Francois.bullet import Bullet, BulletManager, Explosion_Manager

BACKGROUND = Picture("Cosmic_background.png")

def playgame(
    frame_timing: int,
    alien_manager: Alien_Manager,
    bullet_manger: Bullet_Manager,
    Explosion_Manager: Explosion_Manager,
    player: Player
    )

def main() -> None: 
    stdio.writeln("Initialising Project Cosmic")

    # Luhan Steenberg | Canvas Setup
    stddraw.setCanvasSize(w=750, h=1000)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1.4)

    # START SCREEN IMPLEMENTATION
    screens.show_start()

    # Setup Code for permanent variables
    frame_timing = 33
    level = 1

    # ALIEN SETUP
    alien_manager = Alien_Manager()
    alien_health = 1
    alien_scale = 3
    alien_speed = 0.001
    last_enemy_spawn_time = time.time()

    # BULLET SETUP
    """
    Luhan | I quickly did this to test out of my collision system was working
    """
    bullet_manager = BulletManager()
    explosion_manager = Explosion_Manager()
    # last_bullet_spawn_time = time.time()

    # SINGLE PLAYER SETUP
    player = Player(0.5, 0.1, 0.0, 0, 900) # all the variables are handled by the dataclass defaults
    bullet_velocity = 0.02


    playing = True
    while playing:
        # SETUP FOR EACH LOOP
        stddraw.clear(stddraw.GRAY)
        current_time = time.time()


        if not player.is_dead():
            # ALIEN HANDLING

            ## Alien spawner
            if current_time - last_enemy_spawn_time >= 3.2 / (level // 2 +1): # spawns every 3.2 seconds
                num_aliens = (level // 5 + 1) * alien_scale
                alien_manager.add_row(
                    num_aliens,
                    alien_health
                    ) # spawns 5 enemies

                if num_aliens >= 10:
                    alien_health = alien_health + level // 10

                last_enemy_spawn_time = current_time

            alien_manager.move_down(alien_speed * (level // 2 + 1))

            # FRAME UPDATES
            if alien_manager.out_of_bounds():
                player.update_health(1)
            if alien_manager.check_collision(bullet_manager, 0.05):
                player.score += 10
            if player.score >= 500 * level:
                level += 1

        stddraw.picture(BACKGROUND, 0.5, 0.7)
        player.update(bullet_manager, bullet_velocity)
        alien_manager.update()
        bullet_manager.update()

            # GAME OVER STUFF

            screens.score_bar(level, player)
        else: ## If the player is dead, show the game over screen and offer to save their score
            screens.game_over(level, player)

        stddraw.show(frame_timing)

if __name__ == "__main__": main()
