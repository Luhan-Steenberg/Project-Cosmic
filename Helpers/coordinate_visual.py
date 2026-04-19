import stddraw # type: ignore

def draw_coordinate_grid(max_x: float, max_y: float, step: float = 1):
    """
    Generates and draws a labeled coordinate grid, supporting float boundaries.
    """

    stddraw.setPenColor(stddraw.LIGHT_GRAY)
    stddraw.setPenRadius(0.002)

    x_steps = int(max_x // step) + 1
    y_steps = int(max_y // step) + 1

    # Gridlines
    for i in range(x_steps):
        x = i * step
        stddraw.line(x, 0, x, max_y)
    for j in range(y_steps):
        y = j * step
        stddraw.line(0, y, max_x, y)

    stddraw.setPenColor(stddraw.BLACK)

    for i in range(x_steps):
        for j in range(y_steps):
            x = i * step
            y = j * step

            stddraw.setPenRadius(0.01)
            stddraw.point(x, y)

            stddraw.setPenRadius()
            label = f"({x:g},{y:g})"
            stddraw.text(x + (step * 0.15), y + (step * 0.15), label)

    stddraw.show()

def main() -> None:
    # Luhan Steenberg | Canvas Setup
    stddraw.setCanvasSize(w=750, h=1000)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1.4)

    draw_coordinate_grid(1, 1.4, 0.1)

if __name__ == "__main__": main()
