import time

import stddraw, stdio, stdaudio

from picture import Picture


from Jovan.player import Player
from Francois.bullet import Bullet, Bullet_Manager, Explosion_Manager
import Luhan.aliens as Aliens
import Visuals.screens as screens
import Visuals.score_bars as score_bars
from game_over import game_over, win_screen

BACKGROUND = Picture("Cosmic_background.png")

def play(multiplayerFlag: bool):
    print("Game Set")

    # PARAMETERS
    frame_timing = 33
    level = 1

    # Player Setup for Multiplayer
    if multiplayerFlag:
        p1 = Player(1, 3, 0.4)
        p2 = Player(2, 3, 0.6)
        health = 6
    else:
        p1  = Player(1, 6)
        health = 0

    # Alien Setup
    alien_manager = Aliens.Alien_Manager() # Start at Level 1

    # Bullet Setup
    alien_bullets = Bullet_Manager()

    p1_bullets = Bullet_Manager()
    p2_bullets = Bullet_Manager()

    explosion_manager = Explosion_Manager()

    playing = True
    key = None
    while playing:
        c_time = time.time()
        stddraw.clear()
        stddraw.picture(BACKGROUND, 0.5, 0.7)

        alien_manager.update(c_time)
        alien_bullets.update()
        p1_bullets.update()
        p2_bullets.update()
        explosion_manager.update()

        # Luhan | This is Jovan's implementation moved here for multiplayer
        key = None
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

        if multiplayerFlag:
            p2.update(c_time, p2_bullets, 0.008, key)
            p1.update(c_time, p1_bullets, 0.008, key)

            p2.score += alien_manager.check_collision(p2_bullets, explosion_manager)

            players_score = p1.score + p2.score # for levels
            score_bars.m_score_bar(level, health, p1.score, p2.score)

            # EXIT CONDITION
            if health <= 0:
                playing = False
        else:
            p1.update(c_time, p1_bullets, 0.008, key)
            p1.score += alien_manager.check_collision(p1_bullets, explosion_manager)

            score_bars.score_bar(level, p1)
            players_score = p1.score

            if p1.health <= 0:
                playing = False



        if alien_manager.out_of_bounds():
            p1.update_health(1)
            health -= 1

        if players_score >= (1000 * level): # takes into account both scores
            level += 1
            if level != alien_manager.level:
                update_level_attributes(alien_manager, level)

        if level % 10 == 0 and not alien_manager.boss_active:
            alien_manager.add_boss(alien_bullets)

        if alien_manager.boss_just_died:
            win_screen(level, players_score, multiplayerFlag)
            alien_manager.boss_just_died = False

        stddraw.show(frame_timing)

    game_over(level, players_score, multiplayerFlag)
    return



# I should implement some function which clears the different managers
# This function should be called by the "end screen" function after it is exited for whatever reason.

def update_level_attributes(alien_manager, level):
    """
    Level Attributes:
    - alien_speed
    - alien_scale
    - alien_health
    - spawn_timing
    """
    if level % 2 == 0:
        if level % 5 == 0: alien_manager.spawn_timing -= 0.003
        elif level % 3 == 0: pass
        else: alien_manager.alien_scale += 1
    else:
        if level % 5 == 0: pass
        elif level % 3 == 0: alien_manager.alien_speed += 0.0005
        else: alien_manager.alien_health += 0.5




