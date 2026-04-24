import stdio, stddraw # type: ignore

import Visuals.screens as screens

def main() -> None:
    stdio.writeln("Initialising Project Cosmic")

    # Luhan | CANVAS SETUP
    stddraw.setCanvasSize(w=750, h=1000)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1.4)

    screens.show_start() # Enter project cosmic


if __name__ == "__main__": main()
