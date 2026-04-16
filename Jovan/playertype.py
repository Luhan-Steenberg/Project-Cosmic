import math

# Jovan Fourie

class Player:
    # Jovan Fourie | Creating a player data type that tracks the players position, angle of shooter and health
    
    def __init__(self, x: float, y: float, angle: float, health: int):
        self.x = float(x)
        self.y = float(y)
        self.angle = float(angle)
        self.health = int(health)

        # Jovan fourie | Variables that gets changed to update the players movement

        self.vx = 0.0
        self.vangle = 0.0

        # Jovan Fourie | gets the actual angle from the horizontal axes to shoot the bullet

    def getShootAngle(self) -> float:
        if self.angle < 0:
            return abs(self.angle) + 90
        else:
            return 90 - self.angle

    def getShootX(self) -> float:   # Jovan Fourie | Gets the x value of where the shooters nozzle is pointing at
        a = math.radians(self.angle)
        return (self.x + 0.06 * math.sin(a))
             
    def getShootY(self) -> float:   # Jovan Fourie | Gets the y value of where the shooters nozzle is pointing at 
        a = math.radians(self.angle)
        return (self.y + 0.06 * math.cos(a))
