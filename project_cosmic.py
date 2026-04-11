import stddraw, stdio, sys

def main() -> None: 
    stdio.writeln("Initialising Project Cosmic")

    # Luhan Steenberg | Canvas Setup
    stddraw.setCanvasSize(w=512, h=512)



    # Luhan Steenberg | Main Program control loop
    
    while True: 
        # Function-Calling code goes here
        
        stddraw.clear(stddraw.GRAY)
        
        # Draw the next frame here

        stddraw.show()



if __name__ == "__main__": main()
