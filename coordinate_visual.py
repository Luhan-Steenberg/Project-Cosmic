import stddraw # type: ignore

def draw_coordinate_grid(max_x: float, max_y: float, step: float = 1):
    """
    Generates and draws a labeled coordinate grid, supporting float boundaries.
    """
    # 2. Draw the underlying grid lines in light gray
    stddraw.setPenColor(stddraw.LIGHT_GRAY)
    stddraw.setPenRadius(0.002)

    # Calculate grid bounds explicitly as integers to satisfy range()
    x_steps = int(max_x // step) + 1
    y_steps = int(max_y // step) + 1

    # Vertical lines
    for i in range(x_steps):
        x = i * step
        stddraw.line(x, 0, x, max_y)

    # Horizontal lines
    for j in range(y_steps):
        y = j * step
        stddraw.line(0, y, max_x, y)

    # 3. Draw the intersection points and coordinate labels
    stddraw.setPenColor(stddraw.BLACK)

    for i in range(x_steps):
        for j in range(y_steps):
            x = i * step
            y = j * step

            # Plot the point
            stddraw.setPenRadius(0.01)
            stddraw.point(x, y)

            # Label the point
            stddraw.setPenRadius()
            # The :g formatter ensures clean float printing (e.g., drops trailing zeros)
            label = f"({x:g},{y:g})"
            stddraw.text(x + (step * 0.15), y + (step * 0.15), label)

    # 4. Render the drawing to the window
    stddraw.show(2000)

# --- Example Usage ---
if __name__ == "__main__":
    # Draws a 5x5 grid with lines at every 1 unit
    draw_coordinate_grid(5, 5, 1)
