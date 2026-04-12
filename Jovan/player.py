import sys
import math
import stddraw
import stdio
import playertype

def PlayerDisplay(p : Player) -> None: # displays the actual palyer depending on where he is 



    stddraw.clear

    # Both functions will look at the inputs by the player to determine where the player is and how it is rotated

    PlayerMovement(p)
    PlayerRotate(p)     

    stddraw.filledCircle(p.x, p.y, 5)


def PlayerMovement(p : Player) -> None: # Determines if and where player moves horizontoly 
    if PlayerRight :
        p.x += 1
    elif PlayerLeft :
        p.x -= 1
    elif PlayerStop :  
        return


def PlayerRotate(p : Player) -> None:  # Determines if and where player rotates towards
    if PlayerRotateRight :
        p.angle += 1 
    elif PlayerRotateLeft : 
        p.angle -= 1
    elif PlayerRotateStop :
        return


       
          
        



def PlayerRight() -> bool:      # player goes right if d is pressed 
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == 'd':
            return True

def PlayerLeft() -> bool:       # player goes left if a is pressed 
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == 'a':
            return True

def PlayerStop() -> bool:       # player stops moving if s is pressed 
    if stddraw.hasNextKeyTyped():
        key == stddraw.nextKeyTyped()
        if key == 's':
            return True

def PlayerRotateRight() -> bool:        # player rotates right if q is pressed
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == 'q':
            return True

def PlayerRotateLeft() -> bool:     # player rotates left if e is pressed 
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == 'e':
            return True

def PlayerRotateStop() -> bool:     # player stops rotating if w is pressed 
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == 'w':
            return True







