class Player:
    # Creating a player data type that tracks the players position, angle of shooter and health

    def __init__(self, x: float, y: float, angle: float, health: int):
        self.x = float(x)
        self.y = float(y)
        self.angle = float(angle)
        self.health = int(health)

        # Variables that gets changed to update the players movement

        self.vx = 0.0
        self.vangle = 0.0
